import requests  
import os  
  
# Get the API key from environment variable or replace with your key  
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  
  
def call_openrouter_api(prompt, model="moonshotai/kimi-k2:free"):  
    url = "https://openrouter.ai/api/v1/chat/completions"  
    headers = {  
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",  
        "Content-Type": "application/json"  
    }  
    data = {  
        "model": model,  
        "messages": [  
            {"role": "user", "content": prompt}  
        ]  
    }  
    try:  
        response = requests.post(url, headers=headers, json=data)  
        if response.status_code == 200:  
            return response.json()['choices'][0]['message']['content']  
        else:  
            raise Exception(f"Error: {response.status_code} - {response.text}")  
    except Exception as e:  
        raise Exception(f"An error occurred: {str(e)}")  
  
if __name__ == "__main__":  
    # Example usage  
    result = call_openrouter_api("Hello, can you help me with a simple query?", "moonshotai/kimi-k2:free")  
    print("Response from OpenRouter:")  
    print(result)  
