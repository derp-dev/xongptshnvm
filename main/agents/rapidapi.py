import requests, openai, os
from dotenv import load_dotenv

load_dotenv()  # Call the load_dotenv function to load environment variables from the .env file
url = "http://localhost:8080/v1/completions"  # Replace with the URL of your dockerized application: LocalAI
rapidapi = os.getenv("rapidapi_key")  # Access the rapidapi_key environment variable using os.getenv()
prompt = ["Write a python program which provides the dot product of its arguments using only os and sys no imports"]
headers = {
    "Content-Type": "application/json",
#    "Authorization": "Bearer " + rapidapi,
#    "My-Test-Header": "Testing!",
}
data = {
    "model": "orca-mini-7b.ggmlv3.q4_0.bin",
    "prompt": prompt,
    "temperature": 0.2
}
response = requests.post(url, headers=headers, json=data)
print(response.text)

# payload = "{\"my-body-key\": \"my-body-value\"}\"}"
# querystring = {"":"myQueryValue"}
# response = requests.request("POST", url, data=payload, headers=headers, params=querystring, model="orca-mini-7b.ggmlv3.q4_0.bin")
# print(response.text)
# def local_chat_completion(model, messages):
    # Replace with local API call
#    return openai.ChatCompletion.create(model=model, messages=messages)
# chat_completion = local_chat_completion(model="orca-mini-7b.ggmlv3.q4_0.bin", messages=[{"role": "user", "content": "Hello world"}])
# print(chat_completion.choices[0].message.content)
