# from google.cloud import dialogflow
# import os

# # Set your Google Cloud service account key file path
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "adept-might-372205-48291665e5a9.json"

# # Set your Dialogflow project ID, session ID, and language code
# project_id = "adept-might-372205"
# session_id = "116479968643497663936"
# language_code = "en-US"

# # Initialize the Dialogflow client
# session_client = dialogflow.SessionsClient()
# session = session_client.session_path(project_id, session_id)

# # Function to send a query to Dialogflow and get the response
# def detect_intent(text):
#     text_input = dialogflow.TextInput(text=text, language_code=language_code)
#     query_input = dialogflow.QueryInput(text=text_input)
#     response = session_client.detect_intent(request={"session": session, "query_input": query_input})

#     # Check if Dialogflow provided a response
#     if response.query_result.query_text:
#         return response.query_result.fulfillment_text
#     else:
#         return "I'm sorry, I couldn't understand your query."

# # Dictionary mapping user queries to AI responses
# responses = {
#     "hello": "Hi there! How can I help you?",
#     "how are you": "I'm just a computer program, but I'm here to assist you.",
#     "what's the weather today": "I'm not equipped to provide weather information.",
#     "goodbye": "Goodbye! Have a great day!",
# }

# # Function to get AI response
# def get_response(user_input):
#     return responses.get(user_input, "I'm not sure how to respond to that.")

# # Main loop to interact with the AI
# if __name__ == "__main__":
#     print("AI: Hi, how can I assist you today?")
    
#     while True:
#         user_input = input("User: ").lower()
#         response = get_response(user_input)
#         print("AI:", response)

#-------------------------------------------------------------------------------------------

# from google.cloud import dialogflow
# from twilio.twiml.voice_response import Gather, VoiceResponse
# from twilio.rest import Client
# import os

# # Set up your Google Cloud service account key file path
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "adept-might-372205-48291665e5a9.json"

# # Set up your Dialogflow project ID, session ID, and language code
# project_id = "adept-might-372205"
# session_id = "116479968643497663936"
# language_code = "en-US"

# # Initialize the Dialogflow client
# session_client = dialogflow.SessionsClient()
# session = session_client.session_path(project_id, session_id)

# # Function to send a query to Dialogflow and get the response
# def detect_intent(text):
#     text_input = dialogflow.TextInput(text=text, language_code=language_code)
#     query_input = dialogflow.QueryInput(text=text_input)
#     response = session_client.detect_intent(request={"session": session, "query_input": query_input})

#     # Check if Dialogflow provided a response
#     if response.query_result.query_text:
#         return response.query_result.fulfillment_text
#     else:
#         return "I'm sorry, I couldn't understand your query."

# # Function to handle the phone call
# def handle_call():
#     # Twilio Account SID and Auth Token
#     account_sid = "AC4cc5b473630fa06d6b8f864f9c743582"
#     auth_token = "74998b5f06388dc6f7e8af97ff4d0935"

#     # Create a Twilio client
#     client = Client(account_sid, auth_token)

#     # Phone number to call
#     to_phone_number = ["+919025614379"]
#     from_phone_number = "+19802245395"
#     # Create a TwiML response
#     voice_response = VoiceResponse()

#     print("Making a phone call...")

#     # Add initial message
#     voice_response.say("Hi,how can I assist you today?")
#     gather = Gather(input="speech", action="/process_input")
#     gather.say("Please speak your query.")
#     voice_response.append(gather)

#     # Make the call
#     call = client.calls.create(
#         to=to_phone_number,
#         from_=from_phone_number,  # Replace with your Twilio phone number
#         twiml=str(voice_response),
#         record=True
#     )

# # Main entry point for the phone call
# if __name__ == "__main__":
#     handle_call()

from twilio.twiml.voice_response import Gather, VoiceResponse, Play, Pause
from twilio.rest import Client

account_sid = "ACe441fcdf90078f4922d9dc517868eaf8"
auth_token = "acc2c18427983146e98c3bc81d493898"

client = Client(account_sid, auth_token)

to_phone_number = ["+919025614379"]


question_audio_urls = [
    'https://app.resemble.ai/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCSzYzWWcwPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--61561f4f54dd7d4838c9ebc27c457e021ba3bc03/6077e97e-b90f-4037-b231-13cd7b42bcf3.wav',
    'https://app.resemble.ai/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCRUd6WWcwPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--3173892ccf63f3c10e642f4e52ae9e0b6bfeaf99/760b69ee-f81b-43e1-9799-2543504f48ad.wav',
    'https://app.resemble.ai/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCTXJRWWcwPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--94fdc210a1521b00fce832de78cd8de1872a6675/fbbfb766-eb05-4dae-84f5-d4e94c3d6490.wav',
    'https://app.resemble.ai/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCTVMxWWcwPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--a466dc542b078643616d0964ba4824f36de1b0f2/25da4369-fcff-46f7-b956-d56a539e23d2.wav',
    'https://app.resemble.ai/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCQ2kyWWcwPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--40b09c816df56be07068bdbcd78e803d127886c2/9dd45949-ec0b-4240-88ef-ea559e72f441.wav'
]


from_phone_number = "+17657393614"

def play_question(audio_url, voice_response):
    voice_response.append(Play(audio_url))
    voice_response.append(Pause(length=5)) 

voice_response = VoiceResponse()
voice_response.append(Pause(length=5))
for audio_url in question_audio_urls:
    play_question(audio_url, voice_response)

call = client.calls.create(
    to=to_phone_number,
    from_=from_phone_number,
    twiml=str(voice_response),
    record=True,
)

print(f"Calling {to_phone_number}...")

#---------------------------------------------------------------------------------------------

# from google.cloud import dialogflow
# import os

# # Set your Google Cloud service account key file path
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "adept-might-372205-48291665e5a9.json"

# # Initialize the Dialogflow client
# session_client = dialogflow.SessionsClient()
# project_id = "adept-might-372205"
# session_id = "116479968643497663936"
# session = session_client.session_path(project_id, session_id)

# # Function to send a query to Dialogflow and get the response
# def detect_intent(text):
#     language_code = "en-US"
#     text_input = dialogflow.TextInput(text=text, language_code=language_code)
#     query_input = dialogflow.QueryInput(text=text_input)
#     response = session_client.detect_intent(request={"session": session, "query_input": query_input})

#     # Check if Dialogflow provided a response
#     if response.query_result.query_text:
#         return response.query_result.fulfillment_text
#     else:
#         return "I'm sorry, I couldn't understand your query."

# # Create a new intent
# def create_intent():
#     intents_client = dialogflow.IntentsClient()
#     parent = f"projects/{project_id}/agent"

#     # Define the intent parameters
#     display_name = "GetWeather"
#     training_phrases = ["What's the weather today?", "Tell me the weather forecast"]
#     message_texts = ["The weather today in {location} is {weather_condition}"]

#     intent = dialogflow.Intent(
#         display_name=display_name,
#         training_phrases=[dialogflow.Intent.TrainingPhrase(parts=[dialogflow.Intent.TrainingPhrase.Part(text=phrase)]) for phrase in training_phrases],
#         messages=[dialogflow.Intent.Message(text=dialogflow.Intent.Message.Text(text=message)) for message in message_texts],
#     )

#     # Create the intent
#     intents_client.create_intent(request={"parent": parent, "intent": intent})

# # Main function
# if __name__ == "__main__":
#     print("Creating a Dialogflow agent and intent...")
    
#     # Create the intent
#     create_intent()
    
#     print("Agent and intent created successfully!")

#     while True:
#         user_input = input("User: ").strip()
#         response = detect_intent(user_input)
#         print("AI:", response)

