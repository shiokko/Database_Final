from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import os
import random
from crud import exe_sql, add_Blist, delete_Blist, get_History, read_User
from crud import random_Restaurant, search_Restaurant, Rating, get_Restaurants, get_Blacklist, remove_Blacklist

app = Flask(__name__)
app.secret_key = 'key'  # this is a requirement for using session

# 連接到 SQLite 資料庫
conn = sqlite3.connect('project.db')
cursor = conn.cursor()

# 定義資料夾路徑
sql_folder = 'Database'

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

exe_sql(sql_folder,insert_files)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        session['username'] = name  # Store username in session
        read_User(name)
        return redirect(url_for('welcome'))

    return render_template('index.html')


@app.route('/home')
def welcome():
    username = session.get('username')  # 從 session 取得使用者名稱
    if not username:
        return redirect(url_for('login'))  # 如果未登入，跳轉到登入頁面
   
    # 查詢餐廳名稱和其類型
    formatted_restaurants = get_Restaurants()
    # 渲染首頁並傳遞使用者名稱和整理後的餐廳資料
    return render_template('home.html', username=username, restaurants=formatted_restaurants)


@app.route('/home/history')
def history():
    username = session.get('username')  # Fetch username from session
    if not username:
        return redirect(url_for('login'))
    
    history_list =get_History(username)

    return render_template('history.html', username=username, history_list=history_list)


@app.route('/home/rating')
def rating():
    username = session.get('username')  # Fetch username from session
    if not username:
        return redirect(url_for('login'))
    return render_template('rating.html', username=username)


@app.route('/get_random_restaurant', methods=['GET'])
def get_random_restaurant():
    username = session.get('username')
    restaurant = random_Restaurant(username)
    if restaurant['restaurant_name'] == "No restaurant found":
        # 當結果為空時返回錯誤訊息
        return jsonify({
            'error': 'No restaurant data available',
            'details': restaurant
        }), 404
    else:
        return jsonify(restaurant), 200

@app.route('/logout')
def logout():
    session.clear()  # Clear session on logout
    return redirect(url_for('login'))

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip().lower()
    filter_types = request.args.getlist('type')
    results = search_Restaurant(query, filter_types)
   
    return render_template('search.html', results=results, query=query, filter_types=filter_types)

@app.route('/submit_rating', methods=['POST'])
def submit_rating():
    username = session.get('username')
    rating = request.form['rating']
    review = request.form['review']
    restaurant_ID = request.form['restaurant_id']
    blacklist = request.form.get('blacklist') == 'true'  # 判斷是否勾選黑名單
    new_h_id = Rating(username, restaurant_ID, rating, review)

    if not new_h_id:
        return jsonify({'error': '找不到，滾出政大'}), 400

    if blacklist:
        added = add_Blist(new_h_id, username)


    # # if remove_blacklist:
    # #     removed = delete_Blacklist(new_h_id)
    
    return jsonify({'success': True, 'history_id': new_h_id})


@app.route('/get_blacklist')
def printBlacklist():
    username = session.get('username')
    if not username:
        # Handle the case when the username is not available in the session
        return redirect('/login')  # Or redirect to an appropriate page
    data = get_Blacklist(username)
    return jsonify(data)


@app.route('/removeblacklist', methods=['POST'])
def remove_from_blacklist():
    try:
        data = request.get_json()
        user_id = data.get('userId')

        result = remove_Blacklist(user_id)

        success = True

        # Return a JSON response
        return jsonify({'success': success})
    except Exception as e:
        print(f"Error removing user from blacklist: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

