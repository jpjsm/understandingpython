"""Create Application."""

from pathlib import Path

from fastapi import FastAPI, UploadFile


app = FastAPI()

uploads_folder = Path('./uploaded').mkdir(mode=711, parents=True, exist_ok=True)

@app.get("/")
async def root():
    """Heartbeat response.

    :return: hello world hearbeat string
    """
    return {"message": "Hello World!! welcome to file uploader."}

@app.post("/upload/")
async def uploadfile(file: UploadFile):
    try:
        file_path = uploads_folder.joinpath(file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
            return {"message": "File saved successfully"}
    except Exception as e:
        return {"message": e.args}