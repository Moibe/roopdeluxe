import gradio as gr

def greet(input_video):
    print("Hola")
    #video_origen = input_video.value
    #print(video_origen)
    # Guardar el video en un archivo
    #video_origen.save("video_guardado.mp4")
    return input_video

iface = gr.Interface(greet, gr.Video(height=200, width=200), "video")
gr.show()
iface.launch()