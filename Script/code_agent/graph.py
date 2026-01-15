"""CodeAgent LangGraph图构建"""

from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, END
from .state import CodeAgentState
from .nodes import (
    generate_node,
    execute_node,
    check_error_node,
    fix_node,
    verify_node,
    end_node,
)


def create_code_agent_graph() -> StateGraph:
    """创建CodeAgent的LangGraph状态图

    构建工作流:
    generate → execute → check_error →
        ├─ 成功 → verify → end
        └─ 失败 → fix → execute (循环)

    Returns:
        StateGraph: LangGraph状态图实例
    """

    # 创建状态图
    workflow = StateGraph(CodeAgentState)

    # 添加节点
    workflow.add_node("generate", generate_node)
    workflow.add_node("execute", execute_node)
    workflow.add_node("check_error", check_error_node)
    workflow.add_node("fix", fix_node)
    workflow.add_node("verify", verify_node)
    workflow.add_node("end", end_node)

    # 设置入口点
    workflow.set_entry_point("generate")

    # 定义边

    # generate → execute
    workflow.add_edge("generate", "execute")

    # execute → check_error
    workflow.add_edge("execute", "check_error")

    # check_error → verify (成功)
    # check_error → fix (失败且可修复)
    # check_error → end (失败且超限)
    def route_check_error(state: dict) -> str:
        """路由函数: 根据check_error结果决定下一步"""
        return state.get("next_node", "end")

    workflow.add_conditional_edges(
        "check_error",
        route_check_error,
        {"verify": "verify", "fix": "fix", "end": "end"},
    )

    # fix → execute (修复后重新执行)
    workflow.add_edge("fix", "execute")

    # verify → end
    workflow.add_edge("verify", "end")

    # end → END
    workflow.add_edge("end", END)

    return workflow


def visualize_graph(workflow: StateGraph) -> str:
    """可视化图结构(用于调试)

    Args:
        workflow: StateGraph实例

    Returns:
        图的Mermaid格式字符串
    """
    try:
        return workflow.get_graph().print_mermaid()
    except Exception:
        return "图可视化失败"
