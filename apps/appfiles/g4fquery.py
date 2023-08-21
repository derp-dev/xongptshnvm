import g4f

def main():
    query = input("What do you want to ask? ")
    # response = get_response(query)
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}],
        stream=True,
    )	
    for message in response:
        print(message, flush=True, end='')
    print(response)        
        
if __name__ == "__main__":
    main()
"""
# normal response
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": "hi"}],
)  # alterative model setting

print(response)

print(g4f.provider.Ails.params)  # supported args

for message in response:
    print(message)
"""