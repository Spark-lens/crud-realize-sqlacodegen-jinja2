# CRUD operations for vendors
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, date
from db_models.models_all_table import Vendors   # 导入 Vendors 模型，注意文件位置


# 获取单条 vendors 数据
def get_vendors(db: Session, vendor_id: int):
    result = db.query(Vendors).filter(Vendors.vendor_id == vendor_id).first()
    return result.to_dict() if result else None

# 获取 vendors 列表
def get_vendors_list(db: Session, skip: int = 0, limit: int = 100):
    vendors_list = db.query(Vendors).offset(skip).limit(limit).all()
    return [item.to_dict() for item in vendors_list]

# 创建 vendors 数据
def create_vendors(db: Session, vendor_id:int, vendor_name:str):
    db_vendors = Vendors(vendor_id=vendor_id, vendor_name=vendor_name)
    db.add(db_vendors)
    db.commit()
    db.refresh(db_vendors)
    return db_vendors.to_dict()

# 更新 vendors 数据
def update_vendors(db: Session, vendor_id: int, vendor_name: Optional[str] = None):
    db_vendors = db.query(Vendors).filter(Vendors.vendor_id == vendor_id).first()
    if db_vendors:
        
        if vendor_id is not None:
            db_vendors.vendor_id = vendor_id
        
        if vendor_name is not None:
            db_vendors.vendor_name = vendor_name
        
        db.commit()
        db.refresh(db_vendors)
    return db_vendors.to_dict() if db_vendors else None

# 删除 vendors 数据
def delete_vendors(db: Session, vendor_id: int):
    db_vendors = db.query(Vendors).filter(Vendors.vendor_id == vendor_id).first()
    if db_vendors:
        db.delete(db_vendors)
        db.commit()
    return True if db_vendors else False