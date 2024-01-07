import gradio as gr

def greet(input_video):
    print("Imprimiendo en Consola")
    print("Ésto es input_video: ", input_video)
    return input_video

#def carga_consola():
#    return "Hola Mundo"

#iface = gr.Interface(greet, gr.Video(height=200, width=200), "video")
#gr.show()

with gr.Blocks() as demo:
    print("Imprimiendo en Arranque...")
    with gr.Row():
        input1 = gr.Video()
        output = gr.Video()
    btn = gr.Button("Run")
    btn.click(greet, input1, output)

    #consola = gr.Textbox()
    #demo.load(carga_consola, None, consola)

#demo.queue().launch()
demo.launch()