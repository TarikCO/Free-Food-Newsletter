# pip install openai
# pip install python-dotenv
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

respond = openai.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."}, 
    {"role": "user", "content": "What is the meaning of the  word 'happy'?"} 
  ]
)

print(respond.choices[0].message.content)
