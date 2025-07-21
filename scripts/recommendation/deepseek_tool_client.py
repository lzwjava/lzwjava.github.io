import os
import requests
import json
from types import SimpleNamespace

MODEL_NAME = "deepseek-chat"

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"

def parse_to_namespace(data):
    if isinstance(data, dict):
        return SimpleNamespace(**{k: parse_to_namespace(v) for k, v in data.items()})
    elif isinstance(data, list):
        return [parse_to_namespace(item) for item in data]
    else:
        return data

def call_deepseek_api(messages, tools=None):
    if not DEEPSEEK_API_KEY:
        print("Error: DEEPSEEK_API_KEY is not set in .env file.")
        return None
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
        }
        data = {
            "model": MODEL_NAME,
            "messages": messages,
            "stream": False
        }
        if tools:
            data["tools"] = tools
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)        
        response.raise_for_status()
        response_json = response.json()
        if not response_json or not response_json.get('choices') or not response_json['choices'][0].get('message'):
            print(f"  Error: Response is empty or invalid:")
            print(response.content)
            return None
        choice = response_json['choices'][0]
        if choice.get('finish_reason') not in ("stop", "length", "tool_calls"):
            print(f"  Error: Did not finish with 'stop', 'length', or 'tool_calls' reason:")
            print(response.content)
            return None
        print('API call successful')
        # Parse to SimpleNamespace for dot access
        message = parse_to_namespace(choice['message'])
        return message
    except requests.exceptions.RequestException as e:
        print(f"  API call failed with error: {e}")       
        return None
    

if __name__ == "__main__":
    messages = [{"role": "user", "content": "hi"}]
    print(call_deepseek_api(messages=messages))