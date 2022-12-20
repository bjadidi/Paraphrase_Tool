import requests

endpoint = "https://api.openai.com/v1/models/{model}/completions"

parameters = {
    "prompt": "Hello, I would like to ask a question. What is the capital of France?",
    "model": "text-ada-001",
    "max_tokens": 1000,
    "temperature": 0,
    "api_key": "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"
}

response = requests.post(endpoint, json=parameters)
print(response)
if response.status_code == 200:
    generated_text = response.json()["text"]
    print(generated_text)