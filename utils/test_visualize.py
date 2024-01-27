import os
import json
from glob import glob
from pathlib import Path
from PIL import Image, ImageDraw
import pandas as pd


def read_json(filename: str):
    with Path(filename).open(encoding='utf8') as handle:
        ann = json.load(handle)
    return ann

data = read_json("predictions/output.json")

img_lists = glob('../data/medical/img/test/*.jpg')
img_lists = [i.split('/')[-1] for i in img_lists]

def save_vis_to_img(save_dir: os.PathLike = None, img_lists: list = None) -> None:
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)
        
    for i in range(len(img_lists)):
        img_json = [[k, v] for k, v in data['images'].items() if k == img_lists[i]]
        img_path = img_json[0][0]
        img = Image.open(os.path.join('../data/medical/img/test', img_path)).convert("RGB")
        draw = ImageDraw.Draw(img)

            # All of the prepared dataset consists of words. Not a character.
        for obj_k, obj_v in img_json[0][1]['words'].items():
            obj_name = f"{obj_k}"
            # bbox points
            pts = [(int(p[0]), int(p[1])) for p in obj_v['points']]
            pt1 = sorted(pts, key=lambda x: (x[1], x[0]))[0]


            draw.polygon(pts, outline=(255, 0, 0))
            draw.text(
                (pt1[0]-3, pt1[1]-12),
                obj_name,
                fill=(0, 0, 0)
                )

        img.save(os.path.join(save_dir, img_path))

save_vis_to_img("test_vis_res", img_lists)