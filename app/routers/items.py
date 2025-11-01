from fastapi import (APIRouter, 
                     Depends, 
                     HTTPException, 
                     File, 
                     UploadFile )


from ..dependencies import get_token_header
from ..models import ClipModel
import random



router = APIRouter(
    prefix="/clips",
    tags=["clips"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.post("/uploadfile/")
async def uploadfile(file: UploadFile):
    try:
        file_path = f"/Users/reecelock/development/python/FanSite/app/clips/{file.filename}"
        print(file_path)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
            return {"message": "File saved successfully"}
    except Exception as e:
        return {"message": e.args}


# @router.get("/")
# async def read_items():
#     return fake_items_db


# @router.get("/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in fake_items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


# @router.put(
#     "/{item_id}",
#     tags=["custom"],
#     responses={403: {"description": "Operation forbidden"}},
# )
# async def update_item(item_id: str):
#     if item_id != "plumbus":
#         raise HTTPException(
#             status_code=403, detail="You can only update the item: plumbus"
#         )
#     return {"item_id": item_id, "name": "The great Plumbus"}
