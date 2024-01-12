import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-t', '--target_path', help='Ruta al archivo de destino')

args = parser.parse_args()

print("Esto es args: ", args)

print("Hola desde Hola.py")
print("El target path recibido es: ", args.target_path)
print("El target recibido es: ", args.target)
print("El target image recibido es: ", args.target_image)

#nueva_var = args.target_path