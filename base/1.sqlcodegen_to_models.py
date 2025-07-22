# python 自动 curd

# sqlacodegen 生成模型
# 数据库 postgreSql
# sqlacodegen shell 命令
# 数据库指定表输出，下面两条等效
# sqlacodegen --tables mock_data --outfile ./db_output/output.py postgresql+psycopg2://postgreRoot:hatech1618@localhost:5432/test
# sqlacodegen --tables mock_data postgresql+psycopg2://postgreRoot:hatech1618@localhost:5432/test > ./db_model/models2.py
# 数据库所有表全部输出
# sqlacodegen postgresql+psycopg2://postgreRoot:hatech1618@localhost:5432/test > ./db_model/models.py
# sqlacodegen postgresql://postgreRoot:hatech1618@localhost:5432/test > ./db_model/models.py



# sqlacodegen + 自定义模版


import subprocess

def generate_specific_table():
    """生成指定表的模型文件并自动应用后处理"""
    # 生成原始模型文件
    subprocess.run([
        "sqlacodegen",
        "--generator", "declarative",
        # "--tables", "parts",  # 只生成 parts 表
        # "--tables", "mock_data,parts,vendors",  # 指定多个表
        "--tables", "vendor_parts",  # 生成 vendor_parts 中间表，连带生成 vendors、parts表
        "postgresql+psycopg2://postgreRoot:hatech1618@localhost:5432/test"
    ], stdout=open("./db_models/models_specific_table.py", "w", encoding="utf-8"))
    # 运行后处理脚本替换基类
    subprocess.run([
        "python", "postprocess_models.py", "./db_models/models_specific_table.py"
    ], check=True)

def generate_all_tables():
    """生成所有表的模型文件并自动应用后处理"""
    # 生成原始模型文件
    subprocess.run([
        "sqlacodegen",
        "--generator", "declarative",
        "postgresql+psycopg2://postgreRoot:hatech1618@localhost:5432/test"
    ], stdout=open("./db_models/models_all_table.py", "w", encoding="utf-8"))
    # 运行后处理脚本替换基类
    subprocess.run([
        "python", "postprocess_models.py", "./db_models/models_all_table.py"
    ], check=True)

if __name__ == "__main__":
    # 生成指定表的模型文件
    # generate_specific_table()
    # 生成所有表的模型文件
    generate_all_tables()