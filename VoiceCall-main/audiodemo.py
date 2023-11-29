import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC4cc5b473630fa06d6b8f864f9c743582'
auth_token = '74998b5f06388dc6f7e8af97ff4d0935'
client = Client(account_sid, auth_token)

# transcription = client.transcriptions('TRac0f902cfd343dada03458388559b4bd').fetch()

# print(transcription.transcription_text)

transcript = client.intelligence.v2.transcripts.create(service_sid='GA3aba3527a37a2c9163f536b7e8edf121',channel={})

print(transcript.links)