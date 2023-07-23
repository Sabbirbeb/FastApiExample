from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    name: str = ''
    price: float = 0.0
    is_in_offer: Union[bool, None] = None

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    read_root async function.

    :param response_class: class of response 
    :return: root navigation page
    """ 
    return templates.TemplateResponse("root.html", {"request": request})

@app.get("/main", response_class=HTMLResponse)
async def main(request: Request):
    """
    main async function.

    :param response_class: class of response 
    :return: main page with (bootstrap)
    """ 
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{item_id}", response_class=HTMLResponse)
async def read_item(request: Request, item_id: int, q: Union[str, None] = None):
    """
    read_item async function.

    :param response_class: class of response 
    :param item_id: path parameter item id
    :param q: query parameter means nothing 
    :return: item page (html+css+js)
    """ 
    return templates.TemplateResponse("item.html", {"request": request, "item_id": item_id, "q": q})



@app.put("/items/{item_name}")
async def update_item(item_id: int, item: Item):
    return {"Item_name": item.name, "Item_price": item.price}

@app.post("/items/{item_name}")
async def update_item(item_id: int, item: Item):
    return {"Item_name": item.name, "Item_price": item.price}
