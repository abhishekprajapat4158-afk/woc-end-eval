from PIL import Image
def decode_message(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    binary_message = ""
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]

     
            binary_message += str(r & 1)

         
            if binary_message.endswith("1111111111111110"):
                binary_message = binary_message[:-16]
                break
        else:
            continue
        break

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))

    return message
encoded_image= "output.png"
secret_text = decode_message(encoded_image)
print("decoded secret message:",secret_text)
print("end of program")