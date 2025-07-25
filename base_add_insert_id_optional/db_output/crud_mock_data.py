# CRUD operations for mock_data
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, date
from lingzhihua_db_models.models_all_table import MockData   # 导入 MockData 模型，注意文件位置


# 获取单条 mock_data 数据
def get_mock_data(db: Session, id: int):
    result = db.query(MockData).filter(MockData.id == id).first()
    return result.to_dict() if result else None

# 获取 mock_data 列表
def get_mock_data_list(db: Session, skip: int = 0, limit: int = 100):
    mock_data_list = db.query(MockData).offset(skip).limit(limit).all()
    return [item.to_dict() for item in mock_data_list]

# 创建 mock_data 数据
def create_mock_data(db: Session, make:str, model:str, price:str,id: Optional[int] = None,):
    db_mock_data = MockData(id=id, make=make, model=model, price=price)
    db.add(db_mock_data)
    db.commit()
    db.refresh(db_mock_data)
    return db_mock_data.to_dict()

# 更新 mock_data 数据
def update_mock_data(db: Session, id: int, make: Optional[str] = None, model: Optional[str] = None, price: Optional[str] = None):
    db_mock_data = db.query(MockData).filter(MockData.id == id).first()
    if db_mock_data:
        
        if id is not None:
            db_mock_data.id = id
        
        if make is not None:
            db_mock_data.make = make
        
        if model is not None:
            db_mock_data.model = model
        
        if price is not None:
            db_mock_data.price = price
        
        db.commit()
        db.refresh(db_mock_data)
    return db_mock_data.to_dict() if db_mock_data else None

# 删除 mock_data 数据
def delete_mock_data(db: Session, id: int):
    db_mock_data = db.query(MockData).filter(MockData.id == id).first()
    if db_mock_data:
        db.delete(db_mock_data)
        db.commit()
    return True if db_mock_data else False