import os
import sys
from cohere import *
import IPython
from IPython.display import Markdown, clear_output
from ipywidgets import widgets


IP_ADDRESS = '127.0.0.1'
PORT_NUMBER = 8080
CHAT_MODEL = 'converse-xlarge-nightly'
os.environ['COHERE_API_KEY'] = 'elh2OMjrml24I8dzSm5r2fTXvV61SU3lEHLU9Qpt'
api_key = os.environ.get('COHERE_API_KEY')
co = Client(api_key)


text_input = widgets.Text()
text_display = widgets.Output()


def text_length():
    text = text_input.value
    length = len(text)
    text_display.clear_output()
    with text_display:
        IPython.display.display(f"The length of {text} is {length}.")


def coh():
    co.generate("What is 8 mile about?", max_tokens=200)
    res = co.generate(prompt="Hey! How are you doing today?")
    print(res.text)


def main(): 
    pass


if __name__ == "__main__":
    main()
