import requests
import json

def query(payload, model_id, api_token):
    headers = {"Authorization": f"Bearer {api_token}"}
    API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def connect_api(text):

    # Replace with the sentiment analysis model ID ------------------------------------


    model_id = "microsoft/DialoGPT-large"



    # API Token Security
    with open('token.json') as f:
        data = json.load(f)
    
    api_token = data["ai"]




    payload = {"inputs": text}
    response = query(payload, model_id, api_token)

    result = response['generated_text']

    return result

# input_text = "hello there"
# temp = connect_api(input_text)
# result = temp['generated_text']
# print(result)
