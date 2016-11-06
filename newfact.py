from flask import Flask, request, url_for, render_template
import sqlite3 as lite
import sms
import db
import sys

# Text should be the random row index taking the fact data to send (SELECT * FROM table ORDER BY RAND() LIMIT X)
text = SELECT * FROM facts ORDER BY RAND() LIMIT 1 
# import the data from the Phone Number List (SELECT phone FROM numbers)
num = SELECT DISTINCT number FROM number
#

# Credential Usage
sms_out()

# Sends info with numbers used and 
send_sms(self, text, num)