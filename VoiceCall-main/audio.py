import requests

# Replace with your Twilio Account SID and Auth Token
account_sid = "AC4cc5b473630fa06d6b8f864f9c743582"
auth_token = "74998b5f06388dc6f7e8af97ff4d0935"

# Twilio recording URL
recording_url = 'https://api.twilio.com/2010-04-01/Accounts/AC4cc5b473630fa06d6b8f864f9c743582/Recordings/RE45350633359794c35fed278c67a5f0e9.wav'

# Set up HTTP Basic Authentication
auth = (account_sid, auth_token)

# Send a GET request to download the recording
response = requests.get(recording_url, auth=auth)

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
