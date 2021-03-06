import time
import atexit
import db
import sms

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

class sender():
    """Handle the sending of SMS at set intervals."""
    send_rate = 3600
    last_send_time = time.time()

    def send_facts(self):
        """Send an SMS to a list of numbers from the database, containing a random fact from the database."""
        sms_out = sms.sms_out()
        nums = db.db_getnums()
        text = db.db_getfacts()

        sms_out.send_sms(text, nums)


    def start_send_loop(self):
        """Schedule the task to send SMS at set intervals."""
        scheduler = BackgroundScheduler()
        scheduler.start()
        scheduler.add_job(
            func=self.send_facts,
            trigger=IntervalTrigger(seconds=self.send_rate),
            id='SMS_Send_Job',
            name='Send facts every ' + str(self.send_rate) + ' seconds',
            replace_existing=True)
        # Shut down the scheduler when exiting the app
        atexit.register(lambda: scheduler.shutdown())

    def main(self):
        self.start_send_loop()