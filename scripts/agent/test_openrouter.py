import requests  
import os  
  
# Get the API key from environment variable or replace with your key  
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  
  
def test_openrouter():  
    url = "https://openrouter.ai/api/v1/chat/completions"  
    headers = {  
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",  
        "Content-Type": "application/json"  
    }  
    data = {  
        "model": "moonshotai/kimi-k2:free",  # Updated model ID  
        "messages": [  
            {"role": "user", "content": "Hello, can you help me with a simple query?"}  
        ]  
    }  
    try:  
        response = requests.post(url, headers=headers, json=data)  
        if response.status_code == 200:  
            print("Response from OpenRouter:")  
            print(response.json()['choices'][0]['message']['content'])  
        else:  
            print(f"Error: {response.status_code}")  
            print(response.text)  
    except Exception as e:  
        print(f"An error occurred: {str(e)}")  
  
if __name__ == "__main__":  
    test_openrouter()  
