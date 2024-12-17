from flask import Flask, render_template, redirect, url_for, request, flash
from crud import history_routes, blacklist_routes


app = Flask(__name__)
#protect path and data base
app.secret_key = "Secret Key"

app.register_blueprint(history_routes)
app.register_blueprint(blacklist_routes)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('welcome', username=username))
    return render_template('index.html')

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('home.html', username=username)

@app.route('/input')
def input_page():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        flash(f"Data Submitted: {username}")
        return redirect(url_for('home'))

if __name__ == '__main__':    
    app.run(debug=True, host='0.0.0.0', port=8080)

