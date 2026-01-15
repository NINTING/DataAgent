"""CodeAgent主类"""

from typing import Optional, Any
from .graph import create_code_agent_graph
from .state import CodeAgentState


class CodeAgent:
    """CodeAgent - 使用LangGraph的代码生成、执行、修复、验证工作流

    工作流程:
    1. 接收需求
    2. 生成代码 (使用Generator)
    3. 执行代码 (使用Codebox)
    4. 检查错误
    5. 如有错误，修复代码 (使用FixAgent)
    6. 验证结果 (暂时跳过)
    7. 返回最终结果

    Example:
        >>> agent = CodeAgent(max_retries=3, max_fix_attempts=2)
        >>> result = agent.run("计算斐波那契数列前10项")
        >>> if result["success"]:
        ...     print(f"结果: {result['output']}")
    """

    def __init__(self, max_retries: int = 3, max_fix_attempts: int = 2):
        """初始化CodeAgent

        Args:
            max_retries: 最大重试次数 (完整工作流重试)
            max_fix_attempts: 每次执行后最大修复次数
        """
        self.max_retries = max_retries
        self.max_fix_attempts = max_fix_attempts

        # 构建图
        self.graph = create_code_agent_graph()
        self.compiled_graph = self.graph.compile()

    def run(
        self,
        requirements: str,
        validation_rules: Optional[str] = None,
        verbose: bool = True,
    ) -> dict:
        """运行CodeAgent工作流

        Args:
            requirements: 需求描述
            validation_rules: 验证规则 (可选，暂时不启用)
            verbose: 是否打印详细过程

        Returns:
            dict: 执行结果，包含:
                - success: bool, 是否成功
                - output: Any, 最终输出结果
                - code: str, 最终代码
                - retry_count: int, 重试次数
                - fix_attempts: int, 修复尝试次数
                - messages: list, 过程消息列表
                - error: str | None, 错误信息 (如果失败)
        """
        # 初始化状态
        initial_state: CodeAgentState = {
            # 输入
            "requirements": requirements,
            "validation_rules": validation_rules,
            "max_retries": self.max_retries,
            "max_fix_attempts": self.max_fix_attempts,
            # 运行时状态
            "code": "",
            "execution_result": {"success": False, "error": None},
            "error_history": [],
            # 计数器
            "retry_count": 0,
            "fix_attempts": 0,
            # 验证
            "is_valid": None,
            "verification_result": None,
            # 输出
            "final_result": None,
            "success": False,
            "messages": [f"[开始] CodeAgent工作流启动\n需求: {requirements}"],
        }

        try:
            # 执行图
            final_state = self.compiled_graph.invoke(initial_state)

            # 如果需要，打印详细过程
            if verbose:
                self._print_messages(final_state["messages"])

            # 返回结果
            return {
                "success": final_state["success"],
                "output": final_state["final_result"],
                "code": final_state["code"],
                "retry_count": final_state["retry_count"],
                "fix_attempts": final_state["fix_attempts"],
                "messages": final_state["messages"],
                "error": None
                if final_state["success"]
                else (final_state["execution_result"].get("error") or "未知错误"),
            }

        except Exception as e:
            # 处理工作流执行异常
            error_msg = f"工作流执行异常: {type(e).__name__}: {e}"
            return {
                "success": False,
                "output": None,
                "code": "",
                "retry_count": 0,
                "fix_attempts": 0,
                "messages": [error_msg],
                "error": error_msg,
            }

    def _print_messages(self, messages: list):
        """打印过程消息

        Args:
            messages: 消息列表
        """
        print("\n" + "=" * 70)
        print("CodeAgent 执行过程")
        print("=" * 70)
        for msg in messages:
            print(msg)
        print("=" * 70 + "\n")

    def get_graph_structure(self) -> str:
        """获取图结构 (用于调试)

        Returns:
            Mermaid格式的图结构字符串
        """
        try:
            return self.compiled_graph.get_graph().print_mermaid()
        except Exception:
            return "无法获取图结构"
