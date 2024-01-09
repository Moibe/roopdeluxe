import os
from roop.utilities import run_ffmpeg

def hacerVideo(video):

    #Y así quedan los commands: 
    #['-hwaccel', 'auto', '-r', '30', '-i', 'videos\\temp\\triple\\%04d.png', '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-vf', 'colorspace=bt709:iall=bt601-6-625:fast=1', '-y', 'videos\\temp\\triple\\temp.mp4']     

    #origin_path = os.path.join("D:/Esyle-Prod/videos/temp/" + vid_original, "%04d.png")
    origin_path = "D:/Esyle-Prod/videos/temp/" + video + "/%04d.png"

    #Vid_destino, no se necesitará.
    #vid_destino = "22-framefixed"

    #destiny_path = os.path.join("D:/Esyle-Prod/videos/", vid_destino + ".mp4")
    destiny_path = "D:/Esyle-Prod/videos/temp/" + video + "/temp.mp4"

    args = ['-hwaccel', 'auto', '-r', '30', '-i', origin_path, '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-vf', 'colorspace=bt709:iall=bt601-6-625:fast=1', '-y', destiny_path]     

    print("Los args son:")
    print(args)
    run_ffmpeg(args)