from jinja2 import Template
from sqlalchemy import create_engine
from typing import Dict, Any

# 数据库类型字符串到Python类型的映射
TYPE_MAPPING: Dict[str, str] = {
    'BIGINT': 'int',
    'VARCHAR': 'str',
    'DATE': 'date',
    'INTEGER': 'int',
    'BYTEA': 'bytes'
}
from sqlalchemy.inspection import inspect
import argparse


def generate_crud(database_url,output_dir="./db_output/"):
    """生成CRUD操作代码

        Args:
            database_url: 数据库连接字符串。参考：postgresql+psycopg2://postgreRoot:hatech1618@localhost:5432/test
            output_dir: 输出目录

        Returns:
            None
    """

    engine = create_engine(database_url)
    inspector = inspect(engine) 

    with open("./crud_template.j2", "r", encoding="utf-8") as f:
        template = Template(f.read())


    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        # primary_key = next((c for c in columns if c['primary_key']), None)    # 报错，主键多余
        pk_constraint = inspector.get_pk_constraint(table_name)
        pk_cols = pk_constraint.get('constrained_columns', [])
        primary_key = None
        if pk_cols:
            pk_name = pk_cols[0]
            primary_key = next((c for c in columns if c['name'] == pk_name), None)

        # 获取主键的Python类型
        primary_key_type = 'Any'
        if primary_key:
            # 调试: 打印主键类型
            # 现在我们直接使用数据库返回的类型字符串
            primary_key_type_str = primary_key['type'].__class__.__name__
            print("主键类型字符串: {}".format(primary_key_type_str))
            primary_key_type = TYPE_MAPPING.get(primary_key_type_str, 'Any')
            print("映射后的类型: {}".format(primary_key_type))


        # 准备模板变量
        model_name = table_name.title().replace('_','') # 转为驼峰命名


        # 调试: 打印所有列的类型
        # for c in columns:
        #     col_type_str = c['type'].__class__.__name__
        #     mapped_type = TYPE_MAPPING.get(col_type_str, 'Any')
        #     print("列 {} 类型: {}, 映射后: {}".format(c['name'], col_type_str, mapped_type))

        params = ", ".join("{}:{}".format(c['name'], TYPE_MAPPING.get(c['type'].__class__.__name__, 'Any')) for c in columns)
        assignments = ", ".join(f"{c['name']}={c['name']}" for c in columns)
        # update_params = ", ".join(f"{c['name']}: Optional[{TYPE_MAPPING.get(type(c['type']), 'Any')}] = None" for c in columns)       # 报错
        update_params = ", ".join("{}: Optional[{}] = None".format(c['name'], TYPE_MAPPING.get(c['type'].__class__.__name__, 'Any'))
                                  for c in columns if c['name'] != pk_name)



        # 渲染模板
        output = template.render(
            table_name = table_name,
            model_name = model_name,
            columns = columns,
            primary_key = primary_key,
            primary_key_type = primary_key_type,
            params = params,
            assignments = assignments,
            update_params = update_params
        )

        # 写入文件
        with open(f"{output_dir}/crud_{table_name}.py","w",encoding="utf-8") as f:
            f.write(output)

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Generate CRUD operations for PostgreSQL tables.")
    # parser.add_argument("database_url", help="PostgreSQL database URL in the format: postgresql+psycopg2://user:password@host:port/database")
    # args = parser.parse_args()
    # generate_crud(args.database_url)

    # 示例数据库连接字符串
    database_url = "postgresql+psycopg2://postgreRoot:hatech1618@localhost:5432/test"
    generate_crud(database_url)


    # 示例调用
    # 推荐使用 psycopg2 驱动
    # python 2.generate_crud_use_template_model.py postgresql+psycopg2://postgreRoot:hatech1618@localhost:5432/test
    # python 2.generate_crud_use_template_model.py postgresql://postgreRoot:hatech1618@localhost/test