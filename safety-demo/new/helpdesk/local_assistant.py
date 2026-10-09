import os
import ollama

def act(messages):
    r = ollama.chat(model='llama3', messages=messages)
    os.system(r['message']['content'])
