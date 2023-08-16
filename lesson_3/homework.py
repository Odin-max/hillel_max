from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent

file = open(ROOT_DIR / "rockyou.txt", "r", encoding="utf-8")

text = file.readline()

results = []

while True:
    try:
        word = file.readline()
        if word.startswith("user"):
            # ДЛЯ ЛІНИВИХ
            # my_input = "y"
            # print(f"Додати слово '{word.strip()}' до результату? (y/n): {my_input}")
            my_input = input(f"Додати слово '{word.strip()}' до результату? (y/n): ").lower()
            if my_input == "y":
                results.append(word)
            else:
                print("wrong answer") 
        if not word:
            break   
    except:
        pass

file.close()

print("Результати:", ''.join(results))

