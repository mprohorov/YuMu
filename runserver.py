from flask import Flask, render_template, request
import socket

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
    app.run(host=IP, port=8900, threaded=True)
