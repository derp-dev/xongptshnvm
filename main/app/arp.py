import chainlit as cl
import requests, openai, os, json


@cl.on_message
async def main(message: str):
    def local_chat_completion(model, messages):
        return openai.ChatCompletion.create(model=model, messages=messages)


def run_chat_completion():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    chat_completion = local_chat_completion(model="orca-mini-7b.ggmlv3.q4_0.bin", messages=[{"role": "user", "content": "Hello world"}])
    print(chat_completion.choices[0].message.content)


def run_api_request():
    url = "http://localhost:8080/v1/completions"
    prompt = ["Write a python program which provides the dot product of its arguments using only os and sys no imports"]
    headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + os.getenv("RAPIDAPI_KEY"),
    "My-Test-Header": "Testing!",
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


class RequestTemplate:
    def __init__(self, template):
    self.template = template

    def encode(self, context):
    encoded = self.template.format(**context)
    return encoded

class OpenAIPost:
    def __init__(self, template):
    self.template = template

    def generate(self, context):
    encoded = RequestTemplate(self.template).encode(context)

    url = "https://api.openai.com/v1/completions"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": encoded, "max_tokens": 100}

    response = requests.post(
        url=url, headers=headers, json=data
    )

    return response.text

template = "{{text}}"

request = OpenAIPost(template)
context = {"text": "Hello World"}

Return: request.generate(context)

