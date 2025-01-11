from flask import Flask, request, redirect, url_for, flash, render_template, jsonify, random, session
import sqlite3
import os

#連接到資料庫
conn = sqlite3.connect('project.db')
cursor = conn.cursor()

sql_folder = 'Database'

insert_files = [
        'insert_back_mountain.sql',
        'insert_inCampus.sql',
        'insert_left_side.sql',
        'insert_right_side.sql'
        ]

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
def add_Blist(black_id,username,black_date):
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    #check if user exsist
    cursor.execute('''
        SELECT u_id, Name FROM Users WHERE Name = ?
    ''',(username,))
    user = cursor.fetchone()

    if not user:
        print(f"'{username}' doesn't exist")
        conn.close()
        return

    u_id = user[0]

    #確認是否有同一筆黑名單
    cursor.execute('''
        SELECT * FROM Blacklist
        WHERE b_id = ? AND u_id = ?
    ''', (black_id, u_id))
    blacklist = cursor.fetchone()

    if blacklist:
        print(f"Blacklist already exists")
    else:
        #insert blacklist
        cursor.execute('''
            INSERT INTO Blacklist (b_id, u_id, date)
            VALUES (?, ?, ?)
        ''', (black_id, u_id, b_date))
        conn.commit()
    conn.close()



#清除黑名單
def delete_Blist(black_id):
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM Blacklist
        Where b_id = ?
    ''', (black_id,))

    conn.commit()
    print(f"Blacklist deleted successfully")
    conn.close()

#存入歷史資料
def add_History(history_id, username, restaurant_id, rate, reviews, history_date):
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    #check if user exsist
    cursor.execute('''
        SELECT u_id, Name FROM Users WHERE Name = ?
    ''',(username,))
    user = cursor.fetchone()

    if not user:
        print(f"'{username}' doesn't exist")
        conn.close()
        return

    u_id = user[0]

    #確認是否有同一筆歷史紀錄
    cursor.execute('''
        SELECT * FROM History
        WHERE h_id = ? AND u_id = ? AND Date = ?
    ''', (history_id, u_id, history_date))
    history = cursor.fetchone()

    if history:
        print(f"History already exists")
    else:
        # insert history
        cursor.execute('''
            INSERT INTO History (h_id, u_id, r_id, Rate, Reviews, Date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (history_id, u_id, restaurant_id, rate, reviews, history_date))
        conn.commit()
    conn.close()




#存入用戶資料log in(sign in)
def read_user(username):

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
        cursor.execute('''
            INSERT INTO Users (username) 
            VALUES (?)
        ''', (username))
        conn.commit()
        print(f"'{username}' added")

    conn.close()

#查詢和隨機餐廳選擇
def random_restaurant():

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




