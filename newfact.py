from flask import Flask, request, url_for, render_template
import sqlite3 as lite
import sms
import db
import sys

# import the data from the Phone Number List (SELECT phone FROM numbers)

# Text should be the random row index taking the fact data to send (SELECT * FROM table ORDER BY RAND() LIMIT X)
text = SELECT fact FROM facts ORDER BY RAND() LIMIT 1 


app = Flask(__name__)

#Information about 


sendSMS(self, text, num)