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

#清除歷史資料
def delete_Blist(black_id):
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE * FROM Blacklist
        Where b_id = ?
            ''', (black_id,))

    conn.commit()
    print(f"Blacklist deleted successfully")
    conn.close()

#存入用戶資料
def read_user(username):

        
    #存到Users Table
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM Users
        WHERE u_id = ?
    ''',(username,))
    user = cursor.fetchall()
    conn.close()



    





