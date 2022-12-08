from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import webscrapper
from pydantic import BaseModel

class Item(BaseModel):
    nombre: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/getNombresEmpresas")
def read_root():
    nombresEmpresas = webscrapper.getNombresEmpresas()
    return nombresEmpresas

@app.post("/api/getLiquidezGeneral")
async def getLiquidezGeneral(item: Item):
    liquidezGeneral = webscrapper.getLiquidezGeneral(item.nombre)
    return liquidezGeneral
