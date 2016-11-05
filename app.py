from flask import Flask, request, url_for, render_template
import db
import sqlite3 as lite
import sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_post():
    num = request.form['phoneNumber']
    email = request.form['email']

    db.db_add(num, email)

    return render_template('confirmation.html')