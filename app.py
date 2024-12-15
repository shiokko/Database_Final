from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':
        name = request.form['username']
        print(name)
        return redirect(url_for('welcome', username=name))
    
    return render_template('index.html')

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('home.html', username=username)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

