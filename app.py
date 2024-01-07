import gradio as gr

def greet(input_video):
    print("Hola")
    #video_origen = input_video.value
    #print(video_origen)
    # Guardar el video en un archivo
    #video_origen.save("video_guardado.mp4")
    consola.value = "Hola mundo"
    consola.update()
    return input_video

#iface = gr.Interface(greet, gr.Video(height=200, width=200), "video")
#gr.show()

with gr.Blocks() as demo:
    with gr.Row():
        input = gr.Textbox()
        output = gr.Textbox()
    btn = gr.Button("Run")
    btn.click(greet, input, output)
    consola = gr.Textbox()

demo.launch()