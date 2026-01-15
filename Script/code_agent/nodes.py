"""CodeAgent节点实现"""

from typing import Literal
from ..generate_code.generator import generate_code
from ..codebox.code_executor import AICodeExecutor
from .fix_agent import FixCodeAgent


def generate_node(state: dict) -> dict:
    """生成代码节点

    使用generator生成代码，将错误历史添加到prompt以避免重复错误

    Args:
        state: 当前状态

    Returns:
        更新后的状态
    """
    requirements = state["requirements"]
    error_history = state["error_history"]

    # 构建增强的需求描述
    if error_history:
        enhanced_requirements = f"""{requirements}

请注意，之前的尝试中出现过以下错误，请避免:
{chr(10).join(f"- {err}" for err in error_history)}"""
    else:
        enhanced_requirements = requirements

    # 生成代码
    code = generate_code(enhanced_requirements)

    # 更新状态
    new_state = state.copy()
    new_state["code"] = code
    new_state["messages"].append(f"[生成] 生成代码完成，代码长度: {len(code)} 字符")

    return new_state


def execute_node(state: dict) -> dict:
    """执行代码节点

    使用AICodeExecutor执行当前代码

    Args:
        state: 当前状态

    Returns:
        更新后的状态
    """
    code = state["code"]

    # 执行代码
    executor = AICodeExecutor()
    result = executor.execute(code)

    # 更新状态
    new_state = state.copy()
    new_state["execution_result"] = result

    if result["success"]:
        new_state["messages"].append("[执行] 执行成功")
        new_state["final_result"] = result["output"]
    else:
        new_state["messages"].append(f"[执行] 执行失败: {result['error']}")
        new_state["error_history"].append(result["error"])

    return new_state


def check_error_node(state: dict) -> dict:
    """检查错误节点

    判断执行是否成功，决定下一步流向

    Args:
        state: 当前状态

    Returns:
        更新后的状态，包含next_node字段指示下一步
    """
    execution_result = state["execution_result"]
    fix_attempts = state["fix_attempts"]
    max_fix_attempts = state["max_fix_attempts"]

    new_state = state.copy()

    if execution_result["success"]:
        # 执行成功，进入验证节点
        new_state["next_node"] = "verify"
        new_state["messages"].append("[检查] 执行成功，进入验证节点")
    else:
        # 执行失败
        if fix_attempts < max_fix_attempts:
            # 可以尝试修复
            new_state["next_node"] = "fix"
            new_state["messages"].append(
                f"[检查] 执行失败，尝试修复 (第 {fix_attempts + 1} 次)"
            )
        else:
            # 超过修复次数限制，结束
            new_state["next_node"] = "end"
            new_state["success"] = False
            new_state["messages"].append(
                f"[检查] 超过最大修复次数 ({max_fix_attempts})，结束工作流"
            )

    return new_state


def fix_node(state: dict) -> dict:
    """修复代码节点

    使用独立FixAgent修复代码

    Args:
        state: 当前状态

    Returns:
        更新后的状态
    """
    code = state["code"]
    error_history = state["error_history"]

    # 获取最新的错误信息
    latest_error = error_history[-1] if error_history else "未知错误"

    # 使用FixAgent修复
    fix_agent = FixCodeAgent()
    fixed_code = fix_agent.fix(code, latest_error, error_history[:-1])

    # 更新状态
    new_state = state.copy()
    new_state["code"] = fixed_code
    new_state["fix_attempts"] += 1
    new_state["messages"].append(
        f"[修复] 代码修复完成 (第 {new_state['fix_attempts']} 次)"
    )

    # 重置执行结果，准备重新执行
    new_state["execution_result"] = {"success": False, "error": None}

    return new_state


def verify_node(state: dict) -> dict:
    """验证结果节点

    验证执行结果是否符合要求
    注意: 此节点暂时跳过，直接返回成功

    Args:
        state: 当前状态

    Returns:
        更新后的状态
    """
    # 暂时跳过验证逻辑
    new_state = state.copy()
    new_state["is_valid"] = True
    new_state["success"] = True
    new_state["next_node"] = "end"
    new_state["messages"].append("[验证] 验证通过 (暂时跳过实际验证逻辑)")

    # TODO: 未来实现实际验证逻辑
    # 1. 使用AI判断final_result是否符合validation_rules
    # 2. 如果不符合，设置next_node="generate"并增加retry_count
    # 3. 如果符合，设置success=True并结束

    return new_state


def end_node(state: dict) -> dict:
    """结束节点

    标记工作流结束

    Args:
        state: 当前状态

    Returns:
        最终状态
    """
    new_state = state.copy()
    new_state["next_node"] = "__end__"
    new_state["messages"].append("[结束] 工作流结束")
    return new_state


def should_retry(state: dict) -> str:
    """判断是否继续重试

    Args:
        state: 当前状态

    Returns:
        "continue" 或 "end"
    """
    retry_count = state["retry_count"]
    max_retries = state["max_retries"]

    if retry_count < max_retries:
        state["retry_count"] += 1
        state["messages"].append(f"[重试] 第 {state['retry_count']} 次重试")
        return "continue"
    else:
        state["success"] = False
        state["messages"].append(f"[重试] 超过最大重试次数 ({max_retries})，结束工作流")
        return "end"
