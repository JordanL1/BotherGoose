from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def handle_post():
    num = request.form['phoneNumber']
    email = request.form['email']
    return render_template('confirmation.html')