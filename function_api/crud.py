#crud.py
from sqlalchemy.orm import Session
from function_api.schemas import ItemCreateRequest, ItemUpdateRequest
from function_api.models import Item

class ItemService:
    def get_item_by_id(self, db: Session, item_id: int):
        return db.query(Item).filter(Item.id == item_id).first()

    def create_item(self, db: Session, item_data: ItemCreateRequest):
        item = Item(**item_data.dict())
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    def update_item(self, db: Session, item_id: int, item_data: ItemUpdateRequest):
        item = db.query(Item).filter(Item.id == item_id).first()
        if item:
            for field, value in item_data.dict().items():
                setattr(item, field, value)
            db.commit()
            db.refresh(item)
        return item

    def delete_item(self, db: Session, item_id: int):
        item = db.query(Item).filter(Item.id == item_id).first()
        if item:
            db.delete(item)
            db.commit()
            return True
        return False
