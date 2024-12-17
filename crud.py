from flask import Flask, request, redirect, url_for, flash, render_template, Blueprint
import sqlite3
import os


DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Database/project.db")

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

history_routes = Blueprint('history_routes', __name__)
blacklist_routes = Blueprint('blacklist_routes', __name__)

#show history on the web
@history_routes.route('/history')
def view_history():
    conn = get_db_connection()
    history = conn.execute("SELECT * FROM History").fetchall()
    conn.close()
    return render_template('history.html', history=history)

#insert history record
@history_routes.route('/insert_history, methods=[POST]')
def insert_history():
    if request.method == 'POST':
        u_id = request.form['u_id']
        r_id = request.form['r_id']
        rate = request.form['rate']
        reviews = request.form['reviews']
        date = request.form['date']

        conn = get_db_connection()
        conn.execute("INSERT INTO History (u_id, r_id, rate, reviews, date) VALUES (?, ?, ?, ?, ?)",
                     (u_id, r_id, rate, reviews, date))
        conn.commit()
        conn.close()
        flash("History record added successfully")
        return redirect(url_for('view_history'))

#update history record
@history_routes.route('/update_history/<int:h_id>', methods=['GET', 'POST'])
def update_history(h_id):
    conn = get_db_connection()
    history = conn.execute("SELECT * FROM History WHERE h_id = ?", (h_id,)).fetchone()
    if request.method == 'POST':
        u_id = request.form['u_id']
        r_id = request.form['r_id']
        rate = request.form['rate']
        reviews = request.form['reviews']
        date = request.form['date']

        conn.execute("UPDATE History SET u_id = ?, r_id = ?, rate = ?, reviews = ?, date = ? WHERE h_id = ?",
                     (u_id, r_id, rate, reviews, date, h_id))
        conn.commit()
        conn.close()
        flash("History record updated successfully")
        return redirect(url_for('history_routes.view_history'))
    conn.close()
    return render_template('update_history.html', history=history)

#delete history record
@history_routes.route('/delete_history/<int:h_id>', methods=['POST'])
def delete_history(h_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM History WHERE h_id = ?", (h_id,))
    conn.commit()
    conn.close()
    flash("History record deleted successfully")
    return redirect(url_for('history_routes.view_history'))

#show blacklist on the web
@blacklist_routes.route('/blacklist')
def view_blacklist():
    conn = get_db_connection()
    blacklist = conn.execute("SELECT * FROM Blacklist").fetchall()
    conn.close()
    return render_template('blacklist.html', blacklist=blacklist)

#add blacklist record
@blacklist_routes.route('/add_blacklist', methods=['POST'])
def add_blacklist():
    if request.method == 'POST':
        b_id = request.form['b_id']
        u_id = request.form['u_id']
        date = request.form['date']

        conn = get_db_connection()
        conn.execute("INSERT INTO Blacklist (b_id, u_id, date) VALUES (?, ?, ?)",
                     (b_id, u_id, date))
        conn.commit()
        conn.close()
        flash("Blacklist record added successfully")
        return redirect(url_for('view_blacklist'))

#update blacklist record
@blacklist_routes.route('/update_blacklist/<int:b_id>/<int:u_id>', methods=['GET', 'POST'])
def update_blacklist(b_id, u_id):
    conn = get_db_connection()
    blacklist = conn.execute("SELECT * FROM Blacklist WHERE b_id = ? AND u_id = ?", (b_id, u_id)).fetchone()
    if request.method == 'POST':
        date = request.form['date']
        conn.execute("UPDATE Blacklist SET date = ? WHERE b_id = ? AND u_id = ?",
                     (date, b_id, u_id))
        conn.commit()
        conn.close()
        flash("Blacklist record updated successfully")
        return redirect(url_for('blacklist_routes.view_blacklist'))
    conn.close()
    return render_template('update_blacklist.html', blacklist=blacklist)

#delete blacklist record
@blacklist_routes.route('/delete_blacklist/<int:b_id>/<int:u_id>', methods=['POST'])
def delete_blacklist(b_id, u_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM Blacklist WHERE b_id = ? AND u_id = ?", (b_id, u_id))
    conn.commit()
    conn.close()
    flash("Blacklist record deleted successfully")
    return redirect(url_for('blacklist_routes.view_blacklist'))

