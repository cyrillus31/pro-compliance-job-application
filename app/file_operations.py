import os
import csv
import re


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

    def __init__(self, filename):
        Csv.update_paths()
        if filename in Csv.files:
            self.path = Csv._folder_path + "/" + filename
        else:
            raise Exception("This file doesn't exist on a server")

    def filter_data(
        self,
        column_to_filter: str,
        list_of_columns_to_display: list[str],
        like: str = "",
    ):
        result = {}
        with open(self.path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            if column_to_filter not in reader.fieldnames:
                raise Exception("This column doesn't exist in this document")
            for row in reader:
                if like in row[column_to_filter]:
                    for column in list_of_columns_to_display:
                        if column not in result:
                            result[column] = [row[column]]
                        else:
                            result[column].append(row[column])

        return result


# mycsv = Csv("Electric_Vehicle_Population_Data.csv")
# print(
# mycsv.filter_data(
# column_to_filter="City",
# list_of_columns_to_display=["City", "State", "Make"],
# like="Seattle",
# )
# )
