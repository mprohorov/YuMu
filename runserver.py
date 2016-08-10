from flask import Flask, render_template, request, jsonify
import socket
import ast


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('greet.html')
#@app.route('login')
#def login():
#    return render_template('login.html')
#@app.route('signup')
#def signup():
#    return render_template('signup.html')
IP = socket.gethostbyname(socket.gethostname())
if __name__ == '__main__':
    app.run(host=IP, port=8901, threaded=True)

@app.route('/_add_numbers')
def add_numbers():
    res = ast.literal_eval(request.args.keys()[0])
    number1 = res['number1']
    number2 = res['number2']
    return jsonify(number1 + number2)
