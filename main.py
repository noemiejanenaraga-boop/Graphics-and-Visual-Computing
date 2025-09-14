from PIL import Image, ImageDraw, ImageFont


img = Image.open("download.jfif")


width, height = 1080, 820
background = Image.new("RGB", (width, height), color="white")

y = height - img.height  

background.paste(img, (0, y))

draw = ImageDraw.Draw(background)
font = ImageFont.truetype("arial.ttf", 60)  
draw.text((20, 20), "Ma'am present rako sa disco!!!", font=font, fill="black")

raw = ImageDraw.Draw(background)
font = ImageFont.truetype("arial.ttf", 60)  
draw.text((500, 250), "Me: ", font=font, fill="white")

  
background.save("poster_result.png")
background.show()
