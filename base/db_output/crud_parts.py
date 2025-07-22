# CRUD operations for parts
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, date
from db_models.models_all_table import Parts   # 导入 Parts 模型，注意文件位置


# 获取单条 parts 数据
def get_parts(db: Session, part_id: int):
    result = db.query(Parts).filter(Parts.part_id == part_id).first()
    return result.to_dict() if result else None

# 获取 parts 列表
def get_parts_list(db: Session, skip: int = 0, limit: int = 100):
    parts_list = db.query(Parts).offset(skip).limit(limit).all()
    return [item.to_dict() for item in parts_list]

# 创建 parts 数据
def create_parts(db: Session, part_id:int, part_name:str):
    db_parts = Parts(part_id=part_id, part_name=part_name)
    db.add(db_parts)
    db.commit()
    db.refresh(db_parts)
    return db_parts.to_dict()

# 更新 parts 数据
def update_parts(db: Session, part_id: int, part_name: Optional[str] = None):
    db_parts = db.query(Parts).filter(Parts.part_id == part_id).first()
    if db_parts:
        
        if part_id is not None:
            db_parts.part_id = part_id
        
        if part_name is not None:
            db_parts.part_name = part_name
        
        db.commit()
        db.refresh(db_parts)
    return db_parts.to_dict() if db_parts else None

# 删除 parts 数据
def delete_parts(db: Session, part_id: int):
    db_parts = db.query(Parts).filter(Parts.part_id == part_id).first()
    if db_parts:
        db.delete(db_parts)
        db.commit()
    return True if db_parts else False