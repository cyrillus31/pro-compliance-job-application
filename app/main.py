import shutil


from fastapi import FastAPI, HTTPException, UploadFile, status

from fastapi.responses import HTMLResponse

from . import utils


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root():
    with open("app/templates/index.html", "r") as tmp:
        content = tmp.read()
        return HTMLResponse(content=content, status_code=200)


@app.post("/upload_csv", status_code=status.HTTP_201_CREATED)
def upload_file(file: UploadFile):
    utils.create_uploads_folders()
    print(file, type(file))
    if not file.filename:
        raise HTTPException(status_code=400)
    else:
        path = utils.get_the_path(file.filename) + f"/{file.filename}"
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {"filename": file.filename}
