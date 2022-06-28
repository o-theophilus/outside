from flask import Blueprint, jsonify
from os import getcwd
import json

bp = Blueprint("nft", __name__)


@bp.get("/nft")
def get_all():

    output = f"{getcwd()}/static"

    with open(f"{output}/meta.json") as f:
        data = json.load(f)

    return jsonify({
        "status": 200,
        "message": "ok",
        "data": data
    })


@bp.get("/nft/<id>")
def get(id):

    output = f"{getcwd()}/static"

    with open(f"{output}/meta.json") as f:
        data = json.load(f)

    meta = None
    for i in data:
        if i["id"] == int(id):
            meta = i
            break

    if not meta:
        return jsonify({
            "status": 401,
            "message": "invalid request",
        })

    return jsonify({
        "status": 200,
        "message": "ok",
        "data": meta
    })
