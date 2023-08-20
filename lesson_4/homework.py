team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def show_players(players: list[dict]) -> None:
    print("Your team: ")
    for player in players:
        print(
            f"Name: {player['name']}, "
            f"Age: {player['age']}, "
            f"Number: {player['number']}"
        )

    print()


def add_player(num: int, name: str, age: int) -> None:
    new_player = {"name": name, "age": age, "number": num}
    team.append(new_player)
    print(f"Player {name} with number {num} was added")


def remove_player(players: list[dict], num: int) -> None:
    removed_player = None
    for player in players:
        if player["number"] == num:
            removed_player = player
            players.remove(player)
            break

    if removed_player:
        print(f"Removed player {removed_player['name']} with number {num}")
    else:
        print("No player was found")

    print()


def main():
    show_players(team)

    add_player(num=17, name="Chris", age=31)
    add_player(num=17, name="Bob", age=39)
    remove_player(players=team, num=17)

    show_players(team)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
