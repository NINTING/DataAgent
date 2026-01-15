"""代码生成器使用示例

演示 generate_code 函数的各种使用场景
"""

from Script.generate_code import generate_code
from Script.codebox import AICodeExecutor


def example_1_fibonacci():
    """示例1: 生成斐波那契数列函数"""
    print("=" * 60)
    print("示例1: 斐波那契数列")
    print("=" * 60)

    requirements = "生成一个函数，计算斐波那契数列前n项"

    print(f"需求: {requirements}\n")

    code = generate_code(requirements)
    print("生成的代码:")
    print(code)

    executor = AICodeExecutor()
    result = executor.execute(code)

    if result["success"]:
        print(f"\n执行结果: {result['output']}")


def example_2_average():
    """示例2: 计算平均值"""
    print("\n" + "=" * 60)
    print("示例2: 计算平均值")
    print("=" * 60)

    requirements = "生成一个函数，计算列表的平均值"

    print(f"需求: {requirements}\n")

    code = generate_code(requirements)
    print("生成的代码:")
    print(code)

    executor = AICodeExecutor()
    result = executor.execute(code)

    if result["success"]:
        print(f"\n执行结果: {result['output']}")


def example_3_dataframe():
    """示例3: 创建和操作DataFrame"""
    print("\n" + "=" * 60)
    print("示例3: 创建DataFrame")
    print("=" * 60)

    requirements = "生成一个函数，创建包含学生姓名和分数的DataFrame，并计算平均分"

    print(f"需求: {requirements}\n")

    code = generate_code(requirements)
    print("生成的代码:")
    print(code)

    executor = AICodeExecutor()
    result = executor.execute(code)

    if result["success"]:
        print(f"\n执行结果:\n{result['logs']}")
        print(f"\n返回的DataFrame:\n{result['output']}")


def example_4_string_processing():
    """示例4: 字符串处理"""
    print("\n" + "=" * 60)
    print("示例4: 字符串处理")
    print("=" * 60)

    requirements = "生成一个函数，统计字符串中单词的数量和字母的总数"

    print(f"需求: {requirements}\n")

    code = generate_code(requirements)
    print("生成的代码:")
    print(code)

    executor = AICodeExecutor()
    result = executor.execute(code)

    if result["success"]:
        print(f"\n执行结果: {result['output']}")


def example_5_math_operations():
    """示例5: 数学运算"""
    print("\n" + "=" * 60)
    print("示例5: 数学运算")
    print("=" * 60)

    requirements = "生成一个函数，计算1到100的平方和"

    print(f"需求: {requirements}\n")

    code = generate_code(requirements)
    print("生成的代码:")
    print(code)

    executor = AICodeExecutor()
    result = executor.execute(code)

    if result["success"]:
        print(f"\n执行结果: {result['output']}")


def main():
    """运行所有示例"""
    print("\n" + "=" * 60)
    print("代码生成器使用示例")
    print("=" * 60)

    examples = [
        example_1_fibonacci,
        example_2_average,
        example_3_dataframe,
        example_4_string_processing,
        example_5_math_operations,
    ]

    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\n[ERROR] 示例 '{example.__name__}' 发生异常: {e}")
            import traceback

            traceback.print_exc()

    print("\n" + "=" * 60)
    print("示例演示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
