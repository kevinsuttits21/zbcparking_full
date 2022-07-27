import os
import psycopg2
from flask import Flask, render_template, url_for, redirect, request
from config import config
from add_user_cc import add_user_cc
from reg import RegistrationForm, LoginForm, AdminLoginForm

app = Flask(__name__, static_folder="templates")
# app._static_folder = ''
app.config['SECRET_KEY'] = '9eb141fcd4cb15d6b5e5e2e135aa4c80'


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='ZBCParking',
                            user=os.environ['postgres'],
                            password=os.environ['password12345'])
    return conn


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/user/index.html")
def userdashboard():
    return render_template('user/index.html')


@app.route("/login.html", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('user/index.html')
    else:
        print("Login failed !, invalid credentials")
    return render_template('login.html', form=form)

@app.route("/user/password-reset.html")
def passwordreset():
    return render_template('/user/password-reset.html', methods=['POST', 'GET'])


@app.route("/user/billing.html")
def billing():
    return render_template('/user/billing.html')


@app.route("/admin")
def adminindex():
    return render_template('/admin/index.html')


@app.route("/admin/login.html", methods=['POST', 'GET'])
def adminlogin():
    form = AdminLoginForm()
    if form.validate_on_submit():
        return render_template('admin/dashboard.html')
    else:
        print("Login failed!, invalid credentials")
    return render_template('/admin/login.html', form=form)


@app.route("/admin/dashboard.html")
def admindashboard():
    return render_template('/admin/dashboard.html')


@app.route("/admin/password-reset.html", methods=['POST', 'GET'])
def adminpasswordreset():
    return render_template('/admin/password-reset.html')


@app.route("/admin/users.html")
def users():
    return render_template('/admin/users.html')


@app.route("/register.html", methods=['POST', 'GET'])
def register():
    print(request.method)
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        licenseplate = request.form['licensePlate']
        cardnumber = request.form['cardNumber']
        expirationmonth = request.form['expirationMonth']
        expirationyear = request.form['expirationYear']
        firstnamecard = request.form['firstNameCard']
        lastnamecard = request.form['lastNameCard']

        print(email, password)

    form = RegistrationForm()
    if form.validate_on_submit():
        add_user_cc(email, firstname, lastname, 1, password, licenseplate, cardnumber,
                    expirationmonth, expirationyear, firstnamecard, lastnamecard)
        return render_template('user/index.html')
    else:
        print("Registration failed!, invalid credentials")

    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)