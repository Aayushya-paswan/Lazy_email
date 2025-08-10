import ollama
client=ollama.Client()
model="llama3.2:1b"

def give_response(text):
    response_text = client.generate(model=model, prompt=str(text))
    return response_text['response']

print(give_response("Hello there"))

