from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_image(message, time, id):
    image = Image.open("template.jpg")

    draw = ImageDraw.Draw(image)

    # Definicja czcionki
    timeFont = ImageFont.truetype("Roboto-Light.ttf", 22)
    mainFont = ImageFont.truetype("Proxima.otf", 38)
    idFont = ImageFont.truetype("Latinka.ttf", 1000)


    # Testowe wiadomości
    text = "Siłownia to miejsce, gdzie można poprawić swoją sylwetkę i zwiększyć siłę. Dzięki regularnym treningom możemy osiągnąć wymarzone rezultaty. Witaj Olu i Kubo! Zróbcie sobie dzisiaj ciężki trening, pamiętajcie o rozgrzewce i skupcie się na technice ćwiczeń. Pamiętajcie, że cierpliwość i konsekwencja przyniosą Wam sukces! Do zobaczenia na siłowni!"
    text2 = "Siłownia to miejsce, gdzie można poprawić swoją sylwetkę i zwiększyć siłę. "
    time = "26 WRZEŚNIA 2022 \nGODZ. 20:00"
    instagram = "INSTAGRAM\n@spotted_fitnessforlife"
    id = "7"

    # Wyciąganie potrzebnych danych odnośnie rozmiaru
    wrapped_text = textwrap.fill(text2.upper(), width=45)
    id_width, id_height = draw.textsize(id, font=idFont)
    text_width, text_height = draw.textsize(wrapped_text, font=mainFont)

    x_id = (image.width - id_width) / 2
    y_id = (image.height - id_height - 200) / 2
    x_text = (image.width - text_width) / 2
    y_text = (image.height - text_height - 70) / 2


    # Dodawanie tekstu do zdjęcia
    draw.text((816, 890), time, font=timeFont, fill=(200, 200, 200), align='center', spacing=7)
    draw.text((50, 890), instagram, font=timeFont, fill=(200, 200, 200), align='center', spacing=7)
    draw.text((x_id, y_id), id, font=idFont, fill=(19, 19, 19), align='center', stroke_width=5, stroke_fill=(0, 0, 0))
    draw.text((x_text, y_text), wrapped_text, font=mainFont, fill=(220, 220, 220), align='center', spacing=15)
    path = "pillow/images/" + str(id) + ".jpg"
    image.save(path)
    return path
