from twilio.rest import TwilioRestClient
import twilio_tokens

class sms_out():
    client = TwilioRestClient(twilio_tokens.account_sid,
                              twilio_tokens.auth_token)

    def send_sms(self, text, nums):
        for x in xrange(len(nums)):
            message = self.client.messages.create(body=text,
                                                  to=nums[x],  # Replace with your phone number
                                                  from_="+441423740821")  # Our Twilio number