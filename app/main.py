from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    name: str = ''
    price: float = 0.0
    is_in_offer: Union[bool, None] = None

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}", response_class=HTMLResponse)                          #http://127.0.0.1:8080/items/5?q=example
async def read_item(request: Request, item_id: int, q: Union[str, None] = None):
    return templates.TemplateResponse("item.html", {"request": request, "item_id": item_id, "q": q})

@app.put("/items/{item_name}")
async def update_item(item_id: int, item: Item):
    return {"Item_name": item.name, "Item_price": item.price}

@app.post("/items/{item_name}")
async def update_item(item_id: int, item: Item):
    return {"Item_name": item.name, "Item_price": item.price}
