from db_output.crud_vendor_parts import get_vendor_parts, get_vendor_parts_list, create_vendor_parts, update_vendor_parts, delete_vendor_parts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgreRoot:hatech1618@localhost/test"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


try:
    with SessionLocal() as db:
        row = get_vendor_parts(db, 1)          # 获取 mock_data 单条数据
        # row = get_vendor_parts_list(db, 1, 2)        # 获取 mock_data 列表
        # row = create_vendor_parts(db, 1003,1)     # 插入 mock_data 数据
        # row = update_vendor_parts(db, 1003,2)    # 更新 mock_data 数据
        # row = delete_vendor_parts(db, 1003)    # 删除 mock_data 数据
        print(row)
except Exception as e:
    print(f"Exception: {e}")