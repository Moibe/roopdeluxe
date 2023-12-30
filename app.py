import gradio as gr

def greet(input_image):
    return input_image

iface = gr.Interface(greet, gr.Video(height=200, width=200), "video")
iface.launch()