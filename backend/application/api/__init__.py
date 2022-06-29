from flask import Blueprint, jsonify
from os import getcwd, listdir, path, mkdir
import json
import re
from random import randrange, shuffle

bp = Blueprint("api", __name__)


@bp.get("/")
def index():
    return jsonify({
        "status": 200,
        "message": "Welcome"
    })


@bp.get("/generate_meta")
def generate_meta():

    def generate(gender="male"):
        asset_path = f"{getcwd()}/assets"
        id = 0
        out_list = []
        for a in [y for y in listdir(f"{asset_path}/{gender}/ethnicity")]:
            for b in [y for y in listdir(f"{asset_path}/{gender}/nose/{a.split('.')[0]}")]:
                for c in [y for y in listdir(f"{asset_path}/{gender}/eye")]:
                    for d in [y for y in listdir(f"{asset_path}/{gender}/eyebrow")]:
                        for e in [y for y in listdir(f"{asset_path}/{gender}/mouth")]:
                            for f in [y for y in listdir(f"{asset_path}/{gender}/costume")]:
                                for g in [y for y in listdir(f"{asset_path}/{gender}/hair") if not re.search('back', y, re.IGNORECASE)]:
                                    for h in [y for y in listdir(f"{asset_path}/background")]:
                                        id += 1
                                        out_list.append({
                                            "id": id,
                                            "gender": gender,
                                            "ethnicity": a,
                                            "nose": b,
                                            "eye": c,
                                            "eyebrow": d,
                                            "mouth": e,
                                            "costume": f,
                                            "hair": g,
                                            "background": h
                                        })

        return out_list

    male = generate("male")
    female = generate("female")
    shuffle(male)
    shuffle(female)
    male = male[:5000]
    female = female[:5000]
    meta = [*male, *female]
    shuffle(meta)

    j = 0
    for i in meta:
        j += 1
        i["id"] = j

    output = f"{getcwd()}/static"
    if not path.exists(output):
        mkdir(output)
    with open(f"{output}/meta.json", 'w+', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=4)
    print("done 3")

    return jsonify({
        "status": 200,
        "message": "ok"
    })
