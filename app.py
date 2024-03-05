import gradio as gr
from PIL import Image
import time
import os
import pathlib
import zipfile36 as zipfile

def save_images_as_zip(path_foto, filename, plataforma):

    with zipfile.ZipFile(filename, "w") as zip_file:
        for foto in os.listdir(path_foto):
            print("La foto en os.listdir es: ", foto)
            #Si Local
            # path_foto_zippable = str(path_foto) + "\\" + foto
            # #Si HuggingFace
            # path_foto_zippable = str(path_foto) + "/" + foto
            path_foto_zippable = str(path_foto) + (os.sep if plataforma == "local" else "/") + foto
            print("La ruta textual final de esa foto en particular es: ", path_foto_zippable)
            # ruta = pathlib.Path(path_foto_zippable)
            # zip_file.write(ruta)
            ruta = os.path.basename(path_foto_zippable)
            zip_file.write(path_foto_zippable, ruta)

def perform(input1, input2, input3):

    #video o cualquier otro sería para imagenes.
    modo = "pic"
    #local o huggingface
    plataforma = "huggingface"

    #face_swapper o face_enhancer o la combinación de ellos.
    #El default, por si el usuario no eligiera nada, es:
    procesador = "face_swapper"
    print("Por ahora el procesador es:", procesador)

    print("Esto fue el input 3 recibido...:", input3)
    time.sleep(3)

    longitud = len(input3)

    if longitud == 2:
        procesador = "face_swapper face_enhancer"
    elif longitud == 0:
        print("La longitud si da 0")        
    else:
        procesador = input3[0]

    print("El procesador seleccionado terminó siendo...", procesador)
    
    print("Inicio: Estamos en modo ", modo)
    print("Estamos en la plataforma:", plataforma)
    print("El procesador es: ", procesador)

    path_video = input2

    if plataforma == "local":
        #Para local.
        path_parts = path_video.split("\\")
    else:
        #Para HuggingFace
        print("La plataforma en la que basaremos la división es HuggingFace.")
        path_parts = path_video.split("/")

    #Aquí obtendremos nom_video
    filename = path_parts[-1]
    nom_video = filename[:-4]
    print("Esto es filename alias nom_video: ", nom_video)
    time.sleep(1)

    path_particular = "/".join(path_parts[0:len(path_parts) - 1])
    path_general = "/".join(path_parts[0:len(path_parts) - 2])
    
    path_general = path_general.replace("\\", "/")
    path_particular = path_particular.replace("\\", "/")

    print("Path general: ", path_general)
    print("Path general: ", path_particular)

    path = pathlib.Path("result.mp4")
    
    files = os.listdir(path_general)
    print("Estos son los files que hay:")
    print(files)

    ext_imagen = "png"
    ext_video = "mp4"

    #Selector de modo.
    if modo == "video": 
        print("Se asigno la extensión de video:", ext_video)
        extension = ext_video
    else:
        print("Se asigno la extensión de imagen:", ext_imagen)
        extension = ext_imagen

    #El source siempre es una imagen.
    source_path = "source.png"
    target_path = "target." + extension
    result_path = "result." + extension

    #La primera siempre será una imagen, por eso no entra en el modo selector.
    source_image = Image.fromarray(input1)
    print("Esto es source_image: ", source_image)
    source_image.save(source_path)
        
    #Aquí trabajaremos solo el target.
    if modo == "video":
        #Para Video
        target_path = input2
    else:
        #Es decir si es modo imagen
        #Para Imagenes
        target_image = Image.fromarray(input2)
        print("Esto es target_image: ", target_image)
        target_image.save(target_path)

    print("Después de los selectores de modo los paths quedaron así:")
    print("source_path: ", source_path)
    print("target_path: ", target_path)

    command = f"python run.py -s {source_path}  -t {target_path} -o {result_path} --frame-processor {procesador} --execution-provider cuda"
    print(command)
    time.sleep(1)
    proc = os.popen(command)
    output = proc.read()

    print("Output (resultado de la ejecución del código):")
    time.sleep(1)
    print(output)
    print("Terminó la impresión del output...")

    print("Éste es el momento en el que se creo result, revisar...")
    time.sleep(1)

    print("Ahora estamos imprimiendo las rutas para ver si apareció una nueva:")
    files = os.listdir(path_general)
    print("Estos son los files que hay:")
    print(files)

    #Creación de la galería:
    images = []
    
    #nom_video = "whitebeauty"
    path_foto = pathlib.Path(path_particular + "/temp/" + nom_video + "/")
    print("Éste es el path foto: ", path_foto)
    path_result = str(path_foto) + "/temp.mp4"
    print("Y éste es el path del resultado: ", path_result)
 
    #Éste es el segmento que crea la galería de imagenes, que por el momento no usaremos por rendimiento.
    #Se reintegrará si agregamos interacción de poder borrar cada imagen desde la interfaz web.
    
    # for filename in os.listdir(path_foto):
    #     if filename.endswith(".png"):
    #         path = os.path.join(path_foto, filename)
    #         image = Image.open(path)
    #         images.append(image)

    # print("Esto es la lista de imagenes: ", images)

    #nombre_zip = nom_video + ".zip"
    #print("El nombre del zip será: ", nombre_zip)

    try:
        #save_images_as_zip(path_foto, nombre_zip, plataforma)
        print("Ésta vez no crearemos archivo zip.")

    except Exception as e:
        # código que se ejecutará si se produce la excepción
        print(e)
    
    if modo == "video":
        #Para video
        path = pathlib.Path("result.mp4")
        path_abs = os.path.abspath(path)
        print("Éste es el path para video:", path)
        print("Y su ruta absoluta es: ", path_abs)
        #path_zip = pathlib.Path(nombre_zip)
        #path_zip_abs =  os.path.abspath(path_zip)
        #print("Y éste es el path para el zip: ", path_zip)
        #print("Y su ruta absoluta es: ", path_zip_abs)
        return path
    else:
        #Para imagen
        path = pathlib.Path("result.png")
        print("Éste es el path para imagen:", path)
        return path, images, images
    print("Listo! Gracias!")
     
#Así para imagenes
demo = gr.Interface(
fn=perform, inputs=[gr.Image(), gr.Image(), gr.CheckboxGroup(["face_swapper","face_enhancer"], label="Processor")], outputs=[gr.Image(), gr.Image()]
)

#Así para video y 3 outputs: Video, Galería y Archivo Zip.
# demo = gr.Interface(
# fn=perform, inputs=[gr.Image(), gr.Video()], outputs=[gr.Video(), gr.Gallery(), gr.File()]
# )

#Así para 2 outputs, video y zip.
# demo = gr.Interface(
# fn=greet, inputs=[gr.Image(), gr.Video()], outputs=[gr.Video(), gr.File()]
# )

#1 output: video.
# demo = gr.Interface(
# fn=perform, inputs=[gr.Image(), gr.Video(), gr.CheckboxGroup(["face_swapper","face_enhancer"], label="Processor")], outputs=[gr.Video()]
# )

demo.launch()