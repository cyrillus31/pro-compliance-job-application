import os
import csv


class Csv:
    _folder_path = "./app/data/csv"

    files = []
    path_to_files = []

    @classmethod
    def update_paths(cls):
        root, folders, files = next(os.walk(cls._folder_path))
        cls.files = files
        cls.path_to_files = [root + "/" + file for file in files]

    @classmethod
    def get_all_files_all_columns(cls) -> dict:
        cls.update_paths()
        result = {}
        for file in cls.files:
            with open(f"{cls._folder_path}/{file}", "r", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file)
                result[file] = {"columns": reader.fieldnames}
        return result

    def __init__(self, path):
        self.path = path


# print(Csv.get_all_files_all_columns())
