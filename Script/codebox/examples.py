"""Codebox使用示例

演示AICodeExecutor在实际项目中的应用场景。
"""

from Script.codebox import AICodeExecutor


def example_1_basic_usage():
    """示例1: 基本用法 - 简单计算"""
    print("=" * 60)
    print("示例1: 基本用法")
    print("=" * 60)

    executor = AICodeExecutor()

    code = """
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
sum_squared = sum(squared)

print(f"原始列表: {numbers}")
print(f"平方结果: {squared}")
print(f"平方和: {sum_squared}")

sum_squared
    """

    result = executor.execute(code)

    if result["success"]:
        print(f"\n计算结果: {result['output']}")
    else:
        print(f"\n执行失败: {result['error']}")


def example_2_excel_analysis():
    """示例2: Excel数据分析"""
    print("\n" + "=" * 60)
    print("示例2: Excel数据分析")
    print("=" * 60)

    executor = AICodeExecutor()

    code = """
import pandas as pd

# 读取Excel文件
file_path = 'D:\\\\Code\\\\DataAgent\\\\ExcelData\\\\Covid Dashboard.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

print(f"数据形状: {df.shape}")
print(f"列名: {list(df.columns)[:5]}...")  # 只显示前5个

# 获取前3行数据
head_3 = df.head(3)

# 计算基本统计信息
print(f"数据行数: {len(df)}")
print(f"数据列数: {len(df.columns)}")

head_3
    """

    result = executor.execute(code)

    if result["success"]:
        print(f"\n数据预览:\n{result['output']}")
    else:
        print(f"\n执行失败: {result['error']}")


def example_3_with_variables():
    """示例3: 使用变量注入"""
    print("\n" + "=" * 60)
    print("示例3: 使用变量注入")
    print("=" * 60)

    executor = AICodeExecutor()

    # 定义要注入的变量
    variables = {"data": [10, 20, 30, 40, 50], "threshold": 25, "column_name": "values"}

    code = """
import statistics

# 计算基本统计信息
mean = statistics.mean(data)
median = statistics.median(data)
std_dev = statistics.stdev(data)

print(f"{column_name} 统计信息:")
print(f"平均值: {mean:.2f}")
print(f"中位数: {median}")
print(f"标准差: {std_dev:.2f}")

# 筛选大于阈值的数据
filtered = [x for x in data if x > threshold]
print(f"大于 {threshold} 的值: {filtered}")

{
    "mean": mean,
    "median": median,
    "std_dev": std_dev,
    "filtered": filtered,
    "count_above_threshold": len(filtered)
}
    """

    result = executor.execute(code, variables=variables)

    if result["success"]:
        print(f"\n分析结果: {result['output']}")
    else:
        print(f"\n执行失败: {result['error']}")


def example_4_string_processing():
    """示例4: 字符串处理"""
    print("\n" + "=" * 60)
    print("示例4: 字符串处理")
    print("=" * 60)

    executor = AICodeExecutor()

    code = '''
import re

text = """Hello World 123
Python Programming 456
Data Analysis 789
Machine Learning 12"""

# 提取所有数字
numbers = re.findall(r'\\d+', text)
numbers = [int(n) for n in numbers]
print(f"提取的数字: {numbers}")

# 提取所有单词（不包含数字）
words = re.findall(r'[a-zA-Z]+', text)
print(f"提取的单词: {words[:10]}...")

# 计算数字总和
total = sum(numbers)
print(f"数字总和: {total}")

# 统计单词长度分布
word_lengths = [len(word) for word in words]
avg_length = sum(word_lengths) / len(word_lengths)
print(f"平均单词长度: {avg_length:.2f}")

{
    "numbers": numbers,
    "total": total,
    "word_count": len(words),
    "avg_word_length": avg_length
}
    '''

    result = executor.execute(code)

    if result["success"]:
        print(f"\n处理结果: {result['output']}")
    else:
        print(f"\n执行失败: {result['error']}")


def example_5_data_transformation():
    """示例5: 数据转换"""
    print("\n" + "=" * 60)
    print("示例5: 数据转换")
    print("=" * 60)

    executor = AICodeExecutor()

    code = """
import pandas as pd

# 创建示例DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 28, 32],
    "City": ["New York", "London", "Paris", "Tokyo", "Sydney"]
}

df = pd.DataFrame(data)
print("原始数据:")
print(df)

# 数据转换
df["Age_Group"] = pd.cut(df["Age"], bins=[0, 30, 35, 100], labels=["Young", "Middle", "Senior"])
df["Name_Length"] = df["Name"].str.len()

print("\\n转换后数据:")
print(df)

# 统计年龄组分布
age_group_counts = df["Age_Group"].value_counts()
print("\\n年龄组分布:")
print(age_group_counts)

df
    """

    result = executor.execute(code)

    if result["success"]:
        print(f"\n转换结果:\n{result['logs']}")
    else:
        print(f"\n执行失败: {result['error']}")


def example_6_error_handling():
    """示例6: 错误处理演示"""
    print("\n" + "=" * 60)
    print("示例6: 错误处理")
    print("=" * 60)

    executor = AICodeExecutor()

    # 测试1: 除零错误
    print("\n测试1: 除零错误")
    result = executor.execute("x = 1 / 0")
    print(f"结果: {result['success']}")
    print(f"错误: {result['error']}")

    # 测试2: 语法错误
    print("\n测试2: 语法错误")
    result = executor.execute("if True print('No colon')")
    print(f"结果: {result['success']}")
    print(f"错误: {result['error']}")

    # 测试3: 禁止的导入
    print("\n测试3: 禁止的导入")
    result = executor.execute("import os; print('This will fail')")
    print(f"结果: {result['success']}")
    print(f"错误: {result['error']}")


def main():
    """运行所有示例"""
    print("\n" + "=" * 60)
    print("Codebox 使用示例")
    print("=" * 60)

    examples = [
        example_1_basic_usage,
        example_2_excel_analysis,
        example_3_with_variables,
        example_4_string_processing,
        example_5_data_transformation,
        example_6_error_handling,
    ]

    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\n[ERROR] 示例 '{example.__name__}' 发生异常: {e}")

    print("\n" + "=" * 60)
    print("示例演示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
