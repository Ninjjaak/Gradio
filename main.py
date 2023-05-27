#os is not needed but I imported incase for any changes
import os
import openai
import gradio as gr


openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Ask me a question! "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AutoGPT:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Janaka's ChatGPT Clone!</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True, share = True)
