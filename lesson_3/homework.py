from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent

file = open(ROOT_DIR / "rockyou.txt", "r", encoding="utf-8")

text = file.readline()

results = []

while True:
    try:
        word = file.readline()
        if word.startswith("user"):

