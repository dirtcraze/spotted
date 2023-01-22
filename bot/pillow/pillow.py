from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_image(message, time, id, instagram):
    image = Image.open("pillow/template.jpg")

    draw = ImageDraw.Draw(image)

    # Definicja czcionki
    timeFont = ImageFont.truetype("pillow/Roboto-Light.ttf", 22)
    mainFont = ImageFont.truetype("pillow/Proxima.otf", 38)
    idFont = ImageFont.truetype("pillow/Latinka.ttf", 1000)


    instagram = "INSTAGRAM\n@{0}".format(instagram)

    # Wyciąganie potrzebnych danych odnośnie rozmiaru
    wrapped_text = textwrap.fill(message.upper(), width=45)
    id_width, id_height = draw.textsize(str(id), font=idFont)
    text_width, text_height = draw.textsize(wrapped_text, font=mainFont)

    x_id = (image.width - id_width) / 2
    y_id = (image.height - id_height - 200) / 2
    x_text = (image.width - text_width) / 2
    y_text = (900 - text_height) / 2
    if(text_height>200):
        y_text = (820 - text_height) / 2

    # Dodawanie tekstu do zdjęcia
    draw.text((816, 890), time, font=timeFont, fill=(200, 200, 200), align='center', spacing=7)
    draw.text((50, 890), instagram, font=timeFont, fill=(200, 200, 200), align='center', spacing=7)
    draw.text((x_id, y_id), str(id), font=idFont, fill=(19, 19, 19), align='center', stroke_width=5, stroke_fill=(0, 0, 0))
    draw.text((x_text, y_text), wrapped_text, font=mainFont, fill=(220, 220, 220), align='center', spacing=15)
    path = "pillow/images/" + str(id) + ".jpg"
    image.save(path)
    return path
