import json
import requests


class mod1:
    def __init__(self):
        self.prompt = None
        self.parameters = {}
        self.api_endpoint = "https://localhost:8080"

    def set_prompt(self, prompt):
        self.prompt = prompt

    def set_parameters(self, parameters):
        self.parameters = parameters

    def generate_prompt(self):
        # Combine prompt and parameters
        complete_prompt = f"The way to {self.parameters['verb']} a {self.parameters['noun']} is through {self.parameters['mod1']} data structures. "
        complete_prompt += self.prompt

        return complete_prompt

    def execute_prompt(self):
        # Generate prompt and send request to AGENT.x API
        prompt = self.generate_prompt()
        response = requests.post(self.api_endpoint, json={"prompt": prompt})

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to execute prompt."}


# Usage example
agent = mod1()
agent.set_prompt("Instantiate variables {{mod1}}, {{verb}}, {{noun}} and print them to the console.") 
agent.set_parameters({
    "mod1": "most effective",
    "verb": "utilize",
    "noun": "prompt"
})

response = agent.execute_prompt()
print(json.dumps(response, indent=4))


def clean_chat(text):
    cleaned_text = []
    for line in text.split("\n"):
        line = requests.sub(r'\W+', ' ', line).strip()
        if len(line) > 0:
            cleaned_text.append(line)
    return "\n".join(cleaned_text)
