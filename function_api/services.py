#services.py
from function_api.crud import *
from fastapi import Depends
from fastapi.responses import JSONResponse
from function_api.database import *

item_service = ItemService()
class ItemView:
    async def get(self, item_id: int, db: Session = Depends(get_db)):
        item = item_service.get_item_by_id(db, item_id)
        if item:
            return item
        return JSONResponse(status_code=404, content={"message": "Item not found"})

    async def post(self, item_data: ItemCreateRequest, db: Session = Depends(get_db)):
        item = item_service.create_item(db, item_data)
        return item

    async def put(self, item_id: int, item_data: ItemUpdateRequest, db: Session = Depends(get_db)):
        item = item_service.update_item(db, item_id, item_data)
        if item:
            return item
        return JSONResponse(status_code=404, content={"message": "Item not found"})

    async def delete(self, item_id: int, db: Session = Depends(get_db)):
        success = item_service.delete_item(db, item_id)
        if success:
            return {"message": "Item deleted"}
        return JSONResponse(status_code=404, content={"message": "Item not found"})
