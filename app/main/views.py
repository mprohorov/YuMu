import flask_login
from flask import render_template, request, jsonify, redirect, url_for

from app.main import writeinputs
from . import main
from yelpquery import get_results
from app import dbconnect
from app import models

@main.route('/')
def index():
    return render_template('index.html')
@main.route('/pref1')
def pref1():
    return render_template('prefs-one.html')
@main.route('/signup')
def signup():
    return render_template('signup.html')
@main.route('/signin')
def signin():
    return render_template('signin.html')
@main.route('/home')
def home():
    return render_template('home.html')
@main.route('/pref2')
def pref2():
    return render_template('prefs-two.html')
@main.route('/create')
def create():
    return render_template('create.html')
@main.route('/newevent', methods = ['POST'])
def newevent():
    res = request.json
    date = str(res['Date'])
    title = str(res['Title'])
<<<<<<< Updated upstream
    deadline = str(res['Deadline'])
    invitedFriends = []
    for item in res['InvitedFriends']:
        invitedFriends.append(str(item))
    writeinputs.createEvent(date, title, deadline)
'''''
=======
    invitedFriends = []
    for item in res['InvitedFriends']:
        invitedFriends.append(str(item))
    print(title)
    writeinputs.createEvent(ymdh, deadline, title)
"""
>>>>>>> Stashed changes
@main.route('/signin', methods = ['GET', 'POST'])
def signin():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = account.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']
            ):
                login_user(user)
                flash('You were logged in.')
                return redirect(url_for('home.home'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)
'''''

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
    writeinputs.enterPrefs2(budget, startTime, endTime)
@main.route('/testlogin')
def testlogin():
    res = request.json
    email = str(res['Email'])
    password = str(res['Password'])
    user = dbconnect.session.query(models.account).filter(models.account.email.like(email)).one()
    if user != None:
        if password == user.password:
            user.authenticated = True
            dbconnect.session.add(user)
            dbconnect.session.commit()
            flask_login.login_user(user, remember = True)
            return redirect(url_for('home'))
@main.route('/list')
def compromise():
    active = 0
    arts = 0
    beauty = 0
    education = 0
    food = 0
    nightlife = 0
    restaurant = 0
    shopping = 0
    for item in dbconnect.session.query(models.preferences.category).all():
        if "active" in item:
            active += 1
        if "arts" in item:
            arts += 1
        if "beauty" in item:
            beauty += 1
        if "education" in item:
            education += 1
        if "food" in item:
            food += 1
        if "nightlife" in item:
            nightlife += 1
        if "restaurant" in item:
            restaurant += 1
        if "shopping" in item:
            shopping += 1
    tempList = [active, arts, beauty, education, food, nightlife, restaurant, shopping]
    catList = ["active", "arts", "beauty", "education", "food", "nightlife", "restaurant", "shopping"]
    category_filter = catList[tempList.index(max(tempList))]
    budgetList = [0, 0, 0, 0]
    for item in dbconnect.session.query(models.preferences.budget).all():
        if item == "$":
            budgetList[0] += 1.5
        elif item == "$$":
            budgetList[1] += 1.25
        elif item == "$$$":
            budgetList[2] += 1
    budget = budgetList.index(max(budgetList)) + 1
    #hardcode location???
    startTimes = []
    endTimes = []
    for item in dbconnect.session.query(models.times.startTime).all():
        startTimes.append(item)
    for item in dbconnect.session.query(models.times.endTime).all():
        endTimes.append(item)
    compromiseTime = []
    compromiseTime.append(max(startTimes))
    compromiseTime.append(min(endTimes))
    params = {
        'lang': 'eng',
        'location': 'New York',
        'sort': 2,
        'category_filter': category_filter
    }
    ret = get_results(params)
    ret = ret['businesses']
    for item in ret:
        print item["name"]

