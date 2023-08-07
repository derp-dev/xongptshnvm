import os

cohere_api_key = os.getenv("COHERE_API_KEY")
localai_url = os.getenv("LOCALAI_URL")

def get_answer(query):
    # Make a POST request to the local AI server
    response = requests.post(localai_url, json={"query": query})
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()["answer"]
    else:
        return None

query = "hello world"
answer = get_answer(query)
print(answer)

