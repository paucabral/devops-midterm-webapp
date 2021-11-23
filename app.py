from flask import Flask, redirect, url_for, render_template, request
from api import login as loginAPI
from api import register as registerAPI

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/register", methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        response = registerAPI(username, password, email,
                               first_name, last_name)

        if "message" in response.keys():
            message = response['message']
            return render_template('registration.html', message=message)
        else:
            return redirect('/login')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        response = loginAPI(username, password)

        if "message" in response.keys():
            message = response['message']
            return render_template('login.html', message=message)
        else:
            return redirect('/login')


@app.route("/home", methods=['GET'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
