class Team:
    def __init__(self, name) -> None:
        self.name = name
        self._team = {"John"}

    def __getitem__(self, key: str):
        if key not in self._team.keys():
            print("john is not here!")
        else:
            print(f"{key} is there")


school_12 = Team(name="School 12")
school_12["John"]
