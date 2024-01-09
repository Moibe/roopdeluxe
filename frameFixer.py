import os
import time
import shutil

#Convertir esto en una función general

# #Aquí empieza el proceso de crear el nombre del duplicador: 
#         # Convertimos la variable a string
#         archivo_faltante_str = str(archivo_faltante)
#         # Calculamos la longitud de la cadena
#         longitud = len(archivo_faltante_str)
#         # Si la longitud es menor que 4, completamos con ceros
#         if longitud < 4:
#             archivo_faltante_str = "0" * (4 - longitud) + archivo_faltante_str
#         # Agregamos el sufijo
#         archivo_faltante_str += ".png"

#Hacer el video variable: 

def frameFixer(video):

    
    #Ahora ya se recibe por parámetro.
    path = "D:/Esyle-Prod/videos/temp/" + video

    print("Ruta:", path)
    is_dir = os.path.isdir(path)

    if is_dir:
        print("La ruta apunta a un directorio")
    else:
        print("La ruta no apunta a un directorio")

    files = os.listdir(path)

    for file in files:
        print(file)

    # Inicializa un contador
    i = 1
    pendiente = "0001.png"

    dejar_de_checar = False

    # Recorre la lista de archivos
    for file in files:

        dejar_de_checar = False

        while dejar_de_checar is not True: 

            print("Checking row file number: ", file )
            #Empieza el procesamiento: 
            # Obtenemos el número sin la extensión
            nombre = file[:-4]

            print(nombre)
            numero = int(nombre)
            
            print("Y yo soy el contador i, es decir el archivo que debería seguir: ", i)
            print(f"Comparación de fila de archivo número: {numero} con contador número: {i}.")
            # Verifica si el número del archivo coincide con el contador
            if numero == i :
                print("Archivo y contador iguales - OK.")
                print("Siguiente archivo y siguiente contador...")
                dejar_de_checar = True
                i += 1
            else:
                # Si el número del archivo no coincide con el contador, significa que hay un número faltante
                print("Archivo y contador diferente:")
                print(f"Falta el archivo {i}.png.")            
                time.sleep(1)
                
                archivo_faltante = i
                #Aquí empieza el proceso de crear el nombre del duplicador: 
                # Convertimos la variable a string
                archivo_faltante_str = str(archivo_faltante)
                # Calculamos la longitud de la cadena
                longitud = len(archivo_faltante_str)
                # Si la longitud es menor que 4, completamos con ceros
                if longitud < 4:
                    archivo_faltante_str = "0" * (4 - longitud) + archivo_faltante_str
                # Agregamos el sufijo
                archivo_faltante_str += ".png"
                print("El archivo faltante, es decir el que queremos crear es:", archivo_faltante_str)
                archivo_duplicable = i - 1
                #Aquí empieza el proceso de crear el nombre del duplicador: 
                # Convertimos la variable a string
                archivo_duplicable_str = str(archivo_duplicable)
                # Calculamos la longitud de la cadena
                longitud = len(archivo_duplicable_str)
                # Si la longitud es menor que 4, completamos con ceros
                if longitud < 4:
                    archivo_duplicable_str = "0" * (4 - longitud) + archivo_duplicable_str
                # Agregamos el sufijo
                archivo_duplicable_str += ".png"

                print("El nombre del archivo a duplicar es!: ")
                print(archivo_duplicable_str)
                time.sleep(1)

                src = os.path.join(path, archivo_duplicable_str)
                print("Solo para corroborar, estamos creando el archivo:", archivo_faltante_str)
                dst = os.path.join(path, archivo_faltante_str)
                print("Copiando...")
                shutil.copy(src, dst)
                print("Copiado y corregido.")
                time.sleep(1)

                print("Ya quedó corregido, pero file se queda en pendiente pq aún debe encontrar a su par...")
                time.sleep(1)

                #Ahora las operaciones para dejar listo el contador para el siguiente set: 
                i += 1
                
                print("Después de hacer entrado al else, el contador ahora está en: ", i)
                print("Eso es correcto, pero file debe seguir en el mismo número también, es decir no debemos movernos al siguiente file.")
                time.sleep(1)

            print("Terminó el while, sigue el siguiente file.")
            time.sleep(1)