# 在 crud_template.j2 顶部添加

from typing import List, Optional, Dict, Any, Union

from sqlalchemy import func, text

from sqlalchemy.orm import Session

from sqlalchemy.exc import IntegrityError

from datetime import datetime


# CRUD operations for t_dict_large_model
from sqlalchemy.orm import Session
from sqlalchemy import func, text
from sqlalchemy.exc import IntegrityError
from typing import List, Optional, Dict, Any, Union
from datetime import datetime
from .db_models import TDictLargeModel

# 基础 CRUD 操作
def get_t_dict_large_model(db: Session, id: str):
    return db.query(TDictLargeModel).filter(TDictLargeModel.id == id).first()

def get_t_dict_large_model_list(
    db: Session, 
    skip: int = 0, 
    limit: int = 100, 
    order_by: Optional[str] = None, 
    desc: bool = False,
    filters: Optional[Dict[str, Any]] = None
):
    query = db.query(TDictLargeModel)
    
    # 应用过滤条件
    if filters:
        for field, value in filters.items():
            if hasattr(TDictLargeModel, field):
                query = query.filter(getattr(TDictLargeModel, field) == value)
    
    # 应用排序
    if order_by and hasattr(TDictLargeModel, order_by):
        if desc:
            query = query.order_by(getattr(TDictLargeModel, order_by).desc())
        else:
            query = query.order_by(getattr(TDictLargeModel, order_by))
    
    return query.offset(skip).limit(limit).all()

def create_t_dict_large_model(db: Session, id: str, base_url: str, api_key: str, model_name: str, app_id: str, create_user_id: str, create_time: datetime, edit_user_id: str, edit_time: datetime, is_deleted: str):
    db_t_dict_large_model = TDictLargeModel(id=id, base_url=base_url, api_key=api_key, model_name=model_name, app_id=app_id, create_user_id=create_user_id, create_time=create_time, edit_user_id=edit_user_id, edit_time=edit_time, is_deleted=is_deleted)
    db.add(db_t_dict_large_model)
    try:
        db.commit()
        db.refresh(db_t_dict_large_model)
        return db_t_dict_large_model
    except IntegrityError:
        db.rollback()
        raise

def update_t_dict_large_model(
    db: Session, 
    id: str,
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    model_name: Optional[str] = None,
    app_id: Optional[str] = None,
    create_user_id: Optional[str] = None,
    create_time: Optional[datetime] = None,
    edit_user_id: Optional[str] = None,
    edit_time: Optional[datetime] = None,
    is_deleted: Optional[str] = None,
):
    db_t_dict_large_model = db.query(TDictLargeModel).filter(TDictLargeModel.id == id).first()
    if db_t_dict_large_model:
        update_data = {
            'base_url': base_url,
            'api_key': api_key,
            'model_name': model_name,
            'app_id': app_id,
            'create_user_id': create_user_id,
            'create_time': create_time,
            'edit_user_id': edit_user_id,
            'edit_time': edit_time,
            'is_deleted': is_deleted,
        }
        update_data = {k: v for k, v in update_data.items() if v is not None}
        
        for key, value in update_data.items():
            setattr(db_t_dict_large_model, key, value)
            
        db.commit()
        db.refresh(db_t_dict_large_model)
    return db_t_dict_large_model

def delete_t_dict_large_model(db: Session, id: str):
    db_t_dict_large_model = db.query(TDictLargeModel).filter(TDictLargeModel.id == id).first()
    if db_t_dict_large_model:
        db.delete(db_t_dict_large_model)
        db.commit()
        return True
    return False

# 增强型查询操作
def get_t_dict_large_model_by_fields(
    db: Session, 
    fields: Dict[str, Any], 
    limit: int = 1
) -> Optional[TDictLargeModel]:
    """根据多个字段查询单条记录"""
    query = db.query(TDictLargeModel)
    for field, value in fields.items():
        if hasattr(TDictLargeModel, field):
            query = query.filter(getattr(TDictLargeModel, field) == value)
    return query.limit(limit).all()

def get_t_dict_large_model_paginated(
    db: Session,
    page: int = 1,
    page_size: int = 20,
    order_by: Optional[str] = None,
    desc: bool = False,
    filters: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """分页查询，返回结果和总数"""
    query = db.query(TDictLargeModel)
    
    # 应用过滤条件
    if filters:
        for field, value in filters.items():
            if hasattr(TDictLargeModel, field):
                query = query.filter(getattr(TDictLargeModel, field) == value)
    
    # 应用排序
    if order_by and hasattr(TDictLargeModel, order_by):
        if desc:
            query = query.order_by(getattr(TDictLargeModel, order_by).desc())
        else:
            query = query.order_by(getattr(TDictLargeModel, order_by))
    
    total = query.count()
    results = query.offset((page - 1) * page_size).limit(page_size).all()
    
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "results": results
    }

def execute_raw_sql(
    db: Session,
    sql: str,
    params: Optional[Dict[str, Any]] = None
) -> List[Dict[str, Any]]:
    """执行原生SQL查询"""
    result = db.execute(text(sql), params)
    # 修复：正确转换每行结果为字典
    return [dict(row._mapping) for row in result]

def bulk_create_t_dict_large_model(
    db: Session,
    items: List[Dict[str, Any]]
) -> List[TDictLargeModel]:
    """批量创建记录"""
    db_items = [TDictLargeModel(**item) for item in items]
    db.add_all(db_items)
    db.commit()
    return db_items

def bulk_update_t_dict_large_model(
    db: Session,
    items: List[Dict[str, Any]]
) -> int:
    """批量更新记录，每个项目必须包含主键"""
    updated_count = 0
    for item in items:
        primary_value = item.get('id')
        if primary_value:
            db_item = db.query(TDictLargeModel).filter(
                TDictLargeModel.id == primary_value
            ).first()
            if db_item:
                for key, value in item.items():
                    if hasattr(db_item, key) and key != 'id':
                        setattr(db_item, key, value)
                updated_count += 1
    db.commit()
    return updated_count

def count_t_dict_large_model(db: Session, filters: Optional[Dict[str, Any]] = None) -> int:
    """统计记录数量"""
    query = db.query(TDictLargeModel)
    if filters:
        for field, value in filters.items():
            if hasattr(TDictLargeModel, field):
                query = query.filter(getattr(TDictLargeModel, field) == value)
    return query.count()

def group_by_and_aggregate(
    db: Session,
    group_by_field: str,
    aggregate_field: str,
    aggregate_func: str = "count",  # count, sum, avg, min, max
    filters: Optional[Dict[str, Any]] = None
) -> List[Dict[str, Any]]:
    """分组聚合查询"""
    if not hasattr(TDictLargeModel, group_by_field) or not hasattr(TDictLargeModel, aggregate_field):
        return []
    
    func_map = {
        "count": func.count,
        "sum": func.sum,
        "avg": func.avg,
        "min": func.min,
        "max": func.max
    }
    
    aggregate_func = func_map.get(aggregate_func, func.count)
    
    query = db.query(
        getattr(TDictLargeModel, group_by_field),
        aggregate_func(getattr(TDictLargeModel, aggregate_field)).label("aggregated_value")
    ).group_by(getattr(TDictLargeModel, group_by_field))
    
    if filters:
        for field, value in filters.items():
            if hasattr(TDictLargeModel, field):
                query = query.filter(getattr(TDictLargeModel, field) == value)
    
    return [{"group": row[0], "value": row[1]} for row in query.all()]