"""CodeAgent状态定义"""

from typing import TypedDict, List, Optional, Any


class CodeAgentState(TypedDict):
    """CodeAgent工作流状态

    包含工作流运行过程中的所有状态信息
    """

    # 输入
    requirements: str
    validation_rules: Optional[str]
    max_retries: int
    max_fix_attempts: int

    # 运行时状态
    code: str
    execution_result: dict
    error_history: List[str]

    # 计数器
    retry_count: int
    fix_attempts: int

    # 验证(暂时不启用)
    is_valid: Optional[bool]
    verification_result: Optional[dict]

    # 输出
    final_result: Optional[Any]
    success: bool
    messages: List[str]
