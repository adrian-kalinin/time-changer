from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from pytz import timezone
import os

import config


def get_current_time():
    return datetime.now(timezone('Europe/Moscow')).strftime('%H:%M')


def generate_image(text):
    image = Image.open(os.getcwd() + config.photo_filename)
    W, H = image.size
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font='resources/ds-digit.ttf', size=270)
    wt, ht = draw.textsize(text, font=font)

    border_size = config.image_border_size
    border_color = config.image_border_color

    draw.text(((W - wt) / 2 - border_size, (H - ht) / 2 - border_size), text, font=font, fill=border_color)
    draw.text(((W - wt) / 2 + border_size, (H - ht) / 2 - border_size), text, font=font, fill=border_color)
    draw.text(((W - wt) / 2 - border_size, (H - ht) / 2 + border_size), text, font=font, fill=border_color)
    draw.text(((W - wt) / 2 + border_size, (H - ht) / 2 + border_size), text, font=font, fill=border_color)

    draw.text(((W - wt) / 2, (H - ht) / 2), text, font=font, fill=config.image_text_color)

    image.save(config.image_filename)


def delete_image():
    os.remove(config.image_filename)


def get_progress_of_the_day():
    now = datetime.now(timezone('Europe/Moscow'))
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds = (now - midnight).seconds
    return round(seconds / 86400 * 100, 1)
