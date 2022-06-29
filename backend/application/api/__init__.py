from flask import Blueprint, jsonify
from os import getcwd, listdir, path, mkdir
import json
import re
from random import randrange

bp = Blueprint("api", __name__)


@bp.get("/")
def index():
    return jsonify({
        "status": 200,
        "message": "Welcome"
    })


@bp.get("/generate_meta")
def generate_meta():
    asset_path = f"{getcwd()}/assets"

    id = 0

    def generate(gender="male"):
        nonlocal id
        _meta = []
        for a in [y for y in listdir(f"{asset_path}/{gender}/ethnicity")]:
            for b in [y for y in listdir(f"{asset_path}/{gender}/nose/{a.split('.')[0]}")]:
                for c in [y for y in listdir(f"{asset_path}/{gender}/eye")]:
                    for d in [y for y in listdir(f"{asset_path}/{gender}/eyebrow")]:
                        for e in [y for y in listdir(f"{asset_path}/{gender}/mouth")]:
                            for f in [y for y in listdir(f"{asset_path}/{gender}/costume")]:
                                for g in [y for y in listdir(f"{asset_path}/{gender}/hair") if not re.search('back', y, re.IGNORECASE)]:
                                    for h in [y for y in listdir(f"{asset_path}/background")]:
                                        id += 1
                                        _meta.append({
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

                                        if len(_meta) == 1000:
                                            return _meta
        return _meta

    meta = [*generate("male"), *generate("female")]
    print("done 1")

    used = []
    _meta = []
    j = 0
    while len(_meta) < 1000:
        i = randrange(0, len(meta))

        if i not in used:
            used.append(i)
            j += 1
            meta[i]["id"] = j
            _meta.append(meta[i])

    meta = _meta

    output = f"{getcwd()}/static"
    if not path.exists(output):
        mkdir(output)
    with open(f"{output}/meta.json", 'w+', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=4)
    print("done 2")

    return jsonify({
        "status": 200,
        "message": "ok"
    })
