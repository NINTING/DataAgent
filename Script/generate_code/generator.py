"""代码生成器核心实现

使用 pydantic-ai 生成符合 AICodeExecutor 环境约束的 Python 代码
"""

import re
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from ..custom_provider import get_glm_config


CODE_GENERATION_PROMPT = """你是一个 Python 代码生成助手，专门生成单个函数的工具代码。

# 环境约束

## 可用模块
math, re, datetime, collections, itertools, random, statistics
pandas, openpyxl, tabulate

## 禁止使用
- 模块: os, sys, subprocess, pathlib, socket, builtins
- 函数: eval(), exec(), compile(), __import__()

## 执行限制
- 最大操作数: 10,000,000
- print 输出限制: 50,000 字符

# 输出要求

生成单个函数，要求：
1. 函数有明确的参数和返回值
2. 包含简洁的 docstring
3. 添加必要的错误处理
4. 最后返回函数调用结果作为示例
5. 只返回 Python 代码，不要任何解释文字

# 示例

用户: 计算斐波那契数列前n项
```python
def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i-1] + result[i-2])
    
    return result

fibonacci(10)
```

用户: 读取Excel并计算某列平均值
```python
import pandas as pd

def calculate_excel_average(file_path: str, column: str) -> float:
    df = pd.read_excel(file_path)
    return df[column].mean()

calculate_excel_average('data.xlsx', 'score')
```

现在请根据用户需求生成代码：

用户: {requirements}
"""


def parse_code_response(response: str) -> str:
    """提取代码块中的Python代码

    Args:
        response: AI生成的完整响应

    Returns:
        纯Python代码字符串
    """
    match = re.search(r"```python\n(.*?)```", response, re.DOTALL)
    return match.group(1).strip() if match else response.strip()


def validate_code(code: str) -> dict:
    """快速验证代码环境约束

    Args:
        code: 要验证的代码

    Returns:
        dict: {'valid': bool, 'issues': list}
    """
    issues = []

    # 禁止的导入和函数
    forbidden_patterns = [
        "import os",
        "import sys",
        "import subprocess",
        "import pathlib",
        "import socket",
        "eval(",
        "exec(",
        "compile(",
        "__import__",
    ]

    for pattern in forbidden_patterns:
        if pattern in code:
            issues.append(f"禁止使用: {pattern}")

    return {"valid": len(issues) == 0, "issues": issues}


def generate_code(requirements: str) -> str:
    """根据需求生成 Python 代码

    使用 pydantic-ai 调用 GLM API 生成符合 AICodeExecutor 环境约束的代码。

    Args:
        requirements: 代码需求描述

    Returns:
        str: 生成的 Python 代码

    Example:
        >>> code = generate_code("计算斐波那契数列前10项")
        >>> print(code)
        def fibonacci(n: int) -> list[int]:
            ...
    """
    # 读取 GLM 配置
    api_key, base_url, model = get_glm_config()

    # 构建完整的 prompt
    prompt = CODE_GENERATION_PROMPT.format(requirements=requirements)

    # 创建自定义 provider
    provider = OpenAIProvider(api_key=api_key, base_url=base_url)

    # 创建 model 和 agent (model 格式: provider_name:model_name)
    model = OpenAIChatModel(model, provider=provider)
    agent = Agent(model, retries=2)

    try:
        # 调用 API 生成代码
        response = agent.run_sync(prompt)

        # 提取纯代码
        code = parse_code_response(response.output)

        # 验证代码
        validation = validate_code(code)

        if not validation["valid"]:
            print(f"[WARNING] 生成的代码可能包含禁止的内容:")
            for issue in validation["issues"]:
                print(f"  - {issue}")

        return code

    except Exception as e:
        raise RuntimeError(f"代码生成失败: {type(e).__name__}: {e}")
