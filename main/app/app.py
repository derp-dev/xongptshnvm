import chainlit as cl
import requests, openai, os
from dotenv import load_dotenv

@cl.on_message
async def main(message: str):
    # Your custom logic goes here...

    def local_chat_completion(model, messages):
        return openai.ChatCompletion.create(model=model, messages=messages)

    def run_chat_completion():
        openai.api_key = "<YOUR_API_KEY>"
        chat_completion = local_chat_completion(model="orca-mini-7b.ggmlv3.q4_0.bin", messages=[{"role": "user", "content": "Hello world"}])
        print(chat_completion.choices[0].message.content)

    def run_api_request():
        url = "http://localhost:8080/v1/completions"
        rapidapi = os.getenv("rapidapi_key")
        prompt = ["Write a python program which provides the dot product of its arguments using only os and sys no imports"]
        headers = {
            "Content-Type": "application/json",
            # "Authorization": "Bearer " + rapidapi,
            # "My-Test-Header": "Testing!",
        }
        data = {
            "model": "orca-mini-7b.ggmlv3.q4_0.bin",
            "prompt": prompt,
            "temperature": 0.2
        }
        response = requests.post(url, headers=headers, json=data)
        print(response.text)

    # Call the functions as needed
    run_chat_completion()
    run_api_request()

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message}",
    ).send()
