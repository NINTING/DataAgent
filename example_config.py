"""配置管理示例

演示如何使用新的配置管理功能
"""

import os

from Script.custom_provider import get_glm_config, set_glm_config, save_glm_config


def example_1_read_config():
    """示例1: 读取配置"""
    print("=" * 60)
    print("示例1: 读取 GLM 配置")
    print("=" * 60)

    api_key, base_url, model = get_glm_config()

    print(f"API Key: {api_key[:10] if api_key else 'Not configured'}...")
    print(f"Base URL: {base_url}")
    print(f"Model: {model}")


def example_2_set_config():
    """示例2: 设置配置（仅当前会话）"""
    print("\n" + "=" * 60)
    print("示例2: 设置配置（当前会话）")
    print("=" * 60)

    # 设置到环境变量
    set_glm_config(
        api_key="sk-test-api-key-12345678",
        base_url="https://open.bigmodel.cn/api/coding/paas/v4",
        model="GLM-4.7",
    )

    # 读取验证
    api_key, base_url, model = get_glm_config()
    print(f"API Key: {api_key[:10]}...")
    print(f"Base URL: {base_url}")
    print(f"Model: {model}")


def example_3_save_config():
    """示例3: 保存配置到 .env 文件"""
    print("\n" + "=" * 60)
    print("示例3: 保存配置到 .env 文件")
    print("=" * 60)

    # 保存到 .env 文件
    save_glm_config(
        api_key="sk-test-api-key-12345678",
        base_url="https://open.bigmodel.cn/api/coding/paas/v4",
        model="GLM-4.7",
    )

    print("配置已保存到 .env 文件")

    # 读取验证
    api_key, base_url, model = get_glm_config()
    print(f"\n读取的配置:")
    print(f"API Key: {api_key[:10]}...")
    print(f"Base URL: {base_url}")
    print(f"Model: {model}")


def example_4_use_environment_variables():
    """示例4: 使用环境变量"""
    print("\n" + "=" * 60)
    print("示例4: 使用环境变量")
    print("=" * 60)

    # 设置环境变量
    os.environ["GLM_API"] = "sk-env-api-key-87654321"
    os.environ["GLM_MODEL"] = "GLM-4"

    # 读取配置（优先读取环境变量）
    api_key, base_url, model = get_glm_config()
    print(f"API Key: {api_key[:10]}...")
    print(f"Base URL: {base_url}")
    print(f"Model: {model}")


def example_5_check_config_source():
    """示例5: 检查配置来源"""
    print("\n" + "=" * 60)
    print("示例5: 检查配置来源")
    print("=" * 60)

    # 检查是否存在 .env 文件
    env_exists = os.path.exists(".env")
    print(f".env 文件存在: {env_exists}")

    # 检查环境变量
    env_api_key = os.getenv("GLM_API")
    print(f"环境变量 GLM_API 已设置: {env_api_key is not None}")

    # 读取配置
    api_key, base_url, model = get_glm_config()

    if env_api_key:
        print("\n配置来源: 环境变量")
    elif env_exists:
        print("\n配置来源: .env 文件")
    else:
        print("\n配置来源: 默认值（未配置）")

    print(f"\nAPI Key: {api_key[:10] if api_key else 'Not configured'}...")
    print(f"Base URL: {base_url}")
    print(f"Model: {model}")


def main():
    """运行所有示例"""
    print("\n" + "=" * 60)
    print("配置管理示例")
    print("=" * 60)

    examples = [
        example_1_read_config,
        example_5_check_config_source,
        example_2_set_config,
        example_3_save_config,
        example_4_use_environment_variables,
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
