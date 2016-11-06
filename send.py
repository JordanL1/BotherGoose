"""import requests
import time
import atexit
import sms
import json
import sms

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

class sender():
    send_rate = 1
    last_send_time = time.time()

    def send_facts(self):

    def start_send_loop(self):
        scheduler = BackgroundScheduler()
        scheduler.start()
        scheduler.add_job(
            func=self.query_tfl,
            trigger=IntervalTrigger(seconds=self.query_rate),
            id='SMS_Send_Job',
            name='Query TFL every ' + str(self.query_rate) + ' seconds',
            replace_existing=True)
        # Shut down the scheduler when exiting the app
        atexit.register(lambda: scheduler.shutdown())"""