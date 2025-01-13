import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json



conn = sqlite3.connect('project.db')
cursor = conn.cursor()
# cursor.execute('SELECT u_id FROM Users WHERE Name = ?', (username,))
user_id = 4
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
# columns = [description[0] for description in cursor.description]  # Get column names from the cursor
# data = [dict(zip(columns, row)) for row in results]

# # Convert the data to JSON format
# json_data = json.dumps(data, ensure_ascii=False, indent=4)
print(datas)
# print(rows[1])