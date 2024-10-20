import openai
import gradio as gr
import os

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("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")

messages = [{"role": "system", "content": "You are a personal assistant for working professionals."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gr.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Joyful PA")
demo.launch()
