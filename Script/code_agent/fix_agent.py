"""独立的代码修复Agent"""

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from ..custom_provider import get_glm_config
import re


FIX_CODE_PROMPT = """你是一个 Python 代码修复专家，专门修复代码执行错误。

# 你的任务
分析原始代码和错误信息，生成修复后的代码。

# 输入信息
- 原始代码:
```python
{original_code}
```

- 错误信息:
{error_message}

- 错误历史(之前的失败尝试):
{error_history}

# 修复要求
1. 分析错误的根本原因
2. 修复代码逻辑或语法问题
3. 确保修复后符合以下约束:
   - 可用模块: math, re, datetime, collections, itertools, random, statistics, pandas, openpyxl, tabulate
   - 禁止: os, sys, subprocess, pathlib, socket, eval(), exec(), compile(), __import__()
4. 保持原有的代码结构和意图
5. 添加必要的错误处理

# 输出要求
只返回修复后的完整Python代码，不要任何解释或注释。

示例:
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
"""


def parse_fix_response(response: str) -> str:
    """提取代码块中的Python代码

    Args:
        response: AI生成的完整响应

    Returns:
        纯Python代码字符串
    """
    match = re.search(r"```python\n(.*?)```", response, re.DOTALL)
    return match.group(1).strip() if match else response.strip()


class FixCodeAgent:
    """代码修复Agent

    专门用于分析错误信息并修复代码的独立Agent
    """

    def __init__(self):
        """初始化Fix Agent"""
        api_key, base_url, model = get_glm_config()

        provider = OpenAIProvider(api_key=api_key, base_url=base_url)
        model = OpenAIChatModel(model, provider=provider)
        self.agent = Agent(model, retries=2)

    def fix(
        self, original_code: str, error_message: str, error_history: list = None
    ) -> str:
        """修复代码

        Args:
            original_code: 原始代码
            error_message: 错误信息
            error_history: 之前的错误历史列表

        Returns:
            修复后的代码
        """
        if error_history is None:
            error_history = []

        error_history_str = (
            "\n".join([f"- {err}" for err in error_history]) if error_history else "无"
        )

        prompt = FIX_CODE_PROMPT.format(
            original_code=original_code,
            error_message=error_message,
            error_history=error_history_str,
        )

        try:
            response = self.agent.run_sync(prompt)
            fixed_code = parse_fix_response(response.output)
            return fixed_code
        except Exception as e:
            raise RuntimeError(f"代码修复失败: {type(e).__name__}: {e}")
