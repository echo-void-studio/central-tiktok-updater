#!/usr/bin/env python3
"""Update extera-plugins.json using metadata from plugins/*.plugin."""
import argparse
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIELDS = {"id", "name", "version", "description", "author", "category", "icon", "app_version", "sdk_version", "requirements"}

def plugin_meta(path):
    data = {}
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id.startswith("__") and target.id.endswith("__"):
                key = target.id.strip("_")
                if key in FIELDS:
                    data[key] = ast.literal_eval(node.value)
    for required in ("id", "name", "version"):
        if not data.get(required):
            raise ValueError(f"Missing metadata: {required} in {path}")
    return data

def generate():
    plugins = []
    for path in sorted((ROOT / "plugins").glob("*.plugin")):
        raw = path.read_bytes()
        meta = plugin_meta(path)
        meta["file"] = path.relative_to(ROOT).as_posix()
        meta["sha256"] = hashlib.sha256(raw).hexdigest()
        meta["size"] = len(raw)
        plugins.append(meta)
    doc = {
        "schema": 1,
        "name": "Central TikTok Updater",
        "description": "Private Plus ARM8 updates watcher for AyuGram/exteraGram",
        "author": "echo-void-studio",
        "homepage": "https://github.com/echo-void-studio/central-tiktok-updater",
        "plugins": plugins,
    }
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true")
    args = p.parse_args()
    output = generate()
    index = ROOT / "extera-plugins.json"
    if args.check:
        if not index.exists() or index.read_text(encoding="utf-8") != output:
            raise SystemExit("Index is stale; run python build_index.py")
        print("Index is current")
    else:
        index.write_text(output, encoding="utf-8")
        print("Index generated")
