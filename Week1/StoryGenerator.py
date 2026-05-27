import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-lite")

topic = input("Enter topic : ")

tone = input("Enter tone : ")

response = model.generate_content(f"Write a short story about {topic} in a {tone} tone")

print(response.text)