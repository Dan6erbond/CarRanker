import os
import shutil

import requests
from PIL import Image
from slugify import slugify

from app import create_app
from app.database.models import Car


def create_collage(width, height, images):
    cols = 2
    rows = 2
    thumbnail_width = width // cols
    thumbnail_height = height // rows
    size = thumbnail_width, thumbnail_height
    new_im = Image.new('RGB', (width, height))
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


app = create_app()

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
        filepath = "assets/" + slugify(car.make.name + " " + name) + ".jpg"
        try:
            collage = create_collage(300, 300, filepaths)
            collage.save(filepath)
        except Exception as e:
            print(e)
