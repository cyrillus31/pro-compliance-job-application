import os


upload_folders = {"csv": "./app/data"}


def create_uploads_folders():
    for folder in upload_folders.values():
        if not os.path.exists(folder):
            os.mkdir(folder)


def get_the_path(file: str) -> str:
    extension = os.path.splitext(file)[1].strip(".")
    return upload_folders[extension]
