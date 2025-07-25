# CRUD operations for person
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, date
from lingzhihua_db_models.models_all_table import Person   # 导入 Person 模型，注意文件位置


# 获取单条 person 数据
def get_person(db: Session, id: int):
    result = db.query(Person).filter(Person.id == id).first()
    return result.to_dict() if result else None

# 获取 person 列表
def get_person_list(db: Session, skip: int = 0, limit: int = 100):
    person_list = db.query(Person).offset(skip).limit(limit).all()
    return [item.to_dict() for item in person_list]

# 创建 person 数据
def create_person(db: Session, id:int, first_name:str, last_name:str, gender:str, date_of_birth:date, email:str, country_of_birth:str):
    db_person = Person(id=id, first_name=first_name, last_name=last_name, gender=gender, date_of_birth=date_of_birth, email=email, country_of_birth=country_of_birth)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person.to_dict()

# 更新 person 数据
def update_person(db: Session, id: int, first_name: Optional[str] = None, last_name: Optional[str] = None, gender: Optional[str] = None, date_of_birth: Optional[date] = None, email: Optional[str] = None, country_of_birth: Optional[str] = None):
    db_person = db.query(Person).filter(Person.id == id).first()
    if db_person:
        
        if id is not None:
            db_person.id = id
        
        if first_name is not None:
            db_person.first_name = first_name
        
        if last_name is not None:
            db_person.last_name = last_name
        
        if gender is not None:
            db_person.gender = gender
        
        if date_of_birth is not None:
            db_person.date_of_birth = date_of_birth
        
        if email is not None:
            db_person.email = email
        
        if country_of_birth is not None:
            db_person.country_of_birth = country_of_birth
        
        db.commit()
        db.refresh(db_person)
    return db_person.to_dict() if db_person else None

# 删除 person 数据
def delete_person(db: Session, id: int):
    db_person = db.query(Person).filter(Person.id == id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return True if db_person else False