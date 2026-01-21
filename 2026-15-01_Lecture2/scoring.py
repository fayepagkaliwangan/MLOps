"""
Temporary placeholder for the scoring algorithm
"""

from typing import Union

def predict():
    return {"score":1}

def format_output(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
