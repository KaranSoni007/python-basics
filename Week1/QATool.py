import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-lite")

question = input("Ask a question: ")

response = model.generate_content( f"Generate a answer for {question} in simple, short but understandable language")

print(response.text)