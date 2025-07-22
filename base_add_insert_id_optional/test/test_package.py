# 测试导入db_output包
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.abspath('.'))

try:
    # 尝试导入db_output模块
    from db_output.crud_person import get_person
    print("成功导入db_output模块!")
except ImportError as e:
    print(f"导入失败: {e}")