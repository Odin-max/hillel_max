from pathlib import Path

ROOT_DiR = Path(__file__).absolute().parent.parent

file = open(ROOT_DiR / "rockyou.txt","r", encoding="utf-8")
text: str = file.readline()
counter = 0
while True:
    try:
        word = file.readline()
        counter += 1
        print(word)
    except Exception:
        break   

print(counter)
