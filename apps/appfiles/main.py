import openai, os, sys, time, g4f
sys.path.append("..")  # make sure we can run this from the repo
from IPython.display import Markdown, clear_output, display
from ipywidgets import widgets
from cohere import *


IP_ADDRESS = '127.0.0.1'
PORT_NUMBER = 8080
CHAT_MODEL = 'converse-xlarge-nightly'
# os.environ['x_ENDPOINT'] = 'https://
os.environ['COHERE_API_KEY'] = 'elh2OMjrml24I8dzSm5r2fTXvV61SU3lEHLU9Qpt'
api_key = os.environ.get('COHERE_API_KEY')
co = Client(api_key)
# endpoint = os.environ.get('LANGCHAIN_ENDPOINT')
print(f"API Key: {api_key}")
# print(f"endpoint: {endpoint}")
# query = input("What do you want to ask? ")



def g4effer():    # GPT4 API
    response = g4f.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": query}],
      stream=True,
    )	
    for message in response:
        print(message, flush=True, end='')
    # print(response)


def coh():
        co.generate("What is 8 mile about?", max_tokens=200)
        res = co.generate(prompt="Hey! How are you doing today?")
        print(res.text)


"""
def opeais(): # GPT3.5-TURBO API
  openai_api_key = os.getenv("OPENAI_API_KEY")
  openai_api_host = os.getenv("OPENAI_API_HOST")
  response = requests.post(
        f"{openai_api_host}/v1/engines/davinci/completions",
        headers={"Authorization": f"Bearer {openai_api_key}"},
        json={"prompt": text},
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return None
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
    response = get_response(query)
    print(response)
"""


def main():    # Sets cohere and oogabooga API
    coh()

    
if __name__ == "__main__":
    main()


"""
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'
"""    
"""
{
    "id": "chatcmpl-abc123",
    "object": "chat.completion",
    "created": 1677858242,
    "model": "gpt-3.5-turbo-0613",
    "usage": {
        "prompt_tokens": 13,
        "completion_tokens": 7,
        "total_tokens": 20
    },
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "\n\nThis is a test!"
            },
            "finish_reason": "stop",
            "index": 0
        }
    ]
}
"""
