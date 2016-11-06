from twilio.rest import TwilioRestClient
import twilio_tokens

class sms_out():
    client = TwilioRestClient(twilio_tokens.account_sid,
                              twilio_tokens.auth_token)
    twilio_number = '+441423740821'
	def send_sms2(self, text, nums):
		message = self.client.messages.create(body=text, to=nums, from_= self.twilio_number) # Our Twilio number
		
    def send_sms(self, text, nums):
        for x in range(1, len(nums)):
            message = self.client.messages.create(body=text, to=nums[x], from_= self.twilio_number); # Our Twilio number
	
