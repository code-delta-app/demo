"""The dangerous case — a 'rogue agent'. It asks a model for code and then
EXECUTES whatever the model returns. Agent Scan should rate this CRITICAL /
HIGH: the rogue pattern (exec/eval next to an AI call) is the headline risk."""
import openai

def run_generated_code(task: str):
    client = openai.OpenAI()
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Write Python to: {task}"}],
    )
    code = resp.choices[0].message.content
    # DANGER: executing model output directly, unreviewed.
    exec(code)

def eval_model_answer(prompt: str):
    import anthropic
    client = anthropic.Anthropic()
    answer = client.messages.create(model="claude-opus-4-8", max_tokens=256,
                                    messages=[{"role": "user", "content": prompt}])
    # DANGER: eval on model output.
    return eval(answer.content[0].text)
