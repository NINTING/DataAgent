import sys

from Script.custom_provider import get_glm_config
from smolagents import OpenAIModel, CodeAgent


def test_basic_connection():
    """测试 CodeAgent 和模型的基本连接"""

    print("=" * 60)
    print("测试 CodeAgent 和模型的基本连接")
    print("=" * 60)

    try:
        # 获取 GLM 配置
        print("\n1. 获取模型提供者...")
        api_key, base_url, model_name = get_glm_config()
        model = OpenAIModel(
            model_id=model_name,
            api_key=api_key,
            base_url=base_url,
        )
        print("   [OK] 模型提供者创建成功")

        # 创建 CodeAgent
        print("\n2. 创建 CodeAgent...")
        agent = CodeAgent(
            model=model,
            tools=[],
            max_steps=10,
        )
        print("   [OK] CodeAgent 创建成功")

        # 执行简单的测试任务
        print("\n3. 执行简单测试任务...")
        task = "请编写python，计算 15 + 27 的结果，并使用 final_answer 返回答案。"
        print(f"   任务: {task}")

        result = agent.run(task)

        print(f"\n   [OK] 任务执行完成")
        print(f"   结果: {result}")

        print("\n" + "=" * 60)
        print("[OK] 所有测试通过！模型连接正常。")
        print("=" * 60)

        return True

    except Exception as e:
        print(f"\n   [FAIL] 测试失败: {e}")
        print("\n" + "=" * 60)
        print("[FAIL] 测试失败")
        print("=" * 60)
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_basic_connection()
    sys.exit(0 if success else 1)
