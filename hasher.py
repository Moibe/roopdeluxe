import base64
import io
import os

def convert_video_to_base64(filename):
    with open(filename, "rb") as f:
        video_bytes = f.read()

    base64_string = base64.b64encode(video_bytes)
    return base64_string.decode("utf-8")

if __name__ == "__main__":
    filename = "result.mp4"
    base64_string = convert_video_to_base64(filename)

    print(base64_string)