import gradio as gr
from PIL import Image
import time
import os

#Greet es una función de ejemplo para usar.
def greet(input1, input2):
    print("Imprimiendo en Consola")
    print("Ésto es el input1 al día de hoy: ", input1)
    print("Ésto es el input2 al día de hoy: ", input2)

    #Aquí voy a poner como lo maneja roop en hf.
    #https://huggingface.co/spaces/ezioruan/roop/blob/main/app.py

    #Ésta es la forma correcta de guardar imagenes. 
    #Para los videos es directo. 
    #Y al parecer PIL ya lo tiene instalado.

    source_path = "input.jpg"
    target_path = "target.jpg"

    source_image = Image.fromarray(input1)
    print("Esto es source_image: ", source_image)
    source_image.save(source_path)
    target_image = Image.fromarray(input2)
    print("Esto es target_image: ", target_image)
    target_image.save(target_path)

    print("source_path: ", source_path)
    print("target_path: ", target_path)

    command = "python hola.py -t" + source_path
    print(command)
    time.sleep(1)
    proc = os.popen(command)
    output = proc.read()

    print(output)


    return input2

#Así para imagenes
demo = gr.Interface(
fn=greet, inputs=[gr.Image(), gr.Image()], outputs="image"
)

#Así para video
# demo = gr.Interface(
# fn=greet, inputs=[gr.Video(), gr.Video()], outputs="video"
# )

demo.launch()