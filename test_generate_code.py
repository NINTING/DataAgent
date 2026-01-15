"""快速测试代码生成功能

测试 generate_code 函数的基本功能
"""

from Script.generate_code import generate_code
from Script.codebox import AICodeExecutor


def main():
    """运行快速测试"""
    print("=" * 60)
    print("代码生成器快速测试")
    print("=" * 60)

    requirements = "生成一个函数，计算斐波那契数列前10项"

    print(f"\n需求: {requirements}")
    print("\n正在生成代码...")

    try:
        code = generate_code(requirements)

        print("\n生成的代码:")
        print("=" * 60)
        print(code)
        print("=" * 60)

        # 在 AICodeExecutor 中执行
        print("\n正在执行代码...")
        executor = AICodeExecutor()
        result = executor.execute(code)

        if result["success"]:
            print("\n✓ 执行成功!")
            print(f"返回值: {result['output']}")
            if result["logs"]:
                print(f"日志:\n{result['logs']}")
            print("\n" + "=" * 60)
            print("测试通过！")
            print("=" * 60)
        else:
            print(f"\n✗ 执行失败:")
            print(f"错误: {result['error']}")

    except Exception as e:
        print(f"\n✗ 发生错误:")
        print(f"{type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
