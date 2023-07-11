from pymongo import MongoClient

client = MongoClient("mongodb+srv://709:709@atlascluster.9hfxnz5.mongodb.net/?retryWrites=true&w=majority")


async def getById(Id):
    res = client.test.test.find({"parentId":Id},{ "_id": 0,"parentId":0})
    return [x for x in res]


async def addMultipleItems(data):
    client.test.test.insert_many(data)
    return "data added successfully"


async def updateItem(Id,data):
    client.test.test.update_one({"id":Id},{"$set":data})
