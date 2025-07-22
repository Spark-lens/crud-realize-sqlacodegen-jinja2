# CRUD operations for pid_table
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, date
from db_models.models_all_table import PidTable   # 导入 PidTable 模型，注意文件位置


# 获取单条 pid_table 数据
def get_pid_table(db: Session, pid: int):
    result = db.query(PidTable).filter(PidTable.pid == pid).first()
    return result.to_dict() if result else None

# 获取 pid_table 列表
def get_pid_table_list(db: Session, skip: int = 0, limit: int = 100):
    pid_table_list = db.query(PidTable).offset(skip).limit(limit).all()
    return [item.to_dict() for item in pid_table_list]

# 创建 pid_table 数据
def create_pid_table(db: Session, pname:str,pid: Optional[int] = None,):
    db_pid_table = PidTable(pid=pid, pname=pname)
    db.add(db_pid_table)
    db.commit()
    db.refresh(db_pid_table)
    return db_pid_table.to_dict()

# 更新 pid_table 数据
def update_pid_table(db: Session, pid: int, pname: Optional[str] = None):
    db_pid_table = db.query(PidTable).filter(PidTable.pid == pid).first()
    if db_pid_table:
        
        if pid is not None:
            db_pid_table.pid = pid
        
        if pname is not None:
            db_pid_table.pname = pname
        
        db.commit()
        db.refresh(db_pid_table)
    return db_pid_table.to_dict() if db_pid_table else None

# 删除 pid_table 数据
def delete_pid_table(db: Session, pid: int):
    db_pid_table = db.query(PidTable).filter(PidTable.pid == pid).first()
    if db_pid_table:
        db.delete(db_pid_table)
        db.commit()
    return True if db_pid_table else False