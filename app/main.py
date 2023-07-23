import shutil

from fastapi import FastAPI, HTTPException, UploadFile, status
from fastapi.responses import HTMLResponse

from app import file_operations
from . import utils
from . import models


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root():
    with open("app/templates/index.html", "r") as tmp:
        content = tmp.read()

        return HTMLResponse(content=content, status_code=200)


@app.post("/upload", status_code=status.HTTP_201_CREATED)
def upload_file(file: UploadFile):
    if not file.filename:
        raise HTTPException(
            status_code=400, detail="Provide a file with valid extension"
        )

    extension = utils.get_extension(file.filename)

    if utils.is_valid_extension(extension):
        utils.create_uploads_folder(extension)
        utils.save_file(file)
        models.create_table_from_csv(file.filename)

        return {
            "filename": file.filename,
            "detail": "File saved on a server successfully",
        }

    else:
        raise HTTPException(
            status_code=400,
            detail=f"Files of {extension} format are not yet supported",
        )


@app.get("/{extension}", status_code=status.HTTP_200_OK)
def list_files(extension: str):
    all_files_all_columns = file_operations.Csv.get_all_files_all_columns()
    return {"files": all_files_all_columns}


@app.get("/{extension}/{filename}", status_code=status.HTTP_200_OK)
def filter_data(
    column: str = "",
    limit: int = 0,
):
    pass
