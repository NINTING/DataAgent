"""快速测试CodeAgent"""

from Script.code_agent import CodeAgent


def main():
    """快速测试"""
    print("=" * 70)
    print("CodeAgent 快速测试")
    print("=" * 70)

    agent = CodeAgent(max_retries=3, max_fix_attempts=2)

    result = agent.run(
        requirements="生成一个函数，计算斐波那契数列前10项", verbose=True
    )

    print("\n" + "=" * 70)
    print("测试结果")
    print("=" * 70)

    if result["success"]:
        print(f"[OK] 成功!")
        print(f"结果: {result['output']}")
        print(f"重试次数: {result['retry_count']}")
        print(f"修复次数: {result['fix_attempts']}")
    else:
        print(f"[FAIL] 失败!")
        print(f"错误: {result['error']}")


if __name__ == "__main__":
    main()
