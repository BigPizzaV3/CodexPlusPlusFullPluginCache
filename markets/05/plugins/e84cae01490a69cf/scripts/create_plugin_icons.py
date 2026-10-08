from pathlib import Path
from PIL import Image, ImageDraw


def make_icon(path: Path, size: int) -> None:
    image = Image.new("RGBA", (size, size), "#00A82D")
    draw = ImageDraw.Draw(image)
    radius = size // 5
    draw.rounded_rectangle((0, 0, size - 1, size - 1), radius=radius, fill="#00A82D")
    s = size / 512
    # Conventional Z: horizontal bars with a diagonal descending from right to left.
    draw.rectangle((136*s, 142*s, 376*s, 200*s), fill="white")
    draw.polygon([(334*s, 176*s), (376*s, 218*s), (218*s, 370*s), (176*s, 328*s)], fill="white")
    draw.rectangle((136*s, 312*s, 376*s, 370*s), fill="white")
    draw.ellipse((370*s, 106*s, 406*s, 142*s), fill="#D7F7DE")
    image.save(path)


root = Path(__file__).resolve().parents[1] / "assets"
root.mkdir(exist_ok=True)
make_icon(root / "composer-icon.png", 512)
make_icon(root / "logo.png", 1024)
