import os
from huggingface_hub import InferenceClient


model = "meta-llama/Llama-3.1-8B-Instruct"
# model = "mistralai/Mistral-7B-Instruct-v0.3"
model = "meta-llama/Meta-Llama-3-8B-Instruct"
def invoke_llm(prompt, model):
    messages = [{"role": "user", "content": prompt}]
    client = InferenceClient(model, api_key=os.environ["HF_API_KEY"])
    output = client.chat.completions.create(messages)
    return output.choices[0].message.content