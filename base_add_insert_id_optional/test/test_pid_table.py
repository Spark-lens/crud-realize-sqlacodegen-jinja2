from db_output.crud_pid_table import get_pid_table,get_pid_table_list, create_pid_table, update_pid_table, delete_pid_table
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgreRoot:hatech1618@localhost/test"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


try:
    with SessionLocal() as db:
        # row = get_pid_table(db, 1)          # 获取 mock_data 单条数据
        # row = get_pid_table_list(db, 1, 2)        # 获取 mock_data 列表
        # row = create_pid_table(db,"Maserati")     # 插入 mock_data 数据
        # row = update_pid_table(db, 3,"Masera213ti")    # 更新 mock_data 数据
        row = delete_pid_table(db, 3)    # 删除 mock_data 数据
        print(row)
except Exception as e:
    print(f"Exception: {e}")