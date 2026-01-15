"""代码生成器测试

测试 generate_code 函数的基本功能和与 AICodeExecutor 的集成
"""

from Script.generate_code import generate_code
from Script.codebox import AICodeExecutor


def test_basic_generation():
    """测试1: 基础代码生成 - 斐波那契数列"""
    print("=" * 60)
    print("测试1: 基础代码生成 - 斐波那契数列")
    print("=" * 60)

    requirements = "生成一个函数，计算斐波那契数列前n项"

    try:
        code = generate_code(requirements)
        print("\n生成的代码:")
        print(code)

        # 在 AICodeExecutor 中执行
        executor = AICodeExecutor()
        result = executor.execute(code)

        if result["success"]:
            print(f"\n✓ 执行成功")
            print(f"返回值: {result['output']}")
            if result["logs"]:
                print(f"日志: {result['logs']}")
        else:
            print(f"\n✗ 执行失败: {result['error']}")
            return False

    except Exception as e:
        print(f"\n✗ 生成失败: {e}")
        import traceback

        traceback.print_exc()
        return False

    return True


def test_pandas_code():
    """测试2: Pandas 代码生成 - DataFrame 创建"""
    print("\n" + "=" * 60)
    print("测试2: Pandas 代码生成")
    print("=" * 60)

    requirements = "生成一个函数，创建一个包含姓名和年龄的DataFrame，并计算平均年龄"

    try:
        code = generate_code(requirements)
        print("\n生成的代码:")
        print(code)

        executor = AICodeExecutor()
        result = executor.execute(code)

        if result["success"]:
            print(f"\n✓ 执行成功")
            print(f"返回值: {result['output']}")
        else:
            print(f"\n✗ 执行失败: {result['error']}")
            return False

    except Exception as e:
        print(f"\n✗ 生成失败: {e}")
        return False

    return True


def test_math_calculation():
    """测试3: 数学计算代码生成"""
    print("\n" + "=" * 60)
    print("测试3: 数学计算代码生成")
    print("=" * 60)

    requirements = "生成一个函数，计算1到100的整数和"

    try:
        code = generate_code(requirements)
        print("\n生成的代码:")
        print(code)

        executor = AICodeExecutor()
        result = executor.execute(code)

        if result["success"]:
            print(f"\n✓ 执行成功")
            print(f"返回值: {result['output']}")
        else:
            print(f"\n✗ 执行失败: {result['error']}")
            return False

    except Exception as e:
        print(f"\n✗ 生成失败: {e}")
        return False

    return True


def test_excel_reading():
    """测试4: Excel 读取代码生成"""
    print("\n" + "=" * 60)
    print("测试4: Excel 读取代码生成")
    print("=" * 60)

    requirements = "生成一个函数，读取Excel文件并返回前5行数据"

    try:
        code = generate_code(requirements)
        print("\n生成的代码:")
        print(code)

        # 注意：这个测试可能会失败，因为需要实际的 Excel 文件
        # 这里只测试代码生成是否成功
        print("\n✓ 代码生成成功（未实际执行，需要Excel文件）")

    except Exception as e:
        print(f"\n✗ 生成失败: {e}")
        return False

    return True


def main():
    """运行所有测试"""
    print("\n" + "=" * 60)
    print("代码生成器测试套件")
    print("=" * 60)

    tests = [
        test_basic_generation,
        test_pandas_code,
        test_math_calculation,
        test_excel_reading,
    ]

    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"\n[ERROR] 测试 '{test.__name__}' 发生异常: {e}")
            import traceback

            traceback.print_exc()
            results.append(False)

    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"通过: {passed}/{total}")

    if passed == total:
        print("\n✓ 所有测试通过！")
    else:
        print(f"\n✗ {total - passed} 个测试失败")

    print("=" * 60)


if __name__ == "__main__":
    main()
