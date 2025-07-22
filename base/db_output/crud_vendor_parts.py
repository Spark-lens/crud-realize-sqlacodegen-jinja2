# CRUD operations for vendor_parts
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, date
from db_models.models_all_table import VendorParts   # 导入 VendorParts 模型，注意文件位置


# 获取单条 vendor_parts 数据
def get_vendor_parts(db: Session, vendor_id: int):
    result = db.query(VendorParts).filter(VendorParts.vendor_id == vendor_id).first()
    return result.to_dict() if result else None

# 获取 vendor_parts 列表
def get_vendor_parts_list(db: Session, skip: int = 0, limit: int = 100):
    vendor_parts_list = db.query(VendorParts).offset(skip).limit(limit).all()
    return [item.to_dict() for item in vendor_parts_list]

# 创建 vendor_parts 数据
def create_vendor_parts(db: Session, vendor_id:int, part_id:int):
    db_vendor_parts = VendorParts(vendor_id=vendor_id, part_id=part_id)
    db.add(db_vendor_parts)
    db.commit()
    db.refresh(db_vendor_parts)
    return db_vendor_parts.to_dict()

# 更新 vendor_parts 数据
def update_vendor_parts(db: Session, vendor_id: int, part_id: Optional[int] = None):
    db_vendor_parts = db.query(VendorParts).filter(VendorParts.vendor_id == vendor_id).first()
    if db_vendor_parts:
        
        if vendor_id is not None:
            db_vendor_parts.vendor_id = vendor_id
        
        if part_id is not None:
            db_vendor_parts.part_id = part_id
        
        db.commit()
        db.refresh(db_vendor_parts)
    return db_vendor_parts.to_dict() if db_vendor_parts else None

# 删除 vendor_parts 数据
def delete_vendor_parts(db: Session, vendor_id: int):
    db_vendor_parts = db.query(VendorParts).filter(VendorParts.vendor_id == vendor_id).first()
    if db_vendor_parts:
        db.delete(db_vendor_parts)
        db.commit()
    return True if db_vendor_parts else False