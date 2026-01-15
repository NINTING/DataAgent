"""CodeAgent使用示例和测试"""

from Script.code_agent import CodeAgent


def example_1_simple_task():
    """示例1: 简单任务 - 斐波那契数列"""
    print("=" * 70)
    print("示例1: 斐波那契数列")
    print("=" * 70)

    agent = CodeAgent(max_retries=3, max_fix_attempts=2)

    result = agent.run(
        requirements="生成一个函数，计算斐波那契数列前10项", verbose=True
    )

    if result["success"]:
        print(f"\n✓ 成功!")
        print(f"结果: {result['output']}")
        print(f"重试次数: {result['retry_count']}")
        print(f"修复次数: {result['fix_attempts']}")
    else:
        print(f"\n✗ 失败!")
        print(f"错误: {result['error']}")

    print()


def example_2_data_analysis():
    """示例2: 数据分析任务"""
    print("=" * 70)
    print("示例2: 数据分析")
    print("=" * 70)

    agent = CodeAgent(max_retries=3, max_fix_attempts=2)

    result = agent.run(
        requirements="创建一个DataFrame，包含学生姓名和分数，计算平均分", verbose=True
    )

    if result["success"]:
        print(f"\n[OK] 成功!")
        print(f"结果: {result['output']}")
        print(f"重试次数: {result['retry_count']}")
        print(f"修复次数: {result['fix_attempts']}")
    else:
        print(f"\n[FAIL] 失败!")
        print(f"错误: {result['error']}")

    print()


def example_3_math_operations():
    """示例3: 数学运算"""
    print("=" * 70)
    print("示例3: 数学运算")
    print("=" * 70)

    agent = CodeAgent(max_retries=3, max_fix_attempts=2)

    result = agent.run(requirements="生成一个函数，计算1到100的平方和", verbose=True)

    if result["success"]:
        print(f"\n✓ 成功!")
        print(f"结果: {result['output']}")
        print(f"重试次数: {result['retry_count']}")
        print(f"修复次数: {result['fix_attempts']}")
    else:
        print(f"\n✗ 失败!")
        print(f"错误: {result['error']}")

    print()


def example_4_string_processing():
    """示例4: 字符串处理"""
    print("=" * 70)
    print("示例4: 字符串处理")
    print("=" * 70)

    agent = CodeAgent(max_retries=3, max_fix_attempts=2)

    result = agent.run(
        requirements="生成一个函数，统计字符串中单词的数量", verbose=False
    )

    if result["success"]:
        print(f"[OK] 成功!")
        print(f"结果: {result['output']}")
        print(f"重试次数: {result['retry_count']}")
    else:
        print(f"[FAIL] 失败!")
        print(f"错误: {result['error']}")

    print()


def example_5_with_validation():
    """示例5: 带验证规则 (暂时不启用，仅作演示)"""
    print("=" * 70)
    print("示例5: 带验证规则 (暂时不启用)")
    print("=" * 70)

    agent = CodeAgent(max_retries=3, max_fix_attempts=2)

    result = agent.run(
        requirements="生成一个函数，计算列表的平均值",
        validation_rules="结果应该是浮点数，且在0-100之间",
        verbose=False,
    )

    if result["success"]:
        print(f"[OK] 成功!")
        print(f"结果: {result['output']}")
    else:
        print(f"[FAIL] 失败!")
        print(f"错误: {result['error']}")

    print("\n注意: 验证逻辑暂时跳过，将来会实现")
    print()


def main():
    """运行所有示例"""
    print("\n" + "=" * 70)
    print("CodeAgent 使用示例")
    print("=" * 70 + "\n")

    examples = [
        example_1_simple_task,
        example_2_data_analysis,
        example_3_math_operations,
        example_4_string_processing,
        example_5_with_validation,
    ]

    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\n[ERROR] 示例 '{example.__name__}' 发生异常: {e}")
            import traceback

            traceback.print_exc()
            print()

    print("=" * 70)
    print("示例演示完成")
    print("=" * 70)


if __name__ == "__main__":
    main()
