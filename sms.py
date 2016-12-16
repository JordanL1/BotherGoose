from twilio.rest import TwilioRestClient
import twilio_tokens

class sms_out():
    """Handle the sending of SMS."""
    client = TwilioRestClient(twilio_tokens.account_sid,
                              twilio_tokens.auth_token)

    def send_sms_single(self, text, num):
        """Send a single SMS to given number."""
        message = self.client.messages.create(body=text, to=num, from_= '+441423740821') # Our Twilio number

    def send_sms(self, text, nums):
        """Send an SMS to a list of numbers."""
        for x in range(1, len(nums)):
            message = self.client.messages.create(body=text, to=nums[x], from_= '+441423740821') # Our Twilio numbers