import argparse
from roop import core

parser = argparse.ArgumentParser()
# ... añade los argumentos como se describió anteriormente

args = parser.parse_args(['-s', D:/Esyle-Prod/fotos/irina.jpg,
                          '-t', D:/Briefcase/wow.jpg,
                          '-o', D:/Esyle-Prod/resultados/irina-wow.jpg,
                          '--frame-processor', 'face_swapper'])

core.run(args)
