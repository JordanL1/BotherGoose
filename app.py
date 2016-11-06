from flask import Flask, request, url_for, render_template
import sms
import db
import sys

text = "Thanks for signing up with Bother Goose. Stay tuned for some goosey banter!"

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_post():
    num = request.form['phoneNumber']
    email = request.form['email']

    db.db_add(num, email)

    sms.sms_out(text, num)

    return render_template('confirmation.html')