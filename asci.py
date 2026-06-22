from PIL import Image

ASCII_CHARS = "@$B%8&WM#*oahkbdpqwmZO0QLCJUXYzcvuxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def image_to_ascii(image_path, width=200):

    image = Image.open(image_path)

    aspect_ratio = image.height / image.width
    height = int(width * aspect_ratio * 0.55)

    image = image.resize((width, height))

    image = image.convert("L")

    pixels = image.getdata()

    ascii_str = ""

    for pixel in pixels:
        ascii_str += ASCII_CHARS[
            pixel * len(ASCII_CHARS) // 256
        ]

    ascii_art = ""

    for i in range(0, len(ascii_str), width):
        ascii_art += ascii_str[i:i + width] + "\n"

    return ascii_art