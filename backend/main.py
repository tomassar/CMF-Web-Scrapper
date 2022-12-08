from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import webscrapper
from pydantic import BaseModel
from mangum import Mangum

class Item(BaseModel):
    nombre: str


app = FastAPI()
handler = Mangum(app)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/getNombresEmpresas")
def read_root():
    nombresEmpresas = webscrapper.getNombresEmpresas()
    return nombresEmpresas

@app.get("/api/hola")
def hola():
    return webscrapper.hola()

@app.post("/api/getLiquidezGeneral")
async def getLiquidezGeneral(item: Item):
    liquidezGeneral = webscrapper.getLiquidezGeneral(item.nombre)
    return liquidezGeneral

""" @app.get("/api/getLiquidezGeneral/{nombreEmpresa}")
def read_root(nombreEmpresa: str):
    liquidezGeneral = webscrapper.getLiquidezGeneral(nombreEmpresa)
    return liquidezGeneral """

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}