import os
import sqlite3


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
        ''', (black_id, u_id))
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
    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row

    cursor.execute('SELECT u_id FROM Users WHERE Name = ?', (username,))
    user = cursor.fetchone()
    
    #check if user exsist
    if not user:
        print(f"'{username}' doesn't exist")
        conn.close()
        return []

    #查詢user紀錄
    cursor.execute('''
        SELECT r.r_name AS Restaurant_Name, h.Rate, h.Reviews 
        FROM History h 
        JOIN Restaurant r ON h.r_id = r.r_id
        JOIN Users u ON h.u_id = u.u_id
        WHERE u.Name = ?    
    ''',(username,))
    results = cursor.fetchall()
    conn.close()

    if results:
        return [dict(row) for row in results]
    else:
        return []    

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
def random_Restaurant():

    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    cursor.execute('SELECT r_name, a_name, t_name FROM Restaurant '
                   'JOIN Area ON Restaurant.a_id = Area.a_id '
                   'JOIN Restaurant_Types ON Restaurant.r_id = Restaurant_Types.r_id '
                   'JOIN Type ON Restaurant_Types.t_id = Type.t_id '
                   'ORDER BY RANDOM() LIMIT 1')
    result = cursor.fetchone()
    conn.close()

    if result:
        return{
            'restaurant_name': result[0],
            'area_name': result[1],
            'type_name': result[2]
                }
    else:
        return {
            'restaurant_name': "No restaurant found",
            'area_name': "挖哩勒",
            'type_name': "哭出來"
                }
     



def search_Restaurant(query):

    conn = sqlite3.connect('project.db')
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()

    cursor.execute("""
        SELECT r_name, a_name, t_name
        FROM Restaurant
        JOIN Area ON Restaurant.a_id = Area.a_id
        JOIN Restaurant_Types ON Restaurant.r_id = Restaurant_Types.r_id
        JOIN Type ON Restaurant_Types.t_id = Type.t_id
        WHERE LOWER(r_name) LIKE ? OR LOWER(t_name) LIKE ?
    """, (f"%{query}%", f"%{query}%"))
    results = [
        {'r_name': row['r_name'], 'a_name': row['a_name'], 't_name': row['t_name']}
        for row in cursor.fetchall()
    ]
    conn.close()

    return results

#評分系統
def Rating(username, restaurant_name, rating, review):
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()
    
    #查詢餐廳和users
    cursor.execute('SELECT r_id FROM Restaurant WHERE r_name = ?', (restaurant_name,))
    restaurant_id = cursor.fetchone()
    cursor.execute('SELECT u_id FROM Users WHERE Name = ?', (username,))
    user_id = cursor.fetchone()

    #check if r or u exsists
    if not restaurant_id or not user_id:
        conn.close()
        return None

    restaurant_id = restaurant_id[0]
    user_id = user_id[0]

    #add into history
    cursor.execute('''
        INSERT INTO History (r_id, u_id, Rate, Reviews, Date)
        VALUES (?, ?, ?, ?, datetime('now'))
    ''', (restaurant_id, user_id, rating, review))
    conn.commit()
    new_h_id = cursor.lastrowid
    conn.close()

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

    
