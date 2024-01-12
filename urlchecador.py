import requests

url = "https://huggingface.co/countfloyd/deepfake/resolve/main/inswapper_128.onnx"

response = requests.get(url)

content = response.content

print(content)