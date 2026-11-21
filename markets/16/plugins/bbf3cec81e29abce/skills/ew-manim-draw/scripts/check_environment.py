import importlib.util, shutil, json
print(json.dumps({"python":True,"manim":bool(importlib.util.find_spec("manim")),"pillow":bool(importlib.util.find_spec("PIL")),"ffmpeg":bool(shutil.which("ffmpeg")),"mobile_install_required":False},ensure_ascii=False,indent=2))
