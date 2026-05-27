import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")
topic = input("Enter topic: ")
# response = model.generate_content(f"Explain {topic} in very simple terms")
# response = model.generate_content(f"Tell me one fun fact about {topic}")
response = model.generate_content(f"Explain {topic} in simple and short language for beginners")
print(response.text)
