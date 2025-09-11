


import africastalking
import os


from dotenv import load_dotenv

load_dotenv()



def welcome_message(first_name, phone_number, site_id):

    recipients = [f"+254{str(phone_number)}"]

    print(recipients)
    print(phone_number)

    # Set your message
    message = f"Greetings {first_name}, welcome to our site. Lets build together. Remember to stay safe. Incase of emergency call 07xxxxxxx \nSite ID: {site_id}";

    # Set your shortCode or senderId
    sender = 20880

    try:
        response = sms.send(message, recipients, sender)

        print(response)

    except Exception as e:
        print(f'Houston, we have a problem: {e}')

    st.toast(f"Account Created Successfully")