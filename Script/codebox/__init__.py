"""代码执行器模块

提供安全的Python代码执行环境，用于执行AI生成的代码。
支持pandas、openpyxl等Excel相关库。
"""

from .code_executor import AICodeExecutor

__all__ = ["AICodeExecutor"]
