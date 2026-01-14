import os
from smolagents import OpenAIModel


def get_custom_provider():
    """从 config.config 读取配置并返回自定义的模型提供者"""
    
    # 获取配置文件路径
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.config')
    
    # 读取配置文件（简单的键值对格式）
    config = {}
    with open(config_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
    
    # 获取配置项
    base_url = config.get('GLM_BASE_URL', '')
    api_key = config.get('GLM_API', '')
    model_id = config.get('MODEL_ID', 'GLM-4.7')
    
    print(f"读取配置:")
    print(f"  Base URL: {base_url}")
    print(f"  API Key: {api_key[:10]}...{api_key[-5:]}")
    print(f"  Model ID: {model_id}")
    
    # 创建并返回 OpenAIModel 实例
    model = OpenAIModel(
        model_id=model_id,
        api_base=base_url,
        api_key=api_key
    )
    
    return model


if __name__ == '__main__':
    # 测试获取自定义 provider
    model = get_custom_provider()
    print(f"模型提供者已创建: {model}")
