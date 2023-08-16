from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent

file = open(ROOT_DIR / "rockyou.txt", "r", encoding="utf-8")

text = file.readline()

results = []
lines = 0
while True:
    try:
        word = file.readline()
        if word.startswith("user"):
            my_input = input(
                f"Додати слово '{word.strip()}' до результату? (y/n): "
            ).lower()
            if my_input == "y":
                results.append(word)
                lines += 1
            else:
                print("wrong answer")
        if not word:
            break
    except Exception:
        break

file.close()

print("Результати:", "".join(results))
print("Всього строк: ", lines)
