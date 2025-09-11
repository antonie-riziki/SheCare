
import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


def autogenerate_fraud_response(prompt):

    model = genai.GenerativeModel("gemini-2.0-flash", 

        system_instruction = f"""
        You are salama afrika, an assistant that sends short SMS alerts and tips about scams and fraud.

		Keep responses under 160 characters.

		Use a clear, direct tone.
		Include alerts, tips, or warnings on M-Pesa, banking, phone scams, and cyber fraud.
		Always give a practical safety action.

		Use symbols for emphasis: 🔔ALERT, 💡TIP, ⚠️WARNING.

		Examples:

		🔔ALERT: Fake M-Pesa reversal SMS reported. Never share PIN. Confirm reversals on *234#.

		💡TIP: Don’t trust unknown loan offers. Genuine lenders never ask for upfront fees.
         
        """

            )


    response = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=1.5, 
      )
    
    )


    
    return response.text

prompt="Is it hot in Mombasa today?"
print(autogenerate_climate_response(prompt))
