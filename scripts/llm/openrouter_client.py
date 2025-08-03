import requests
import os

# Get the API key from environment variable or replace with your key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL_MAPPING = {
    "claude-opus": "anthropic/claude-opus-4",
    "claude-sonnet": "anthropic/claude-sonnet-4",
    "gemini-flash": "google/gemini-2.5-flash",
    "deepseek-v3": "deepseek/deepseek-chat-v3-0324:free",
    "gemini-pro": "google/gemini-2.5-pro",
    "kimi-k2": "moonshotai/kimi-k2:free",
    "mistral-nemo": "mistralai/mistral-nemo",
    "qwen-coder":"qwen/qwen3-coder:free"
}


def call_openrouter_api_with_messages(messages, model="mistral-nemo"):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    # Check if the model exists in the mapping
    if model not in MODEL_MAPPING:
        raise Exception(f"Model '{model}' not found in MODEL_MAPPING")

    data = {"model": MODEL_MAPPING[model], "messages": messages}
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")


def call_openrouter_api(prompt, model="mistral-nemo"):
    messages = [{"role": "user", "content": prompt}]
    return call_openrouter_api_with_messages(messages, model)


if __name__ == "__main__":
    # Example usage
    for model_name in MODEL_MAPPING.keys():
        try:
            result = call_openrouter_api(
                "Hello, 9.11 or 9.9, which one is bigger? ", model_name
            )
            print(f"Response from {model_name}:")
            print(result)
            print("-" * 50)
        except Exception as e:
            print(f"Error with {model_name}: {str(e)}")
            print("-" * 50)
