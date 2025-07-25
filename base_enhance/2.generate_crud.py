from jinja2 import Template
from sqlalchemy import create_engine
from sqlalchemy.inspection import inspect
import argparse
# 新增需要的导入，根据实际模板用到的模块补充
from typing import List, Optional, Dict, Any, Union
from sqlalchemy import func, text
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


def map_db_type_to_python(db_type):
    """将数据库类型映射为 Python 类型"""
    type_name = db_type.__class__.__name__.upper()

    if type_name in ['CHAR', 'VARCHAR', 'TEXT', 'STRING']:
        return 'str'
    elif type_name in ['INTEGER', 'BIGINT', 'SMALLINT']:
        return 'int'
    elif type_name in ['NUMERIC', 'DECIMAL', 'FLOAT', 'REAL']:
        return 'float'
    elif type_name in ['BOOLEAN']:
        return 'bool'
    elif type_name in ['TIMESTAMP', 'DATETIME', 'DATE', 'TIME']:
        return 'datetime'
    else:
        return 'str'  # 默认为字符串类型


def generate_crud(database_url, output_dir="./models"):
    engine = create_engine(database_url)
    inspector = inspect(engine)

    with open("crud_template.j2", encoding="utf-8") as f:
        template = Template(f.read())

    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)

        # 获取主键信息（使用主键约束，更可靠）
        pk_constraint = inspector.get_pk_constraint(table_name)

        # 优先使用主键约束信息
        if pk_constraint and pk_constraint.get('constrained_columns'):
            pk_column_name = pk_constraint['constrained_columns'][0]
            primary_key = next((c for c in columns if c['name'] == pk_column_name), None)
            if not primary_key:
                print(f"警告: 表 '{table_name}' 主键列 '{pk_column_name}' 在列定义中未找到")
        else:
            # 备用方法：检查列的 primary_key 属性
            primary_key = next((c for c in columns if c.get('primary_key') is True), None)
            if not primary_key:
                print(f"警告: 表 '{table_name}' 没有定义主键约束")

        # 如果没有找到主键，使用第一列作为替代
        if not primary_key and columns:
            primary_key = columns[0]
            print(f"警告: 表 '{table_name}' 没有定义主键，使用第一列 '{primary_key['name']}' 作为替代")
        elif not primary_key:
            print(f"错误: 表 '{table_name}' 没有可用的列，跳过生成")
            continue

        # 处理空表的情况
        if not columns:
            print(f"错误: 表 '{table_name}' 没有列定义，跳过生成")
            continue

        model_name = table_name.title().replace('_', '')

        # 为每列和主键添加 Python 类型映射
        for column in columns:
            column['python_type'] = map_db_type_to_python(column['type'])

        primary_key['python_type'] = map_db_type_to_python(primary_key['type'])

        # 使用正确的类型注解
        params = ", ".join(f"{c['name']}: {c['python_type']}" for c in columns)
        assignments = ", ".join(f"{c['name']}={c['name']}" for c in columns)

        # 排除主键，避免重复参数
        update_params = ", ".join(
            f"{c['name']}: Optional[{c['python_type']}] = None" for c in columns if c['name'] != primary_key['name'])

        # 构造 imports 变量，根据模板实际需要的导入调整
        imports = {
            "typing": ["List", "Optional", "Dict", "Any", "Union"],
            "sqlalchemy": ["func", "text"],
            "sqlalchemy.orm": ["Session"],
            "sqlalchemy.exc": ["IntegrityError"],
            "datetime": ["datetime"]  # 添加 datetime 模块
        }

        output = template.render(
            table_name=table_name,
            model_name=model_name,
            columns=columns,
            primary_key=primary_key,
            params=params,
            assignments=assignments,
            update_params=update_params,
            imports=imports  # 传入 imports 变量
        )

        with open(f"{output_dir}/crud_{table_name}.py", "w", encoding="utf-8") as f:
            f.write(output)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Generate CRUD operations from database")
    # parser.add_argument("database_url", help="Database connection URL")
    # args = parser.parse_args()
    # generate_crud(args.database_url)

    database_url = "postgresql+psycopg2://postgreRoot:hatech1618@10.1.140.170:5432/istorm_aiagent"
    generate_crud(database_url, output_dir="./models")
