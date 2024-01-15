import http.cookiejar
import urllib

cookiejar = http.cookiejar.CookieJar()

cookie_handler = urllib.request.HTTPCookieProcessor(cookiejar)

# Abra la URL en su navegador para generar la cookie necesaria.

# Copie la cookie desde su navegador.

cookie_value = "eyJhbGciOiJFZERTQSJ9.eyJyZWFkIjp0cnVlLCJvbkJlaGFsZk9mIjp7Il9pZCI6IjYzZTNjYTVmYzY1Zjk3NWI0MzZlMzM2NCIsInVzZXIiOiJNb2liZSJ9LCJpYXQiOjE3MDUyMjIwMTksInN1YiI6Ii9zcGFjZXMvTW9pYmUvdmlkZW8iLCJleHAiOjE3MDUzMDg0MTksImlzcyI6Imh0dHBzOi8vaHVnZ2luZ2ZhY2UuY28ifQ.haEkPgrbQZ0TEAiOGH5_C-LVpbtL_K6d5pys2HjXlc-zb6M30iGJh79cRmBrM2VqPehfODhXfdD8TLtq_VI0DA"

cookie_value = bytes(cookie_value, "utf-8")

url = "https://moibe-video.hf.space/--replicas/rzjof/file=/tmp/gradio/24ac48bd3028fc69e1c09d7f9819c6435e1326c5/temp/stockings/0015.png"

request = urllib.request.Request(url)

request.add_header("Cookie", cookie_value)

opener = urllib.request.build_opener(cookie_handler)

urllib.request.install_opener(opener)

urllib.request.urlretrieve(request, "local-filename.jpg")
