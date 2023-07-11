from fastapi import FastAPI
from db import getById, addMultipleItems, updateItem
from helpers import validateData


app = FastAPI()

@app.get("/")
async def index():
    return {"status" : "ok"}


@app.get("/getQuestionnaire/{itemId}")
async def getItem(itemId:str):
    return await getById(itemId)


@app.post("/createQuestionnaire/")
async def addItem(data:list):
    data,parentId = await validateData(data)
    res = await addMultipleItems(data)
    return parentId


@app.put("/updateQuestionnaire/")
async def updateItems(data:list):
    for item in data:
        Id = item.get("id")
        item.pop("id")
        await updateItem(Id,item)
    return "updated successfully"
