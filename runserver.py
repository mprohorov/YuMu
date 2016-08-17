from flask import Flask, render_template, request, jsonify
import socket
import ast


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('greeting.html')
@app.route('/pref')
def pref():
    return render_template('pref.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/signin')
def signin():
    return render_template('signin.html')
@app.route('/_add_numbers', methods = ['POST'])
def add_numbers():
    res = request.json
    print res
    number1 = int(res['number1'])
    number2 = int(res['number2'])
    return jsonify(res = (number1 + number2))
@app.route('/home1', methods = ['POST'])
def home1():
    res = request.json
    firstName = str(res['FirstName'])
    lastName = str(res['LastName'])
    email = str(res['Email'])
    password = str(res['Password'])
    phoneNumber = str(res['PhoneNumber'])
    return jsonify(name = (firstName + lastName),
                   email = email,
                   password = password,
                   phoneNumber = phoneNumber)
@app.route('/home2', methods = ['POST'])
def home2():
    res = request.json
    email = str(res['Email'])
    password = str(res['Password'])
    return jsonify(email = email,
                   password = password)

IP = socket.gethostbyname(socket.gethostname())
if __name__ == '__main__':
    app.run(host=IP, port=8901, threaded=True)
