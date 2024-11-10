import sys
from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://anujkumartiwarinmims:Anuj123@mymongodbcluster.6gxvf.mongodb.net")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    doc = conn.notes.notes.find({})
    for d in doc:
        print(d)
    return templates.TemplateResponse("index.html", {"request": request})

