from enum import Enum

from fastapi import FastAPI

app = FastAPI()

"""Path parameters"""
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
"""http://127.0.0.1:8000/items/foo
"""


"""Path parameters with types"""
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
""" http://127.0.0.1:8000/items/3
    http://127.0.0.1:8000/items/foo
"""

"""Create an Enum Class"""
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
"""http://127.0.0.1:8000/models/alexnet
"""

"""File Paths"""
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
"""http://127.0.0.1:8000/files//home/johndoe/myfile.txt"""


"""Query parameters"""
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
"""http://127.0.0.1:8000/items/?skip=0&limit=10"""


"""Optional parameters"""
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
"""
http://127.0.0.1:8000/items/foo?short=1
http://127.0.0.1:8000/items/foo?short=True
http://127.0.0.1:8000/items/foo?short=0
"""

