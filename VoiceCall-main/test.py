

# # Twilio Account SID and Auth Token
# account_sid = "ACe441fcdf90078f4922d9dc517868eaf8"
# auth_token = "acc2c18427983146e98c3bc81d493898"


from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

# Twilio Account SID and Auth Token
account_sid = "AC4cc5b473630fa06d6b8f864f9c743582"
auth_token = "74998b5f06388dc6f7e8af97ff4d0935"

# Create a Twilio client
client = Client(account_sid, auth_token)

# Phone number to call
to_phone_number = "+919025614379"
from_phone_number = "+19802245395"
# Create a TwiML response with only the final message
final_response = VoiceResponse()
final_response.play('https://api.twilio.com/cowbell.mp3')

try:
    # Make the call
    call = client.calls.create(
        to=to_phone_number,
        from_=from_phone_number,  # Your Twilio phone number
        twiml=str(final_response),
        record=True,
    )

    print(f"Calling {to_phone_number}...")
    print("Call SID:", call.sid)
except Exception as e:
    print(f"Error making the call: {str(e)}")
