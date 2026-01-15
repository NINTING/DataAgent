"""快速配置脚本

帮助用户快速设置 GLM API 配置
"""

import os
import sys


def setup_config():
    """配置 GLM API"""

    print("=" * 60)
    print("GLM API 配置向导")
    print("=" * 60)
    print()

    # 询问配置方式
    print("请选择配置方式：")
    print("1. 创建 .env 文件（推荐）")
    print("2. 设置环境变量（仅当前会话）")
    print("3. 复制 .env.example 模板手动配置")
    print()

    choice = input("请输入选项 (1/2/3): ").strip()

    if choice == "1":
        setup_env_file()
    elif choice == "2":
        setup_env_var()
    elif choice == "3":
        copy_template()
    else:
        print("无效的选项")
        return False

    print()
    print("=" * 60)
    print("配置完成！")
    print("=" * 60)

    return True


def setup_env_file():
    """配置 .env 文件"""
    print()
    print("配置 .env 文件")
    print("-" * 60)

    # 获取 API Key
    api_key = input("请输入你的 GLM API Key: ").strip()

    if not api_key:
        print("错误: API Key 不能为空")
        return False

    # 获取其他配置（可选）
    print()
    print("以下配置可以留空使用默认值：")

    base_url = input(
        f"GLM API 基础 URL [默认: https://open.bigmodel.cn/api/coding/paas/v4]: "
    ).strip()
    if not base_url:
        base_url = "https://open.bigmodel.cn/api/coding/paas/v4"

    model = input("模型名称 [默认: GLM-4.7]: ").strip()
    if not model:
        model = "GLM-4.7"

    # 写入 .env 文件
    env_content = f"""# GLM API 配置
# GLM API 密钥（必填）
GLM_API={api_key}

# GLM API 基础 URL（可选）
GLM_BASE_URL={base_url}

# 模型名称（可选）
GLM_MODEL={model}
"""

    env_file = ".env"

    try:
        with open(env_file, "w", encoding="utf-8") as f:
            f.write(env_content)

        print()
        print(f"✓ 配置已保存到 {env_file}")
        print(f"✓ API Key: {api_key[:10]}...")
        print(f"✓ Base URL: {base_url}")
        print(f"✓ Model: {model}")
        print()
        print("注意: .env 文件已自动添加到 .gitignore，不会被提交到 Git。")

        return True

    except Exception as e:
        print(f"错误: 无法保存配置文件 - {e}")
        return False


def setup_env_var():
    """配置环境变量"""
    print()
    print("配置环境变量（仅当前会话）")
    print("-" * 60)

    # 获取 API Key
    api_key = input("请输入你的 GLM API Key: ").strip()

    if not api_key:
        print("错误: API Key 不能为空")
        return False

    # 设置环境变量
    os.environ["GLM_API"] = api_key

    # 可选配置
    print()
    print("以下配置可以留空使用默认值：")

    base_url = input(
        f"GLM API 基础 URL [默认: https://open.bigmodel.cn/api/coding/paas/v4]: "
    ).strip()
    if not base_url:
        base_url = "https://open.bigmodel.cn/api/coding/paas/v4"

    model = input("模型名称 [默认: GLM-4.7]: ").strip()
    if not model:
        model = "GLM-4.7"

    os.environ["GLM_BASE_URL"] = base_url
    os.environ["GLM_MODEL"] = model

    print()
    print(f"✓ 环境变量已设置（仅当前会话）")
    print(f"✓ API Key: {api_key[:10]}...")
    print(f"✓ Base URL: {base_url}")
    print(f"✓ Model: {model}")
    print()
    print("注意: 环境变量仅在当前会话有效，重启终端后需要重新设置。")

    return True


def copy_template():
    """复制模板文件"""
    print()
    print("复制 .env.example 模板")
    print("-" * 60)

    if not os.path.exists(".env.example"):
        print("错误: .env.example 文件不存在")
        return False

    # 复制模板
    import shutil

    shutil.copy(".env.example", ".env")

    print()
    print("✓ 已复制 .env.example 到 .env")
    print()
    print("下一步：")
    print("1. 编辑 .env 文件")
    print("2. 填入你的 GLM API Key")
    print("3. 保存文件")

    return True


def verify_config():
    """验证配置"""
    print()
    print("验证配置...")
    print("-" * 60)

    # 导入配置读取函数
    from Script.custom_provider import get_glm_config

    api_key, base_url, model = get_glm_config()

    print(f"API Key: {api_key[:10] if api_key else 'Not configured'}...")
    print(f"Base URL: {base_url}")
    print(f"Model: {model}")

    if api_key:
        print()
        print("[OK] 配置有效！")
        return True
    else:
        print()
        print("[ERROR] API Key 未配置")
        return False


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="GLM API 配置工具")
    parser.add_argument("--verify", action="store_true", help="仅验证配置")
    args = parser.parse_args()

    if args.verify:
        verify_config()
    else:
        if setup_config():
            print()
            verify_config()


if __name__ == "__main__":
    main()
