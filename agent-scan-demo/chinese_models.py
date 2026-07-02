"""Non-Western providers — DeepSeek, Alibaba Qwen (dashscope), Zhipu GLM,
Moonshot Kimi, Baidu ERNIE (qianfan).

NOTE: as of v1.8.2 several of these native SDKs are NOT YET in Agent Scan's
recognised list — this file is the gap demo. The exceptions: providers that
expose an OpenAI-compatible endpoint and are used via the `openai` SDK (with a
custom base_url) ARE already caught, because the openai import is detected."""
import dashscope                      # Alibaba Qwen / Tongyi — native SDK
import zhipuai                        # Zhipu GLM — native SDK
from openai import OpenAI             # ← THIS import IS detected today

def call_qwen(prompt):
    return dashscope.Generation.call(model="qwen-max", prompt=prompt)

def call_glm(prompt):
    client = zhipuai.ZhipuAI()
    return client.chat.completions.create(model="glm-4", messages=[{"role": "user", "content": prompt}])

def call_deepseek(prompt):
    # DeepSeek via its OpenAI-compatible endpoint — detected via the openai import.
    client = OpenAI(base_url="https://api.deepseek.com", api_key="...")
    return client.chat.completions.create(model="deepseek-chat",
                                          messages=[{"role": "user", "content": prompt}])
