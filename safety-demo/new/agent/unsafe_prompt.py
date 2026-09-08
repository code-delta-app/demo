"""Prompt-injection exposure — untrusted user input is concatenated straight
into prompts with no sanitisation. Agent Scan should report injection vectors."""
import openai

def handle_user(user_input):
    client = openai.OpenAI()
    # User input flows straight into the prompt — classic injection surface.
    prompt = "You are a support bot. Answer this customer: " + user_input
    return client.chat.completions.create(
        model="gpt-4o", messages=[{"role": "user", "content": prompt}])

def chat_loop():
    while True:
        q = input("you: ")                       # untrusted
        msg = f"Reply helpfully to: {q}"          # unsanitised interpolation
        handle_user(msg)
