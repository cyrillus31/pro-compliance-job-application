import os


import shutil


import csv


# create data directory


if not os.path.exists("./app/data"):
    os.mkdir("./app/data")


# provide paths to folders for specific file extensions


_upload_folders = {
    "csv": "./app/data/csv",
}


def is_valid_extension(extension: str) -> bool:
    return extension in _upload_folders


def create_uploads_folder(extension):
    folder = _upload_folders[extension]

    if not os.path.exists(folder):
        os.mkdir(folder)


def get_extension(filename: str) -> str:
    extension = os.path.splitext(filename)[1].strip(".")
    return extension


def get_path(extension) -> str:
    return _upload_folders[extension]


def save_file(file) -> bool:
    extension = get_extension(file.filename)

    filename = file.filename.replace(" ", "_")

    path = get_path(extension) + f"/{filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


def get_list_of_all_files_by_extension(extension: str) -> list[str]:
    path = _upload_folders[extension]

    root, folders, files = next(os.walk(path))
    return files
