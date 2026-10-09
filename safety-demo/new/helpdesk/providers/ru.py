"""Russian-hosted providers — Sber GigaChat and YandexGPT (native SDKs, plus a
raw HTTP call to the Yandex LLM endpoint). Detected natively since v1.9.1 —
each triggers data_egress(RU) and the non-allied data-sovereignty flag, the
same treatment as the CN providers in chinese_models.py. Inert demo code:
nothing here is called, no credentials exist."""
import gigachat                        # Sber GigaChat — native SDK
import yandex_cloud_ml_sdk             # YandexGPT — official Yandex Cloud ML SDK
import requests

def call_gigachat(prompt):
    client = gigachat.GigaChat(credentials="demo-placeholder")
    return client.chat(prompt)

def call_yandexgpt(prompt):
    sdk = yandex_cloud_ml_sdk.YCloudML(folder_id="demo")
    return sdk.models.completions("yandexgpt").run(prompt)

def call_yandex_raw(prompt):
    # Raw HTTP, no SDK — caught by known-endpoint detection.
    return requests.post("https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
                         json={"modelUri": "gpt://demo/yandexgpt", "messages": [prompt]})
