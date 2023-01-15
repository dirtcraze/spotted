from PIL import Image, ImageDraw, ImageFont

# return path


def create_image(message, time, id):
    image = Image.open("pillow/templateimg.jpg")
    draw = ImageDraw.Draw(image)
    # Definicja czcionki
    fonttime = ImageFont.truetype("pillow/Roboto-Medium.ttf", 33)
    text = ImageFont.truetype("pillow/Roboto-Medium.ttf", 33)
    fontid = ImageFont.truetype("pillow/Roboto-Medium.ttf", 47)
    # Dodawanie tekstu do zdjęcia
    draw.text((106, 51.5), time, font=fonttime, fill=(195, 195, 195))
    draw.text((1101, 1103.5), str(id), font=fontid, fill=(195, 195, 195))
    path = "pillow/images/" + str(id) + ".jpg"
    image.save(path)
    return path
