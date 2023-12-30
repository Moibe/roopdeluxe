import gradio as gr

def greet(input_image):
    return input_image

iface = gr.Interface(greet, gr.Image(height=200, width=200), "image")
iface.launch()