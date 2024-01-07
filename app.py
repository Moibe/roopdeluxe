import gradio as gr

def greet(input1, input2):
    print("Imprimiendo en Consola")
    print("Ésto es input1: ", input1)
    print("Ésto es input2: ", input2)
    return input1

#def carga_consola():
#    return "Hola Mundo"

#iface = gr.Interface(greet, gr.Video(height=200, width=200), "video")
#gr.show()

# with gr.Blocks() as demo:
#     print("Imprimiendo en Arranque...")
#     with gr.Row():
#         input1 = gr.Image()
#         input2 = gr.Image()
#         output = gr.Image()
#     btn = gr.Button("Run")
#     btn.click(greet, inputs=[gr.Image(), gr.Image()], outputs="image")

demo = gr.Interface(
fn=greet, inputs=[gr.Video(), gr.Video()], outputs="video"
)

demo.launch()