from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def draw_pic(filePath):
    img = Image.open(filePath)
    size=img.size
    font_size = size[1]/4;
    position = size[1]-font_size
    text = "2"
    dra = ImageDraw.Draw(img)
    font=ImageFont.truetype("arial.ttf",size=font_size)
    dra.text((position,0),str(text),(255,255,0),font)
    return img

draw_pic('0000.png').save('re.png')