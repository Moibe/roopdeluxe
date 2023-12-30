import gradio as gr

def greet(name):
    return "OK"

iface = gr.Interface(fn=greet, gr.Image(height=200, width=200), "image")
iface.launch()