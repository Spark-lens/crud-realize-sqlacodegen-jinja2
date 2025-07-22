from db_output.crud_parts import get_parts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgreRoot:hatech1618@localhost/test"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


try:
    with SessionLocal() as db:
        row = get_parts(db, 1)        # 获取 mock_data 列表
        # row = get_mock_data(db, 1)          # 获取 mock_data 单条数据
        # row = create_mock_data(db, 1003,"Maserati","S11","109578.78")     # 插入 mock_data 数据
        # row = update_mock_data(db, 1003,"Masera213ti","S21","109578.78")    # 更新 mock_data 数据
        # row = delete_mock_data(db, 1003)    # 删除 mock_data 数据
        print(row)
except Exception as e:
    print(f"Exception: {e}")