from PIL import Image, ImageFont, ImageDraw
import textwrap

def decode_image(file_location="Images/encoded_image.png"):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            pixxie = red_channel.getpixel((i,j))
            if bin(pixxie)[-1] == '1':
                decoded_image.putpixel((i,j),(0,0,0))
            else:
                decoded_image.putpixel((i,j),(255,255,255))

    return decoded_image
    # decoded_image.save("images/decoded_image.png")

def write_text(text_to_write, image_size):
    """Writes text to an RGB image. Automatically line wraps
    text_to_write: the text to write to the image
    image_size: size of the resulting text image. Is a tuple (x_size, y_size)
    """
    x_size = image_size[0]
    y_size = image_size[1]
    image_text = Image.new("RGB", image_size)

    if y_size > 200:
        font = ImageFont.truetype("times.ttf", 23)
        interlineado = 25
    else:
        font = ImageFont.load_default().font
        interlineado = 12

    if x_size > 200:
        width = 45
    else:
        width = 15

    drawer = ImageDraw.Draw(image_text)

    #Text wrapping. Change parameters for different text formatting
    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=width):
        drawer.text((margin,offset), line, font=font)
        offset += interlineado
    return image_text

def encode_image(text_to_encode,nombre_imagen,template_image="Images/samoyed.jpg"):
    """Encodes a text message into an image
    text_to_encode: the text to encode into the template image
    template_image: the image to use for encoding. An image is provided by default.
    """
    encoded_image = Image.open(template_image)
    red_channel = encoded_image.split()[0]

    decoded_image = write_text(text_to_encode,encoded_image.size)

    x_size = decoded_image.size[0]
    y_size = decoded_image.size[1]

    for i in range(x_size):
        for j in range(y_size):
            pixxie = decoded_image.getpixel((i,j))
            pix_out = encoded_image.getpixel((i,j))
            bin_red = bin(pix_out[0])
            if pixxie == (0,0,0):
                bin_red = bin_red[0:-1] + '0'
            else:
                bin_red = bin_red[0:-1] + '1'

            red = int(bin_red,2)
            pix_out = (red,pix_out[1],pix_out[2])
            encoded_image.putpixel((i,j),pix_out)

    file_type = nombre_imagen.split('.')[-1]
    if file_type == 'png':
        encoded_image.save(nombre_imagen)
    else:
        encoded_image.save(nombre_imagen + ".png")

# encode_image('Hoola',nombre_imagen="Prueba_1")
# decode_image("Images/Prueba_1.png")
