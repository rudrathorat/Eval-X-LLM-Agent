# api.py

from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from model import evaluate_prompt, load_csv_to_memory
import shutil
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Question(BaseModel):
    question: str

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/evaluate")
async def evaluate(question: Question):
    response = evaluate_prompt(question.question)
    return JSONResponse(content={"answer": response})

@app.post("/upload_csv")
async def upload_csv(file: UploadFile = File(...)):
    upload_dir = "csv_data"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Load CSV to memory
    load_csv_to_memory(file_path)

    return {"message": "CSV uploaded. Now ask your question."}
