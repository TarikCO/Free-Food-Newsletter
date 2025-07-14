import requests  
import os  
from dotenv import load_dotenv 


load_dotenv()

api_key = os.getenv("PERPLEXITY_API_KEY")
base_url = "https://api.perplexity.ai/chat/completions"  # API endpoint URL

headers = {
    "Authorization": f"Bearer {api_key}",  
    "Content-Type": "application/json" 
}


user_question = "Tell me about Perplexity AI."


data = {
    "model": "llama-3.1-sonar-small-128k-online",
    "messages": [
        {"role": "user", "content": user_question}
    ]
}

response = requests.post(base_url, headers=headers, json=data)

if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"])
else:
    print(f"Error: {response.status_code} - {response.text}")
