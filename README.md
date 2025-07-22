# 使用方法

## 生成模型

运行 1.sqlcodegen_to_models.py 会连带运行 postprocess_models.py ，根据 ./db_models/base.py ，生成 PostgreSql 数据库下全部的表对应的模型

```
# 目录结构
base
│  ├─ 1.sqlcodegen_to_models.py
│  ├─ db_models
│  │  ├─ base.py
│  │  ├─ models_all_table.py
│  ├─ postprocess_models.py
```

```python
class Person(Base):
    __tablename__ = 'person'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='person_pkey'),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    gender: Mapped[str] = mapped_column(String(15))
    date_of_birth: Mapped[datetime.date] = mapped_column(Date)
    email: Mapped[Optional[str]] = mapped_column(String(150))
    country_of_birth: Mapped[Optional[str]] = mapped_column(String(50))
```

## 生成 crud 函数

运行 2.generate_crud_use_template_model.py ，使用模板 crud_template 自动生成 CRUD 代码函数，具体函数功能取决于模板内容（仓库模板包含：获取单行、获取多行、插入单行、修改单行、删除单行）

```
# 目录结构
base
│  ├─ 1.sqlcodegen_to_models.py
│  ├─ 2.generate_crud_use_template_model.py
│  ├─ crud_template.j2
│  ├─ db_models
│  │  ├─ base.py
│  │  ├─ models_all_table.py
│  ├─ db_output
│  │  ├─ crud_person.py
│  ├─ postprocess_models.py
```

base_add_insert_id_optional模板 与 base模板差别在于 插入单行 可以不指定 主键

 base模板

```jinja2
# Jinja2 模板
# 创建 {{ table_name }} 数据
def create_{{ table_name }}(db: Session, {{ params }}):
    db_{{ table_name }} = {{ model_name }}({{ assignments }})
    db.add(db_{{ table_name }})
    db.commit()
    db.refresh(db_{{ table_name }})
    return db_{{ table_name }}.to_dict()
```

```python
# python函数
# 插入 person 数据
def create_person(db: Session, id:int, first_name:str, last_name:str, gender:str, date_of_birth:date, email:str, country_of_birth:str):
    db_person = Person(id=id, first_name=first_name, last_name=last_name, gender=gender, date_of_birth=date_of_birth, email=email, country_of_birth=country_of_birth)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person.to_dict()
```

base_add_insert_id_optional模板

```jinja2
# Jinja2 模板
# 创建 {{ table_name }} 数据
def create_{{ table_name }}(db: Session, {{ non_primary_params }},{{ primary_key.name }}: Optional[{{ primary_key_type }}] = None,):
    db_{{ table_name }} = {{ model_name }}({{ assignments }})
    db.add(db_{{ table_name }})
    db.commit()
    db.refresh(db_{{ table_name }})
    return db_{{ table_name }}.to_dict()
```

```python
# python函数
# 插入 person 数据
def create_person(db: Session, first_name:str, last_name:str, gender:str, date_of_birth:date, email:str, country_of_birth:str,id: Optional[int] = None,):
    db_person = Person(id=id, first_name=first_name, last_name=last_name, gender=gender, date_of_birth=date_of_birth, email=email, country_of_birth=country_of_birth)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person.to_dict()
```