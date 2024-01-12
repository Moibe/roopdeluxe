from roop.utilities import restore_audio

def restauraAudio(video):

    #Antes tienes que ejecutar continuaVideo para armar el video que no se hizo directamente. Ponerle audio es el paso final.
    #restore_audio("RutaDondeEstáElAudioOriginal","RutaDeDondeQuedoElResultadoFinal")

    #Aquí pon el nombre final 
    audio_path = "D:/Esyle-Prod/videos/" + video +".mp4"

    descripcion = "cuttedTest"
    #Agregar como parámetro solo cuando llames a todo pipeline.py en una sola línea.
    vid_final = video + "-" + descripcion

    audio_target = "D:/Esyle-Prod/resultados/" + vid_final + ".mp4"


    print("El tipo de audio_path es:")
    print(type(audio_target))
    print(audio_target)
    restore_audio(audio_path, audio_target)