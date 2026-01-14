"""代码执行器测试示例

演示AICodeExecutor的各种使用场景。
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from codebox import AICodeExecutor


def test_simple_execution():
    """测试1: 简单的Python代码执行"""
    print("=" * 60)
    print("测试1: 简单的Python代码执行")
    print("=" * 60)
    
    executor = AICodeExecutor()
    
    result = executor.execute("""
result = 2 + 3
print("计算完成")
result * 10
    """)
    
    print_result(result)


def test_with_variables():
    """测试2: 使用变量注入"""
    print("\n" + "=" * 60)
    print("测试2: 使用变量注入")
    print("=" * 60)
    
    executor = AICodeExecutor()
    
    result = executor.execute(
        code="""
result = data['a'] + data['b']
print(f"计算结果: {result}")
result
        """,
        variables={"data": {"a": 10, "b": 20}}
    )
    
    print_result(result)


def test_excel_reading():
    """测试3: 读取Excel文件"""
    print("\n" + "=" * 60)
    print("测试3: 读取Excel文件")
    print("=" * 60)
    
    executor = AICodeExecutor()
    
    result = executor.execute("""
import pandas as pd

df = pd.read_excel('D:\\\\Code\\\\DataAgent\\\\ExcelData\\\\Covid Dashboard.xlsx', sheet_name='Sheet1')
print(f"成功读取 {len(df)} 行数据")
print(f"列名: {list(df.columns)}")

df.head(3)
    """)
    
    print_result(result)


def test_error_handling():
    """测试4: 错误处理"""
    print("\n" + "=" * 60)
    print("测试4: 错误处理")
    print("=" * 60)
    
    executor = AICodeExecutor()
    
    result = executor.execute("""
x = 1 / 0
    """)
    
    print_result(result)


def test_syntax_error():
    """测试5: 语法错误"""
    print("\n" + "=" * 60)
    print("测试5: 语法错误")
    print("=" * 60)
    
    executor = AICodeExecutor()
    
    result = executor.execute("""
if True
    print("缺少冒号")
    """)
    
    print_result(result)


def test_forbidden_import():
    """测试6: 禁止的模块导入"""
    print("\n" + "=" * 60)
    print("测试6: 禁止的模块导入")
    print("=" * 60)
    
    executor = AICodeExecutor()
    
    result = executor.execute("""
import os
print("这个不应该执行")
    """)
    
    print_result(result)


def test_multiple_statements():
    """测试7: 多语句执行"""
    print("\n" + "=" * 60)
    print("测试7: 多语句执行")
    print("=" * 60)
    
    executor = AICodeExecutor()
    
    result = executor.execute("""
numbers = [1, 2, 3, 4, 5]
print(f"原始列表: {numbers}")

squared = [x**2 for x in numbers]
print(f"平方后: {squared}")

total = sum(squared)
print(f"总和: {total}")

total
    """)
    
    print_result(result)


def test_math_operations():
    """测试8: 数学运算"""
    print("\n" + "=" * 60)
    print("测试8: 数学运算")
    print("=" * 60)
    
    executor = AICodeExecutor()
    
    result = executor.execute("""
import math

x = math.pi
print(f"π = {x}")

y = math.sin(math.pi / 2)
print(f"sin(π/2) = {y}")

z = math.sqrt(16)
print(f"√16 = {z}")

[x, y, z]
    """)
    
    print_result(result)


def test_string_operations():
    """测试9: 字符串操作"""
    print("\n" + "=" * 60)
    print("测试9: 字符串操作")
    print("=" * 60)
    
    executor = AICodeExecutor()
    
    result = executor.execute("""
import re

text = "Hello, World! 123"
print(f"原始文本: {text}")

words = text.split()
print(f"分割结果: {words}")

numbers = re.findall(r'\\d+', text)
print(f"提取数字: {numbers}")

result = text.replace("World", "Python")
print(f"替换后: {result}")

result
    """)
    
    print_result(result)


def print_result(result):
    """打印执行结果的辅助函数"""
    if result["success"]:
        print("[SUCCESS] 执行成功")
        if result["output"] is not None:
            print(f"返回值: {result['output']}")
        if result["logs"]:
            print(f"日志:\n{result['logs']}")
        if result["is_final_answer"]:
            print("[INFO] 调用了 final_answer")
    else:
        print("[FAILED] 执行失败")
        print(f"错误信息: {result['error']}")


def main():
    """运行所有测试"""
    print("\n" + "=" * 60)
    print("AI代码执行器测试套件")
    print("=" * 60)
    
    tests = [
        test_simple_execution,
        test_with_variables,
        test_excel_reading,
        test_error_handling,
        test_syntax_error,
        test_forbidden_import,
        test_multiple_statements,
        test_math_operations,
        test_string_operations,
    ]
    
    for test in tests:
        try:
            test()
        except Exception as e:
            print(f"\n[ERROR] 测试 '{test.__name__}' 发生异常: {e}")
    
    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
