from PIL import Image, ImageDraw, ImageFont

image = Image.open("templateimg.jpg")

draw = ImageDraw.Draw(image)

# Definicja czcionki
time = ImageFont.truetype("Roboto-Medium.ttf", 33)
text = ImageFont.truetype("Roboto-Medium.ttf", 33)
id = ImageFont.truetype("Roboto-Medium.ttf", 47)


# Dodawanie tekstu do zdjęcia
draw.text((106, 51.5), "15:01", font=time, fill=(195, 195, 195))


draw.text((1101, 1103.5), "2", font=id, fill=(195, 195, 195))

image.save("zdjecie_z_tekstem.jpg")
