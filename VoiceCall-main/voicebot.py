from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from http.server import BaseHTTPRequestHandler, HTTPServer

# Your Twilio Account SID and Auth Token
account_sid = 'AC4cc5b473630fa06d6b8f864f9c743582'
auth_token = '74998b5f06388dc6f7e8af97ff4d0935'

# Create a Twilio client
client = Client(account_sid, auth_token)

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/voice':
            self.handle_voice_request()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_voice_request(self):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length).decode('utf-8')
        
        response = VoiceResponse()
        response.say("Hello! This is your Voicebot speaking. How can I assist you today?")
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/xml')
        self.end_headers()
        self.wfile.write(str(response).encode('utf-8'))

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Listening on port 5000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
