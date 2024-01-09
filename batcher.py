import os
import time

#Ruta donde están las imagenes que quiero convertir.
pics_dir = "D:/Organizar/ZJB/Esyle/art"
#pics_dir = "D:/Esyle-Prod/videos/next"
pics_name = os.path.basename(pics_dir)
print(pics_name)
time.sleep(1)

#Crea un nuevo directorio dentro de resultados-pics que contendrá los resultados de éste batch.
resultados_dir = "D:/Esyle-Prod/resultados_pics/"
os.makedirs(os.path.join(resultados_dir, pics_name))

#Lista los archivos que convertiras.
pics = os.listdir(pics_dir)
print(pics)

#Calcula cuantos archivos son:
cuantos = len(pics)
print("Trabajaremos con: ", cuantos)



#Corre el proceso por cada archivo.
for pic in pics:
    print("Listo para correr el comando, nos faltan: ", cuantos)
    command = "python run.py -s D:/Esyle-Prod/fotos/irina.jpg -t " + pics_dir + "/" + pic + " -o " + resultados_dir + pics_name + "/irina-" + pic + " --frame-processor face_swapper"
    print(command)
    time.sleep(1)
    proc = os.popen(command)
    output = proc.read()
    cuantos -= 1 

    print(output)