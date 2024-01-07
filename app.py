import gradio as gr

def greet(input_video):
    print("Imprimiendo en Consola")
    return input_video

#def carga_consola():
#    return "Hola Mundo"

#iface = gr.Interface(greet, gr.Video(height=200, width=200), "video")
#gr.show()

with gr.Blocks() as demo:
    print("Imprimiendo en Arranque...")
    with gr.Row():
        input = gr.Video()
        output = gr.Video()
    btn = gr.Button("Run")
    btn.click(greet, input, output)

    #consola = gr.Textbox()
    #demo.load(carga_consola, None, consola)

demo.launch()