from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from pytz import timezone
import io


def get_current_time():
    return datetime.now(timezone('Europe/Moscow')).strftime('%H:%M')


def generate_image(text):
    image = Image.new('RGB', (500, 500), color='black')
    W, H = image.size
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font='resources/ds-digit.ttf', size=212)
    wt, ht = draw.textsize(text, font=font)
    draw.text(((W - wt) / 2, (H - ht) / 2 ), text, font=font, fill='#157381')
    im = io.BytesIO()
    im.name = 'time_image.jpg'
    image.save(im, 'JPG')
    im.seek(0)
    return im
