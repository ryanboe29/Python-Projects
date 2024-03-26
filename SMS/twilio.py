#This will use Twilio API, this will try and send a text message to my phone
#I would have had to create a Twilio account
from twilio.rest import Client

account_sid = 'askldfjowerbtbvvhydeowns'
auth_token = '[AuthToken given by Twilio]'
client = Client(account_sid, auth_token)

messsage = client.messages.create(from='your number', body='Hello' to='clients number')

print(message.sid)