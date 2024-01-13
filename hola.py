import argparse

def func_hola():

    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--target_path', help='Ruta al archivo de destino')

    args = parser.parse_args()

    print("Esto es args: ", args)

    print("Hola desde Hola.py el día de hoy:")
    print("El target path recibido es: ", args.target_path)

    nueva_var = args.target_path
    print("La nueva var es: ", nueva_var)

    return nueva_var

if __name__ == "__main__":
    func_hola()