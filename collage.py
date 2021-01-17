import os
import shutil

import requests
from PIL import Image, ImageFont, ImageDraw
from slugify import slugify

from app import create_app
from app.database.models import Car


def create_collage(width, height, images):
    cols = 2
    rows = 2
    thumbnail_width = width // cols
    thumbnail_height = height // rows
    size = thumbnail_width, thumbnail_height
    new_im = Image.new('RGB', (width, height), "#fff")
    ims = []
    for p in images:
        im = Image.open(p)
        shorter_side = im.height if im.width >= im.height else im.width
        start_x = (im.width - shorter_side) / 2
        start_y = (im.height - shorter_side) / 2
        region = im.crop((start_x, start_y, start_x + shorter_side, start_y + shorter_side))
        region.thumbnail(size)
        ims.append(region)
    i, x, y = 0, 0, 0
    for _col in range(cols):
        for _row in range(rows):
            new_im.paste(ims[i], (x, y))
            i += 1
            y += thumbnail_height
        x += thumbnail_width
        y = 0

    return new_im


def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


app = create_app()
title = ImageFont.truetype("arial.ttf", 14)
body = ImageFont.truetype("arial.ttf", 12)
subtitle = ImageFont.truetype("arial.ttf", 11)

with app.app_context():
    cars = Car.query.all()
    for car in cars:
        filepaths = list()
        for image in car.images:
            filename = image.url.split("/")[-1]
            filepath = "assets/" + filename
            filepaths.append(filepath)

            if os.path.exists(filepath):
                continue

            r = requests.get(image.url, stream=True)
            r.raw.decode_content = True

            with open(filepath, "wb+") as f:
                shutil.copyfileobj(r.raw, f)

        name = car.type_full or car.variant
        filepath = "assets/" + slugify(f"{car.make.name} {name}") + ".png"
        try:
            org_collage = create_collage(300, 300, filepaths)

            collage = Image.new('RGB', (300, 450), (255, 255, 255))
            draw = ImageDraw.Draw(collage)

            draw.text((10, 20), f"{car.make.name} {name}", (0, 0, 0), font=title)

            collage.paste(org_collage, (0, 50))

            draw.text((10, 350 + 10 + 0 * 20),
                      f"{car.horse_power} HP / {car.consumption_combined} l/km", (0, 0, 0),
                      font=body)
            draw.text((10, 350 + 10 + 1 * 20), f"{car.price} CHF", (0, 0, 0), font=body)
            draw.text((10, 350 + 10 + 2 * 20), f"{car.doors} doors / {car.seats} seats", (0, 0, 0), font=body)
            draw.text((10, 350 + 10 + 3 * 20), car.drive_type.value, (0, 0, 0), font=body)

            draw.text((200, 420), "CarMaker, 2021", (0, 0, 0), font=subtitle)

            collage = add_corners(collage, 15)

            collage.save(filepath)
            print("Successfully exported", filepath)
        except Exception as e:
            print(e)
