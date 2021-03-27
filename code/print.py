from PIL import Image, ImageDraw, ImageFont
from datetime import date

def print_date(f = 'input/base.png', fontfile = 'input/arial.ttf', fontsize = 24):
    image = Image.open(f)
    draw = ImageDraw.Draw(image)
    cdate = date.today().strftime('%d %B %Y')
    width, height = image.size
    font = ImageFont.truetype(fontfile, size = fontsize)
    twidth, theight = draw.textsize(cdate, font = font)
    draw.text(((width-twidth)/2, (height-theight)*2/3), cdate, fill='rgb(0,0,0)', font = font)
    image.save('output/'+cdate+'.png', 'PNG')

if __name__=="__main__":
    print_date()