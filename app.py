from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'key'  # this is a requirement for using session



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        session['username'] = name  # Store username in session
        return redirect(url_for('welcome'))

    return render_template('index.html')


@app.route('/home')
def welcome():
    username = session.get('username')      # Fetch username from session
    if not username:
        return redirect(url_for('login'))  # Redirect to login if not logged in
    return render_template('home.html', username=username)


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


@app.route('/logout')
def logout():
    session.clear()  # Clear session on logout
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

