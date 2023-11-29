# from twilio.twiml.voice_response import Gather, VoiceResponse
# from twilio.rest import Client
# import time
# import requests

# # Twilio Account SID and Auth Token
# account_sid = "AC4cc5b473630fa06d6b8f864f9c743582"
# auth_token = "74998b5f06388dc6f7e8af97ff4d0935"

# # Create a Twilio client
# client = Client(account_sid, auth_token)

# # Phone number to call
# to_phone_number = ["+919025614379"]

# # Questions for the survey
# questions = [
#     "Welcome to DCI. We are calling from the HR team.",
#     "Question 1: May I know your name?",
#     "Okay , Question 2: please let me know which domain you want to choose.",
#     "Question 3: Please let me know your years of experience.",
#     "Thanks for your answers. We will get back to you shortly."
# ]

# # Twilio phone number
# from_phone_number = "+19802245395"  # Your Twilio phone number

# # Function to ask a question
# def ask_question(question, gather, voice_response):
#     gather.say(question)
#     voice_response.append(gather)

# # Create a TwiML response
# voice_response = VoiceResponse()

# for question in questions:
#     gather = Gather(numDigits=1, action='/process_survey', method='POST')
#     ask_question(question, gather, voice_response)
#     time.sleep(5)  # Wait for 5 seconds before asking the next question

# # Make the call
# call = client.calls.create(
#     to=to_phone_number,
#     from_=from_phone_number,
#     twiml=str(voice_response),
#     record=True
# )

# print(f"Calling {to_phone_number}...")

# # Twilio recording URL
# recording_url = 'https://api.twilio.com/2010-04-01/Accounts/AC4cc5b473630fa06d6b8f864f9c743582/Recordings/RE45350633359794c35fed278c67a5f0e9.wav'

# # Set up HTTP Basic Authentication
# auth = (account_sid, auth_token)

# # Send a GET request to download the recording
# response = requests.get(recording_url, auth=auth)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Specify the local file name to save the recording
#     local_filename = 'recording.wav'

#     # Open the local file in binary write mode and write the response content (audio data) to it
#     with open(local_filename, 'wb') as f:
#         f.write(response.content)

#     print(f"Recording saved as {local_filename}")
# else:
#     print(f"Failed to download recording. Status code: {response.status_code}")




import os
from twilio.rest import Client
import requests

# Twilio Account SID and Auth Token
account_sid = "AC4cc5b473630fa06d6b8f864f9c743582"
auth_token = "74998b5f06388dc6f7e8af97ff4d0935"

# Create a Twilio client
client = Client(account_sid, auth_token)

# Define the call SID for the call you want to retrieve the recording from
call_sid = "CA2694f51bb758dc2b2bd38d98fc3daa83"

# # Use the Twilio API to list the recordings for the specified call
# recordings = client.recordings.list(call_sid=call_sid)

# Use the Twilio API to list the recordings for the specified call
recordings = client.recordings.list(call_sid=call_sid)
print(recordings)

# Sort the recordings by date_created in descending order to get the most recent one
recordings.sort(key=lambda x: x.date_created, reverse=True)

# Check if there are any recordings
if recordings:
    # Get the URL of the most recent recording (media_url)
    recording_media_url = recordings[0].media_url + ".wav"  # Add ".wav" extension
    print(recording_media_url)

    # Set up HTTP Basic Authentication
    auth = (account_sid, auth_token)

    # Send a GET request to download the recording
    response = requests.get(recording_media_url, auth=auth)
    print(response)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Specify the local file name to save the recording
        local_filename = 'recording.wav'

        # Open the local file in binary write mode and write the response content (audio data) to it
        with open(local_filename, 'wb') as f:
            f.write(response.content)

        print(f"Recording saved as {local_filename}")
    else:
        print(f"Failed to download recording. Status code: {response.status_code}")
else:
    print("No recordings found for the specified call.")






