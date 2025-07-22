# CRUD operations for part_drawings
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, date
from db_models.models_all_table import PartDrawings   # 导入 PartDrawings 模型，注意文件位置


# 获取单条 part_drawings 数据
def get_part_drawings(db: Session, part_id: int):
    result = db.query(PartDrawings).filter(PartDrawings.part_id == part_id).first()
    return result.to_dict() if result else None

# 获取 part_drawings 列表
def get_part_drawings_list(db: Session, skip: int = 0, limit: int = 100):
    part_drawings_list = db.query(PartDrawings).offset(skip).limit(limit).all()
    return [item.to_dict() for item in part_drawings_list]

# 创建 part_drawings 数据
def create_part_drawings(db: Session, part_id:int, file_extension:str, drawing_data:bytes):
    db_part_drawings = PartDrawings(part_id=part_id, file_extension=file_extension, drawing_data=drawing_data)
    db.add(db_part_drawings)
    db.commit()
    db.refresh(db_part_drawings)
    return db_part_drawings.to_dict()

# 更新 part_drawings 数据
def update_part_drawings(db: Session, part_id: int, file_extension: Optional[str] = None, drawing_data: Optional[bytes] = None):
    db_part_drawings = db.query(PartDrawings).filter(PartDrawings.part_id == part_id).first()
    if db_part_drawings:
        
        if part_id is not None:
            db_part_drawings.part_id = part_id
        
        if file_extension is not None:
            db_part_drawings.file_extension = file_extension
        
        if drawing_data is not None:
            db_part_drawings.drawing_data = drawing_data
        
        db.commit()
        db.refresh(db_part_drawings)
    return db_part_drawings.to_dict() if db_part_drawings else None

# 删除 part_drawings 数据
def delete_part_drawings(db: Session, part_id: int):
    db_part_drawings = db.query(PartDrawings).filter(PartDrawings.part_id == part_id).first()
    if db_part_drawings:
        db.delete(db_part_drawings)
        db.commit()
    return True if db_part_drawings else False