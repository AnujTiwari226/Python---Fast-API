from typing import Union

from fastapi import FastAPI
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/test/{item_id}")
async def get_item(item_id: int, q: str | None = None):
    result = {"item_id": item_id, "Q": q}
    logger.info(result)  # Debug output in the console
    return result
