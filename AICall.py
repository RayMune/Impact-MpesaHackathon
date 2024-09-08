from flask import Flask, request, jsonify
from twilio.twiml.voice_response import VoiceResponse
import openai
import os
import requests
import base64
from datetime import datetime

app = Flask(__name__)

# Set your OpenAI API key and Twilio credentials
openai.api_key = os.getenv('OPENAI_API_KEY')

# M-Pesa credentials (replace with your actual credentials)
MPESA_CONSUMER_KEY = os.getenv('MPESA_CONSUMER_KEY')
MPESA_CONSUMER_SECRET = os.getenv('MPESA_CONSUMER_SECRET')
MPESA_SHORTCODE = os.getenv('MPESA_SHORTCODE')  # Business Shortcode
MPESA_PASSKEY = os.getenv('MPESA_PASSKEY')
MPESA_ENV = "sandbox"  # Use "production" for live environment

# Safaricom OAuth URL (for access token)
MPESA_OAUTH_URL = f"https://{MPESA_ENV}.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

# Safaricom STK Push URL
MPESA_STK_PUSH_URL = f"https://{MPESA_ENV}.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

def get_mpesa_access_token():
    """Get the M-Pesa API access token."""
    try:
        response = requests.get(MPESA_OAUTH_URL, auth=(MPESA_CONSUMER_KEY, MPESA_CONSUMER_SECRET))
        json_response = response.json()
        return json_response['access_token']
    except Exception as e:
        print(f"Error fetching M-Pesa access token: {e}")
        return None

def initiate_stk_push(phone_number, amount):
    """Initiate an M-Pesa STK Push request."""
    access_token = get_mpesa_access_token()
    if not access_token:
        return "Failed to get access token."

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    password = base64.b64encode(f"{MPESA_SHORTCODE}{MPESA_PASSKEY}{timestamp}".encode()).decode('utf-8')

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "BusinessShortCode": MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://your-server-url/callback",  # Replace with your callback URL
        "AccountReference": "Eco Ventures",
        "TransactionDesc": "Payment for Eco-friendly product"
    }

    try:
        response = requests.post(MPESA_STK_PUSH_URL, json=payload, headers=headers)
        return response.json()
    except Exception as e:
        print(f"Error initiating M-Pesa STK Push: {e}")
        return "Failed to initiate STK Push."

@app.route("/voice", methods=['POST'])
def voice():
    """Handle inbound calls and respond using OpenAI."""
    transcription = request.form.get('SpeechResult', '').strip()

    if transcription:
        if "pay" in transcription.lower():  # Simple check for payment trigger
            # Example of initiating STK Push with a phone number and amount
            phone_number = request.form.get('From')  # Get the caller's phone number from Twilio
            stk_response = initiate_stk_push(phone_number, 500)  # Trigger payment of 500
            response_text = "We are sending an STK push to your phone for payment."
        else:
            response_text = get_openai_response(transcription)
    else:
        response_text = "I'm sorry, I didn't catch that. Can you repeat?"

    # Respond to the caller
    resp = VoiceResponse()
    resp.say(response_text)

    return str(resp)

def get_openai_response(prompt):
    """Get a response from OpenAI's GPT model based on the user's voice input."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return "There was an issue processing your request. Please try again later."

@app.route("/callback", methods=['POST'])
def mpesa_callback():
    """Handle the M-Pesa STK push callback."""
    callback_data = request.json
    print(f"Callback received: {callback_data}")
    # Process the callback data and handle payment success or failure
    return jsonify({"ResultCode": 0, "ResultDesc": "Success"})

if __name__ == "__main__":
    app.run(debug=True)
