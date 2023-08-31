file_name = "lesson_7/names.txt"

with open(file_name, mode="r") as file:
    lines = file.readlines()


class FileBase:
    def __init__(self, file: str) -> None:
        self.file = file

    def close(self):
        print(f"Closing file {self.file}")


class FileReader(FileBase):
    def readlines(self):
        print("Reading all lines from the file")

    def write(self):
        print("Readonly!!!")


class FileWriter(FileBase):
    def readlines(self):
        print("Only for writting")

    def write(self, data: str):
        print(f"Writing the {data}")


class open:
    def __init__(self, file_name: str, mode: str) -> None:
        self._file_name = file_name
        self._mode = mode

    def __enter__(self):
        if self._mode == "r":
            self._file_mode_instance = FileReader(self._file_name)
        elif self._mode == "w":
            self._file_mode_instance = FileWriter(self._file_name)
        else:
            raise NotImplementedError

    def __exit__(self, *args, **kwargs):
        self._file_mode_instance.close()
