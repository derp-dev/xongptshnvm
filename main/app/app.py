import chainlit as cl
import requests, openai, os
from dotenv import load_dotenv

@cl.on_message
async def main(message: str):
    """
    A decorator for a ChainLit base class that modifies function behavior without changing the code, similar to ABCs in Python.
    ChainLit runs an event loop in the background, monitoring for new messages. When a new message arrives, ChainLit checks for any functions decorated with @cl.on_message.
    The decorated function, such as main(), defines the message payload as its first parameter. The decorator populates this parameter with the payload when the function is called.
    Alternatively, the decorator can pass the full event as a dictionary using .event. You can access attributes like .event['message'], .event['type'], and more.
    You also have the option to wrap the function to extract specific arguments from the event dictionary.
    Given that the interaction with the user might involve asynchronous operations, the decorated function is often defined as an async function. This allows you to use await statements within the function to handle asynchronous tasks smoothly.
    """
    
    def local_chat_completion(model, messages):
        return openai.ChatCompletion.create(model=model, messages=messages)
        """
         local_chat_completion takes a model and messages as input and uses the openai library to create a chat completion. run_chat_completion sets the openai.api_key and calls local_chat_completion with some predefined parameters.
        """
    def run_chat_completion():
        openai.api_key = "<YOUR_API_KEY>"
        chat_completion = local_chat_completion(model="orca-mini-7b.ggmlv3.q4_0.bin", messages=[{"role": "user", "content": "Hello world"}])
        print(chat_completion.choices[0].message.content)

    def run_api_request():
        url = "http://localhost:8080/v1/completions"
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

    # Call the previously defined functions to execute the chat completion and API request
    run_chat_completion()
    run_api_request()

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message}",
    ).send()
