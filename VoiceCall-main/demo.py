
# from twilio.twiml.voice_response import Gather, VoiceResponse
# from twilio.rest import Client
# import time

# # Twilio Account SID and Auth Token
# account_sid = "AC4cc5b473630fa06d6b8f864f9c743582"
# auth_token = "74998b5f06388dc6f7e8af97ff4d0935"

# # Create a Twilio client
# client = Client(account_sid, auth_token)

# # Phone number to call
# to_phone_number = ["+919025614379"]

# # Questions for the survey
# questions = [
#     "Welcome to Dci we are calling from HR team.",
#     "Question 1: may i know your name",
#     "Question 2: ok,please let me know which domain do you want to choose",
#     "Question 3: please let me know your years of experience ",
#     "Thanks for your answers. we will get back to you shortly"
# ]
 
# # Twilio phone number
# from_phone_number = "+19802245395" # Your Twilio phone number

# # Function to ask a question
# def ask_question(question, gather, voice_response):
#     gather.say(question)
#     voice_response.append(gather)

# # Create a TwiML response
# voice_response = VoiceResponse()

# for question in questions:
#     gather = Gather(numDigits=1, action='/process_survey', method='POST')
#     ask_question(question, gather, voice_response)
#     # gather.record(timeout=10,maxLength=30)
#     time.sleep(5)  # Wait for 5 seconds before asking the next question

# # Make the call
# call = client.calls.create(
#     to=to_phone_number,
#     from_=from_phone_number,
#     twiml=str(voice_response),
#     record = True
# )

# print(f"Calling {to_phone_number}...")

from twilio.twiml.voice_response import Gather, VoiceResponse
from twilio.rest import Client
import time

# Twilio Account SID and Auth Token for making a phone call
account_sid = "AC4cc5b473630fa06d6b8f864f9c743582"
auth_token = "74998b5f06388dc6f7e8af97ff4d0935"

# Create a Twilio client for making a phone call
call_client = Client(account_sid, auth_token)

# Phone number to call
to_phone_number = ["+919025614379"]

# Questions for the survey
questions = [
    "Welcome to DCI. we are calling from HR team.",
    "Question 1: may I know your name",
    "Okay, Question 2: please let me know which domain do you want to choose",
    "Question 3: please let me know your years of experience",
    "Thanks for your answers. We will get back to you shortly."
]

# Twilio phone number for making a call
from_phone_number = "+19802245395"  # Your Twilio phone number

# Create a TwiML response for the call with voice set to "Polly.Salli"
voice_response = VoiceResponse(voice='Polly.Matthew')

# Function to ask a question during the call
def ask_question(question, gather, voice_response):
    gather.say(question)
    voice_response.append(gather)

for question in questions:
    gather = Gather(numDigits=1, action='/process_survey', method='POST')
    ask_question(question, gather, voice_response)
    time.sleep(5)  # Wait for 5 seconds before asking the next question

# Make the call
call = call_client.calls.create(
    to=to_phone_number,
    from_=from_phone_number,
    twiml=str(voice_response),
    record=True
)

print(f"Calling {to_phone_number}...")
