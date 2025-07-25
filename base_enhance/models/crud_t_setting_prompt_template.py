# 在 crud_template.j2 顶部添加

from typing import List, Optional, Dict, Any, Union

from sqlalchemy import func, text

from sqlalchemy.orm import Session

from sqlalchemy.exc import IntegrityError

from datetime import datetime


# CRUD operations for t_setting_prompt_template
from sqlalchemy.orm import Session
from sqlalchemy import func, text
from sqlalchemy.exc import IntegrityError
from typing import List, Optional, Dict, Any, Union
from datetime import datetime
from .db_models import TSettingPromptTemplate

# 基础 CRUD 操作
def get_t_setting_prompt_template(db: Session, id: str):
    return db.query(TSettingPromptTemplate).filter(TSettingPromptTemplate.id == id).first()

def get_t_setting_prompt_template_list(
    db: Session, 
    skip: int = 0, 
    limit: int = 100, 
    order_by: Optional[str] = None, 
    desc: bool = False,
    filters: Optional[Dict[str, Any]] = None
):
    query = db.query(TSettingPromptTemplate)
    
    # 应用过滤条件
    if filters:
        for field, value in filters.items():
            if hasattr(TSettingPromptTemplate, field):
                query = query.filter(getattr(TSettingPromptTemplate, field) == value)
    
    # 应用排序
    if order_by and hasattr(TSettingPromptTemplate, order_by):
        if desc:
            query = query.order_by(getattr(TSettingPromptTemplate, order_by).desc())
        else:
            query = query.order_by(getattr(TSettingPromptTemplate, order_by))
    
    return query.offset(skip).limit(limit).all()

def create_t_setting_prompt_template(db: Session, id: str, app_id: str, submit_user_id: str, submit_time: datetime, trainer: str, prompt_type: str, template_name: str, template_content: str, tag_id: str, create_user_id: str, create_time: datetime, edit_user_id: str, edit_time: datetime, is_deleted: str):
    db_t_setting_prompt_template = TSettingPromptTemplate(id=id, app_id=app_id, submit_user_id=submit_user_id, submit_time=submit_time, trainer=trainer, prompt_type=prompt_type, template_name=template_name, template_content=template_content, tag_id=tag_id, create_user_id=create_user_id, create_time=create_time, edit_user_id=edit_user_id, edit_time=edit_time, is_deleted=is_deleted)
    db.add(db_t_setting_prompt_template)
    try:
        db.commit()
        db.refresh(db_t_setting_prompt_template)
        return db_t_setting_prompt_template
    except IntegrityError:
        db.rollback()
        raise

def update_t_setting_prompt_template(
    db: Session, 
    id: str,
    app_id: Optional[str] = None,
    submit_user_id: Optional[str] = None,
    submit_time: Optional[datetime] = None,
    trainer: Optional[str] = None,
    prompt_type: Optional[str] = None,
    template_name: Optional[str] = None,
    template_content: Optional[str] = None,
    tag_id: Optional[str] = None,
    create_user_id: Optional[str] = None,
    create_time: Optional[datetime] = None,
    edit_user_id: Optional[str] = None,
    edit_time: Optional[datetime] = None,
    is_deleted: Optional[str] = None,
):
    db_t_setting_prompt_template = db.query(TSettingPromptTemplate).filter(TSettingPromptTemplate.id == id).first()
    if db_t_setting_prompt_template:
        update_data = {
            'app_id': app_id,
            'submit_user_id': submit_user_id,
            'submit_time': submit_time,
            'trainer': trainer,
            'prompt_type': prompt_type,
            'template_name': template_name,
            'template_content': template_content,
            'tag_id': tag_id,
            'create_user_id': create_user_id,
            'create_time': create_time,
            'edit_user_id': edit_user_id,
            'edit_time': edit_time,
            'is_deleted': is_deleted,
        }
        update_data = {k: v for k, v in update_data.items() if v is not None}
        
        for key, value in update_data.items():
            setattr(db_t_setting_prompt_template, key, value)
            
        db.commit()
        db.refresh(db_t_setting_prompt_template)
    return db_t_setting_prompt_template

def delete_t_setting_prompt_template(db: Session, id: str):
    db_t_setting_prompt_template = db.query(TSettingPromptTemplate).filter(TSettingPromptTemplate.id == id).first()
    if db_t_setting_prompt_template:
        db.delete(db_t_setting_prompt_template)
        db.commit()
        return True
    return False

# 增强型查询操作
def get_t_setting_prompt_template_by_fields(
    db: Session, 
    fields: Dict[str, Any], 
    limit: int = 1
) -> Optional[TSettingPromptTemplate]:
    """根据多个字段查询单条记录"""
    query = db.query(TSettingPromptTemplate)
    for field, value in fields.items():
        if hasattr(TSettingPromptTemplate, field):
            query = query.filter(getattr(TSettingPromptTemplate, field) == value)
    return query.limit(limit).all()

def get_t_setting_prompt_template_paginated(
    db: Session,
    page: int = 1,
    page_size: int = 20,
    order_by: Optional[str] = None,
    desc: bool = False,
    filters: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """分页查询，返回结果和总数"""
    query = db.query(TSettingPromptTemplate)
    
    # 应用过滤条件
    if filters:
        for field, value in filters.items():
            if hasattr(TSettingPromptTemplate, field):
                query = query.filter(getattr(TSettingPromptTemplate, field) == value)
    
    # 应用排序
    if order_by and hasattr(TSettingPromptTemplate, order_by):
        if desc:
            query = query.order_by(getattr(TSettingPromptTemplate, order_by).desc())
        else:
            query = query.order_by(getattr(TSettingPromptTemplate, order_by))
    
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

def bulk_create_t_setting_prompt_template(
    db: Session,
    items: List[Dict[str, Any]]
) -> List[TSettingPromptTemplate]:
    """批量创建记录"""
    db_items = [TSettingPromptTemplate(**item) for item in items]
    db.add_all(db_items)
    db.commit()
    return db_items

def bulk_update_t_setting_prompt_template(
    db: Session,
    items: List[Dict[str, Any]]
) -> int:
    """批量更新记录，每个项目必须包含主键"""
    updated_count = 0
    for item in items:
        primary_value = item.get('id')
        if primary_value:
            db_item = db.query(TSettingPromptTemplate).filter(
                TSettingPromptTemplate.id == primary_value
            ).first()
            if db_item:
                for key, value in item.items():
                    if hasattr(db_item, key) and key != 'id':
                        setattr(db_item, key, value)
                updated_count += 1
    db.commit()
    return updated_count

def count_t_setting_prompt_template(db: Session, filters: Optional[Dict[str, Any]] = None) -> int:
    """统计记录数量"""
    query = db.query(TSettingPromptTemplate)
    if filters:
        for field, value in filters.items():
            if hasattr(TSettingPromptTemplate, field):
                query = query.filter(getattr(TSettingPromptTemplate, field) == value)
    return query.count()

def group_by_and_aggregate(
    db: Session,
    group_by_field: str,
    aggregate_field: str,
    aggregate_func: str = "count",  # count, sum, avg, min, max
    filters: Optional[Dict[str, Any]] = None
) -> List[Dict[str, Any]]:
    """分组聚合查询"""
    if not hasattr(TSettingPromptTemplate, group_by_field) or not hasattr(TSettingPromptTemplate, aggregate_field):
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
        getattr(TSettingPromptTemplate, group_by_field),
        aggregate_func(getattr(TSettingPromptTemplate, aggregate_field)).label("aggregated_value")
    ).group_by(getattr(TSettingPromptTemplate, group_by_field))
    
    if filters:
        for field, value in filters.items():
            if hasattr(TSettingPromptTemplate, field):
                query = query.filter(getattr(TSettingPromptTemplate, field) == value)
    
    return [{"group": row[0], "value": row[1]} for row in query.all()]