import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-lite")

topic = input("Enter email topic: ")
tone = input("Enter tone: ")

response = model.generate_content(f"Write an email about {topic} in a {tone} tone")

print(response.text)