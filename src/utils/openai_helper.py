from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def translate_prompt(prompt):
    client = OpenAI(
        api_key = os.getenv("OPENAI_API_KEY")
    )
    try:
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Please translate to chinese:{prompt}"}
            ]
        )
        return completion.choices[0].message.content
    
    except Exception as e:
        print(f"Error calling OpenAI API {e}")
        return "Sorry, something went wrong"
    