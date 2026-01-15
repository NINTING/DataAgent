"""配置读取模块

使用 python-dotenv 读取环境配置
"""

from dotenv import load_dotenv
import os


def get_glm_config():
    """读取 GLM 配置

    从 .env 文件或环境变量中读取 GLM API 配置。

    配置优先级：
    1. 环境变量
    2. .env 文件

    Returns:
        tuple: (api_key, base_url, model)
            - api_key: GLM API 密钥
            - base_url: GLM API 基础 URL
            - model: 模型名称
    """
    # 加载 .env 文件（如果存在）
    load_dotenv()

    # 从环境变量读取配置（支持 .env 文件和环境变量）
    api_key = os.getenv("GLM_API", "")
    base_url = os.getenv("GLM_BASE_URL", "https://open.bigmodel.cn/api/coding/paas/v4")
    model = os.getenv("GLM_MODEL", "GLM-4")

    return api_key, base_url, model


def set_glm_config(api_key: str, base_url: str = None, model: str = None):
    """设置 GLM 配置到环境变量

    Args:
        api_key: GLM API 密钥
        base_url: GLM API 基础 URL（可选）
        model: 模型名称（可选）
    """
    os.environ["GLM_API"] = api_key
    if base_url:
        os.environ["GLM_BASE_URL"] = base_url
    if model:
        os.environ["GLM_MODEL"] = model


def save_glm_config(
    api_key: str, base_url: str = None, model: str = None, env_file: str = ".env"
):
    """保存 GLM 配置到 .env 文件

    Args:
        api_key: GLM API 密钥
        base_url: GLM API 基础 URL（可选）
        model: 模型名称（可选）
        env_file: .env 文件路径（默认项目根目录）
    """
    if base_url is None:
        base_url = "https://open.bigmodel.cn/api/coding/paas/v4"
    if model is None:
        model = "GLM-4"

    config_content = f"""# GLM API 配置
GLM_API={api_key}
GLM_BASE_URL={base_url}
GLM_MODEL={model}
"""

    with open(env_file, "w", encoding="utf-8") as f:
        f.write(config_content)
