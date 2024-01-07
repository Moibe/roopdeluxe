import os
import time

#command = "python run.py -s D:/Esyle-Prod/fotos/irina.jpg  -t D:/Briefcase/wow.jpg -o D:/Esyle-Prod/resultados/irina-wow.jpg --frame-processor face_swapper"
command = "python hola.py"
print(command)
time.sleep(1)
proc = os.popen(command)
output = proc.read()

print(output)