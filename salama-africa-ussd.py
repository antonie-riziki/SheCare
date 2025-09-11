import os
from flask import Flask, request

from dotenv import load_dotenv

sys.path.insert(1, '/autogenerate')

from autogenerate.ai_response import autogenerate_fraud_response

app = Flask(__name__)

@app.route("/ussd", methods = ['POST'])
def ussd():
  # Read the variables sent via POST from our API
  session_id   = request.values.get("sessionId", None)
  serviceCode  = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text         = request.values.get("text", "default")

  if text      == '':
      # This is the first request. Note how we start the response with CON
      response  = "CON Welcome to Salama Afrika, Inclusive Digital Protection for Everyone \n"
      response += "1. Verify Number / SMS \n"
      response += "2. Report Online Harassment \n"
      response += "3. Scam & Fraud Alerts \n"
      response += "4. Accessibility Options (PWDs) \n"
      response += "5. About Salama Afrika \n"

  elif text    == '1':
      # Business logic for first level response
      response  = "CON Enter phone number to check: \n"
      # response += "1. Phone number"

  elif text   == '2':
      response  = "CON Choose type of issue: \n"
      response += "1.  Unwanted messages/DMs \n"
      response += "2.  Bullying / Abuse (e.g. on X/Twitter) \n"
      response += "3.  Blackmail / NCII threat \n"
      response += "4.  Other \n"

  elif text    == '3':
      response = "CON Latest Scam Alerts: \n Learn how to protect yourself: \n"
      response += "1. Fake MPESA screenshots \n"
      response += "2. Loan Scam SMS \n"  
      response += "3. WhatsApp phishing groups \n" 

  elif text    == '4':
    response = "CON Latest Scam Alerts: \n Learn how to protect yourself:"
    response += "1. Accessibility Settings: \n"
    response += "2. High-contrast mode \n"  
    response += "3. Voice reporting (record your issue) \n" 
    response += "4. Language (Swahili / Local Language) \n"

  elif text    == '5':
    response = "END Salama Afrika protects you from scams, harassment & fraud. Anonymous & safe."

  else :
      response = "END Invalid choice"

  # Send the response back to the API
  return response

if __name__ == '__main__':
    app.run(debug=True, port="8000")