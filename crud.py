import os
import sqlite3
import json
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

#連接到資料庫
def exe_sql(sql_folder,insert_files):
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()


#匯入資料
    for file in insert_files:
        file_path = os.path.join(sql_folder, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            insert_sql = f.read()
            cursor.executescript(insert_sql) 
            print(f"{file} 已執行並插入資料。")

    conn.commit()
    conn.close()

#新增黑名單
def add_Blist(h_id,username):
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    #check if user exsist
    cursor.execute('''
        SELECT u_id, Name FROM Users WHERE Name = ?
    ''',(username,))
    user = cursor.fetchone()

    if not user:
        conn.close()
        return False

    u_id = user[0]

     #insert blacklist
    cursor.execute('''
        INSERT INTO Blacklist (h_id, u_id, date)
        VALUES (?, ?, datetime('now'))
        ''', (h_id, u_id))
    conn.commit()
    conn.close()

    return True

#清除黑名單
def delete_Blist(black_id):
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM Blacklist
        Where b_id = ?
    ''', (black_id,))

    conn.commit()
    removed = cursor.rowcount > 0
    conn.close()

    return removed

#存入歷史資料
def get_History(username):
    conn = sqlite3.connect('project.db')
    conn.row_factory = sqlite3.Row  # Assign row factory before creating cursor
    cursor = conn.cursor()

    cursor.execute('SELECT u_id FROM Users WHERE Name = ?', (username,))
    user = cursor.fetchone()

    # 檢查用戶是否存在
    if not user:
        print(f"'{username}' doesn't exist")
        conn.close()
        return []

    u_id = user["u_id"]  # Extract user ID

    # 查詢用戶歷史紀錄
    cursor.execute('''
        SELECT r.r_name AS Restaurant_Name, h.Rate, h.Reviews
        FROM History h
        JOIN Restaurant r ON h.r_id = r.r_id
        WHERE h.u_id = ?
    ''', (u_id,))
    
    results = cursor.fetchall()
    conn.close()

    return [dict(row) for row in results] if results else []
   

#存入用戶資料log in(sign in)
def read_User(username):

    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    #確認是否sign up
    cursor.execute('''
        SELECT * FROM Users
        WHERE Name = ?
    ''',(username,))
    user = cursor.fetchone()

    if user:
        print(f"'{username}' already exists")
    else:
        # insert in to Users
        cursor.execute('INSERT INTO Users (Name) VALUES (?)', (username,))        
        conn.commit()
    conn.close()

#查詢和隨機餐廳選擇
def random_Restaurant(username):

    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()
    cursor.execute('SELECT u_id FROM Users WHERE Name = ?', (username,))
    user_id = cursor.fetchone()[0]

    cursor.execute('''
        SELECT Restaurant.r_id, r_name, a_name, t_name
        FROM Restaurant
        JOIN Area ON Restaurant.a_id = Area.a_id
        JOIN Restaurant_Types ON Restaurant.r_id = Restaurant_Types.r_id
        JOIN Type ON Restaurant_Types.t_id = Type.t_id
        WHERE Restaurant.r_id NOT IN (
            SELECT r_id
            FROM History
            WHERE h_id IN (
                SELECT h_id
                FROM Blacklist
                WHERE u_id = ?
            )
        )
        ORDER BY RANDOM()
        LIMIT 1
    ''', (user_id,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return {
                'restaurant_id': result[0],
                'restaurant_name': result[1],
                'area_name': result[2],
                'type_name': result[3]
        }
    else:
        return {
            'restaurant_id': None,
            'restaurant_name': "No restaurant found",
            'area_name': "挖哩勒",
            'type_name': "哭出來"
        }
     

def search_Restaurant(query,filter_types=None):

    base_query = """
        SELECT r_name, a_name, t_name
        FROM Restaurant
        JOIN Area ON Restaurant.a_id = Area.a_id
        JOIN Restaurant_Types ON Restaurant.r_id = Restaurant_Types.r_id
        JOIN Type ON Restaurant_Types.t_id = Type.t_id
        WHERE 1=1
    """
    params = []

     # 如果有搜尋關鍵字
    if query:
        base_query += " AND (LOWER(r_name) LIKE ? OR LOWER(t_name) LIKE ?)"
        params.extend([f"%{query}%", f"%{query}%"])

    # 如果有篩選條件
    if filter_types:
        placeholders = ",".join("?" for _ in filter_types)
        base_query += f" AND Type.t_id IN ({placeholders})"
        params.extend(filter_types)
    
    conn = sqlite3.connect('project.db')
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()


    cursor.execute(base_query, params)
    results = cursor.fetchall()
    conn.close()

    return results

#評分系統
def Rating(username, restaurant_id, rating, review):
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT u_id FROM Users WHERE Name = ?', (username,))
    user_id = cursor.fetchone()
    print(restaurant_id)
    print(user_id)

    #check if r or u exsists
    if not restaurant_id or not user_id:
        conn.close()
        return None

    user_id = user_id[0]

    #add into history
    cursor.execute('''
        INSERT INTO History (r_id, u_id, Rate, Reviews, Date)
        VALUES (?, ?, ?, ?, datetime('now'))
    ''', (restaurant_id, user_id, rating, review))
    conn.commit()
    new_h_id = cursor.lastrowid
    conn.close()
    return(new_h_id)



def get_Blacklist(username):
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()
    cursor.execute('SELECT u_id FROM Users WHERE Name = ?', (username,))
    user_id = cursor.fetchone()[0]
    cursor.execute('''
            SELECT Blacklist.b_id, Blacklist.date, History.r_id, Restaurant.r_name
            FROM Blacklist
            JOIN History ON Blacklist.h_id = History.h_id
            JOIN Restaurant ON History.r_id = Restaurant.r_id
            WHERE Blacklist.u_id = ?
        ''', (user_id,))
    results = cursor.fetchall()

    datas = []
    for result in results:
        # Example logic to map query result to user-like structure
        data = {
            "name": result[3],  # Assuming result[3] is the restaurant name
            "id": result[0],  # Assuming result[0] is the b_id (blacklist ID)
            "date": result[1],  # Assuming result[1] is the date
        }
        datas.append(data)
    return datas


def remove_Blacklist(blacklist_id):
    try:
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()

        cursor.execute('''
                DELETE FROM Blacklist
                WHERE b_id = ?;
            ''', (blacklist_id,))
        results = cursor.fetchall()

        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': f'User with b_id {blacklist_id} removed successfully.'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    return 0

def get_Restaurants():
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT Restaurant.r_name, Type.t_name
        FROM Restaurant
        JOIN Restaurant_Types ON Restaurant.r_id = Restaurant_Types.r_id
        JOIN Type ON Restaurant_Types.t_id = Type.t_id
    ''')
    data = cursor.fetchall()
    conn.close()

     # 使用字典來整理資料，將相同餐廳名稱的類型合併
    restaurants = {}
    for restaurant_name, type_name in data:
        if restaurant_name not in restaurants:
            restaurants[restaurant_name] = []
        restaurants[restaurant_name].append(type_name)

    # 將餐廳名稱和類型合併成字串
    formatted_restaurants = [
        f"{name} - {', '.join(types)}"
        for name, types in restaurants.items()
    ]

    return formatted_restaurants

