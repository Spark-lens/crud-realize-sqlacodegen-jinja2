# 详细诊断导入问题
import sys
import os

# 打印当前Python路径
print("当前Python路径:")
for path in sys.path:
    print(f"  {path}")

# 尝试添加项目根目录到Python路径
project_root = os.path.abspath('.')
sys.path.append(project_root)
print(f"添加项目根目录到Python路径: {project_root}")

# 检查db_output目录是否存在
print(f"检查目录是否存在: {os.path.join(project_root, 'db_output')}")
if os.path.exists(os.path.join(project_root, 'db_output')):
    print("  目录存在!")
else:
    print("  目录不存在!")

# 检查db_output目录是否包含__init__.py文件
print(f"检查文件是否存在: {os.path.join(project_root, 'db_output', '__init__.py')}")
if os.path.exists(os.path.join(project_root, 'db_output', '__init__.py')):
    print("  文件存在!")
else:
    print("  文件不存在!")

# 尝试导入db_output模块
try:
    # 尝试导入db_output模块
    import db_output
    print("成功导入db_output模块!")
    # 尝试导入crud_person
    from db_output import crud_person
    print("成功导入db_output.crud_person模块!")
    # 尝试导入get_person函数
    from db_output.crud_person import get_person
    print("成功导入get_person函数!")
except ImportError as e:
    print(f"导入失败: {e}")
    # 打印错误堆栈
    import traceback
    traceback.print_exc()