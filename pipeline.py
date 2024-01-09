from frameFixer import frameFixer 
from continuaVideo import hacerVideo
from restauraAudio import restauraAudio

#Después de terminar el video, corrige manualmente los frames que no van. Respeta la numeración. 
#Es decir solo tienes que borrar los que no quieres.

#El siguiente paso es arreglar los frames, con frameFixer.py Aquellos que borraste serán restaurados con el frame anterior. 
#Lo único a considerar es que siempre debe haber un frama 0001.png. 
#Idealmente se debería de mover o eliminar el archivo temp.mp4 si existe porque causará error al correr el archivo.
#Programar una excepción para el futuro, pero de todas formas si se corre frameFixer es porque se deea un nuevo temp.mp4.

video = 'Emily_Home_Test'

#En caso de que no haya habido remoción de frames puedes saltar el frameFixer.
frameFixer(video)

#Después de que lo arregla volverá a hacer el video: 
hacerVideo(video)

#Y por último restauramos el audio.
#Si será en un video que cortaste, el audio ya no coincidirá y si restauras audio quedará mal el video.
restauraAudio(video)
