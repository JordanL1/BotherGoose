from flask import Flask, request, url_for, render_template
import sms
import db
import send
import sys

text = "Thanks for signing up with Bother Goose. Stay tuned for some goosey banter!"

app = Flask(__name__)
sender = send.sender()
sender.main()

@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_post():
    num = request.form['phoneNumber']
    email = request.form['email']

    db.db_add(num, email)

    sms_obj = sms.sms_out()

    sms_obj.send_sms(text, num)

    return render_template('confirmation.html')