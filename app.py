import gradio as gr

def greet(name):
    return "OK"

iface = gr.Interface(fn=greet, inputs="video", outputs="video")
iface.launch()