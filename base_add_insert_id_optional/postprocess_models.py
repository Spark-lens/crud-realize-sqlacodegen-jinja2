import sys

def postprocess_model_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换基类导入
    content = content.replace('from sqlalchemy.orm import DeclarativeBase', 'from db_models.base import Base')
    # 移除默认Base类定义
    content = content.replace('class Base(DeclarativeBase):\n    pass\n\n', '')
    # 确保所有模型类继承自定义Base
    content = content.replace('(DeclarativeBase)', '(Base)')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python postprocess_models.py <model_file_path>")
        sys.exit(1)
    postprocess_model_file(sys.argv[1])