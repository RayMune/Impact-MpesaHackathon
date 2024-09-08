from flask import Flask, request

app = Flask(__name__)

# Temporary storage for user data
user_data = {}

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route("/ussd", methods=['POST'])
def ussd():
    # Read the variables sent via POST from our API
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "")

    print("phone number", phone_number)
    print("text", text)

    if text == '':
        # First menu: Welcome and options
        response = "CON Welcome to Eco Ventures, your one-stop Green Marketplace \n"
        response += "1. Browse Products \n"
        response += "2. Check Reward Balance \n"
        response += "3. Redeem Green Tokens \n"
        response += "4. Contact Support \n"

    elif text == '1':
        # Category selection
        response = "CON Choose a product category: \n"
        response += "1. Recycled Products \n"
        response += "2. Biodegradable Products \n"
        response += "3. Organic Products \n"

    elif text == '1*1':
        # Recycled Products with more options
        response = "CON Recycled Products: \n"
        response += "1. Reusable Shopping Bag - KES 1000 \n"
        response += "2. Recycled Notebook - KES 300 \n"
        response += "3. Recycled Plastic Bottle - KES 200 \n"
        response += "4. Recycled Paper Pen - KES 150 \n"
        response += "5. Back to Main Menu \n"

    elif text == '1*2':
        # Biodegradable Products with more options
        response = "CON Biodegradable Products: \n"
        response += "1. Bamboo Toothbrush - KES 500 \n"
        response += "2. Biodegradable Plates - KES 600 \n"
        response += "3. Biodegradable Cutlery - KES 300 \n"
        response += "4. Compostable Straw - KES 200 \n"
        response += "5. Back to Main Menu \n"

    elif text == '1*3':
        # Organic Products with more options
        response = "CON Organic Products: \n"
        response += "1. Organic Cotton Shirt - KES 1500 \n"
        response += "2. Organic Coffee Beans - KES 1200 \n"
        response += "3. Organic Soap - KES 400 \n"
        response += "4. Organic Cotton Towel - KES 900 \n"
        response += "5. Back to Main Menu \n"

    elif text == '1*1*1' or text == '1*2*1' or text == '1*3*1':
        # Payment method selection and confirmation
        response = "END Awaiting STK push. Please check your phone for payment instructions."

    elif text == '2':
        # Check Reward Balance
        response = "END Your reward balance is 700 Green Tokens, worth 70 Ksh ."

    elif text == '3':
        # Redeem Green Tokens
        response = "CON Enter the number of Green Tokens to redeem:"

    elif text == '3*':
        # After token redemption input
        response = "END You have successfully redeemed your tokens. Check M-Pesa for cashback."

    elif text == '4':
        # Contact Support
        response = "END Please contact support at +254712345678 for any inquiries."

    else:
        # Default fallback response
        response = "END Invalid input, please try again."

    # Print the response to the console for debugging
    print(response)

    # Return the response to the API
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
