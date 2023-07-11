from datetime import datetime
from pytz import timezone

async def validateData(data):
    sectionId = None
    parentId = await generate_hash()
    insertData=[]
    for item in data:
        item.update({"parentId" :parentId})
        if item["type"] != "heading" and sectionId:
            item.update({"sectionId" :sectionId})
            item.update({"id":await generate_hash()})
        elif item["type"] == "heading":
            sectionId = await generate_hash()
            item.update({"id": sectionId})
        insertData.append(item)
    return insertData,parentId


temp=0
async def generate_hash():
    global temp
    now = datetime.now(timezone("Asia/Kolkata"))
    hash_value = now.strftime("%Y%m%d%H%M%S%f")
    temp += 1
    final_hash = hex(int(hash_value) + temp)[2:]
    return final_hash
