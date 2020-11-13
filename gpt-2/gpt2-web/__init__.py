import requests

def gpt2_web(text, model):
    params = {
        'input_text': text,
        'model_name': model,
    }
    req = requests.get('https://f52e5e8bfa9f.ngrok.io/text-generate', params=params, timeout=500)
    return req.text
