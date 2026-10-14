"""Ustvari podstrani /<domena>/index.html iz index.html.

Zaženite po vsaki spremembi index.html:  python3 build.py
"""
import pathlib, re, shutil

root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")
block = html[html.index("const DOMAINS = ["):]
names = re.findall(r'name:\s*"([^"]+)"', block[:block.index("];")])

for old in root.glob("*.si"):
    if old.is_dir() and old.name not in names:
        shutil.rmtree(old)
for name in names:
    (root / name).mkdir(exist_ok=True)
    (root / name / "index.html").write_text(html, encoding="utf-8")
(root / "404.html").write_text(html, encoding="utf-8")
print("Ustvarjenih podstrani:", len(names))
