from flask import Flask, request, render_template
import sms
import db
import send

text = "Thanks for signing up with Bother Goose. Stay tuned for some goosey banter!"

app = Flask(__name__)
sender = send.sender()
sender.main()

@app.route('/', methods=['GET'])
def home_page():
    """Show home page when receiving get request to '/'."""
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_post():
    """Add contact details from form to database.  Send an automated SMS to the registered number."""
    num = request.form['phoneNumber']
    email = request.form['email']

    db.db_add(num, email)

    sms_obj = sms.sms_out()

    sms_obj.send_sms2(text, num)

    return render_template('confirmation.html')