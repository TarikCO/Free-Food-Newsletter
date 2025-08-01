import os

from dotenv import load_dotenv  

load_dotenv()
import openai

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

with open("eventcredential.txt", "r") as file:
    event_content = file.read()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Write a short overview of each event, don't forget to include event name, time and place {event_content}",
        }
    ],
    model="llama3-8b-8192",
)
summary = chat_completion.choices[0].message.content
with open("summary.txt", "w") as summary_file:
    summary_file.write(summary)