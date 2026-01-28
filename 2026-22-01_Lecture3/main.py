"""
This file handles the API routes only
"""

from typing import Union

from fastapi import FastAPI
from scoring import predict as scoring_predict, format_output as scoring_format_output

app = FastAPI()


@app.get("/")
def root():
    return scoring_predict()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return scoring_format_output(item_id, q)