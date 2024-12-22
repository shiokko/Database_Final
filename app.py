from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import os
import random

app = Flask(__name__)
app.secret_key = 'key'  # this is a requirement for using session

# 連接到 SQLite 資料庫
conn = sqlite3.connect('project.db')
cursor = conn.cursor()

# 定義資料夾路徑
sql_folder = 'DATABASE'

# 執行 create_table.sql 建立資料表
# create_sql_path = os.path.join(sql_folder, 'create_table.sql')
# with open(create_sql_path, 'r', encoding='utf-8') as f:
#     create_sql = f.read()
#     cursor.executescript(create_sql)  # 批量執行建立表格的 SQL
#     print("資料表已建立。")

# 執行其他插入資料的 SQL 檔案
insert_files = [
    'insert_back_mountain.sql',
    'insert_inCampus.sql',
    'insert_left_side.sql',
    'insert_right_side.sql'
]

for file in insert_files:
    file_path = os.path.join(sql_folder, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        insert_sql = f.read()
        cursor.executescript(insert_sql)  # 批量執行插入資料的 SQL
        print(f"{file} 已執行並插入資料。")

# 提交更改並關閉連接
conn.commit()
conn.close()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        session['username'] = name  # Store username in session
        return redirect(url_for('welcome'))

    return render_template('index.html')


@app.route('/home')
def welcome():
    username = session.get('username')  # 從 session 取得使用者名稱
    if not username:
        return redirect(url_for('login'))  # 如果未登入，跳轉到登入頁面

    # 連接到資料庫
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    # 查詢餐廳名稱和其類型
    cursor.execute('''
        SELECT Restaurant.r_name, Type.t_name
        FROM Restaurant
        JOIN Restaurant_Types ON Restaurant.r_id = Restaurant_Types.r_id
        JOIN Type ON Restaurant_Types.t_id = Type.t_id
    ''')
    data = cursor.fetchall()

    # 關閉資料庫連接
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

    # 渲染首頁並傳遞使用者名稱和整理後的餐廳資料
    return render_template('home.html', username=username, restaurants=formatted_restaurants)



@app.route('/home/history')
def history():
    username = session.get('username')  # Fetch username from session
    if not username:
        return redirect(url_for('login'))
    return render_template('history.html', username=username)


@app.route('/home/rating')
def rating():
    username = session.get('username')  # Fetch username from session
    if not username:
        return redirect(url_for('login'))
    return render_template('rating.html', username=username)
@app.route('/get_random_restaurant', methods=['GET'])
def get_random_restaurant():
    # 連接到 SQLite 資料庫
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()
    
    # 隨機選擇一間餐廳
    cursor.execute('SELECT r_name, a_name, t_name FROM Restaurant '
                   'JOIN Area ON Restaurant.a_id = Area.a_id '
                   'JOIN Restaurant_Types ON Restaurant.r_id = Restaurant_Types.r_id '
                   'JOIN Type ON Restaurant_Types.t_id = Type.t_id '
                   'ORDER BY RANDOM() LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    
    if result:
        restaurant_name, area_name, type_name = result
    else:
        restaurant_name, area_name, type_name = "No restaurant found", "挖哩勒", "哭出來"
    
    # 返回 JSON 格式的餐廳資料
    return jsonify({
        'restaurant_name': restaurant_name,
        'area_name': area_name,
        'type_name': type_name
    })

@app.route('/logout')
def logout():
    session.clear()  # Clear session on logout
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

