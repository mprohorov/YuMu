
from flask import render_template, request, jsonify, redirect, url_for, flash, g, make_response
import flask_login
from flask_login import login_user, LoginManager, current_user
#from flask_security import login_required
from app import writeinputs
from app.auth.forms import LoginForm
from app.models import account
from . import main


@main.route('/')
def index():
    return render_template('greeting.html')
@main.route('/pref')
def pref():
    return render_template('pref.html')
@main.route('/signup')
def signup():
    return render_template('signup.html')
@main.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = account.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('home'))
        flash('Invalid username or password')
    return render_template('signin.html', form=form)
@main.route('/_add_numbers', methods = ['POST'])
def add_numbers():
    res = request.json
    print res
    number1 = int(res['number1'])
    number2 = int(res['number2'])
    return jsonify(res = (number1 + number2))
@main.route('/home1', methods = ['POST'])
def home1():
    res = request.json
    firstName = str(res['FirstName'])
    lastName = str(res['LastName'])
    email = str(res['Email'])
    password = str(res['Password'])
    phoneNumber = str(res['PhoneNumber'])
    print(firstName)
    writeinputs.createAccount(email, phoneNumber, firstName, lastName, password)
    """
    return jsonify(name = (firstName + lastName),
                   email = email,
                   password = password,
                   phoneNumber = phoneNumber)
    """
@main.route('/home2', methods = ['POST'])
def home2():
    res = request.json
    email = str(res['Email'])
    password = str(res['Password'])
    return jsonify(email = email,
                   password = password)
@main.route('/pref1info', methods = ['POST'])
def pref1info():
    res = request.json
    latitude = float(res["latitude"])
    longitude = float(res["longitude"])
    category = ""
    listOfCat = ["active", "arts", "beautysvc", "education", "food", "nightlife", "restaurants", "shopping"]
    for item in listOfCat:
        if str(res[item]) == "true":
            category += item
    writeinputs.enterPrefs1(latitude, longitude, category)
@main.route('/pref2info', methods = ['POST'])
def pref2info():
    res = request.json
    budget = int(res["budget"])
    startTime = str(res["startTime"])
    endTime = str(res["endTime"])
    #do yo database thing on budget, start and endTime
    writeinputs.enterPrefs2(budget, startTime, endTime)

