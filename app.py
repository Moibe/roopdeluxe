import gradio as gr

def greet(input_video):
    return input_video

iface = gr.Interface(greet, gr.Video(height=200, width=200), "video")
iface.launch()