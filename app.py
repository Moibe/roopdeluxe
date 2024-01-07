import gradio as gr

def greet(input_video):
    
    return input_video

def carga_consola():
    return "Hola Mundo"


#iface = gr.Interface(greet, gr.Video(height=200, width=200), "video")
#gr.show()

with gr.Blocks() as demo:
    with gr.Row():
        input = gr.Textbox()
        output = gr.Textbox()
    btn = gr.Button("Run")
    btn.click(greet, input, output)

    consola = gr.Textbox()
    demo.load(carga_consola, None, consola)

demo.queue().launch()