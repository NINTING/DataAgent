"""AI代码执行器

使用smolagents的LocalPythonExecutor提供安全的Python代码执行环境。
支持自定义变量注入、工具注册和完整的错误处理。
"""

from smolagents import LocalPythonExecutor
from smolagents.local_python_executor import InterpreterError


class AICodeExecutor:
    """AI代码执行器
    
    使用smolagents的LocalPythonExecutor提供安全的代码执行环境。
    支持pandas、openpyxl等Excel相关库，以及自定义变量和工具注入。
    
    Attributes:
        executor: LocalPythonExecutor实例
        authorized_imports: 授权导入的模块列表
    """
    
    def __init__(self, additional_imports=None):
        """初始化执行器
        
        Args:
            additional_imports: 额外授权导入的模块列表
        """
        self.authorized_imports = [
            "math",
            "re",
            "datetime",
            "collections",
            "itertools",
            "random",
            "statistics",
            "pandas",
            "openpyxl",
            "tabulate",
        ]
        
        if additional_imports:
            self.authorized_imports.extend(additional_imports)
        
        self.executor = LocalPythonExecutor(
            additional_authorized_imports=self.authorized_imports
        )
    
    def execute(
        self,
        code: str,
        variables: dict = None,
        tools: dict = None,
        clear_state: bool = True
    ):
        """执行Python代码

        Args:
            code: 要执行的Python代码字符串
            variables: 要注入的变量字典（可选）
            tools: 要注册的自定义工具字典（可选）
            clear_state: 是否清除之前的状态（默认True）

        Returns:
            dict: 执行结果字典，包含以下字段：
                - success: bool, 是否执行成功
                - output: Any, 代码返回值
                - logs: str, print输出
                - is_final_answer: bool, 是否调用了final_answer
                - error: str | None, 错误信息（如果有）

        Example:
            >>> executor = AICodeExecutor()
            >>> result = executor.execute("result = 2 + 3; print('Done'); result * 10")
            >>> if result["success"]:
            ...     print(result["output"])  # 50
            ...     print(result["logs"])    # "Done\n"
        """
        try:
            if clear_state:
                self.executor.state = {"__name__": "__main__"}

            if variables:
                self.executor.send_variables(variables)

            self.executor.send_tools(tools or {})

            output = self.executor(code_action=code)

            return {
                "success": True,
                "output": output.output,
                "logs": output.logs,
                "is_final_answer": output.is_final_answer,
                "error": None
            }

        except InterpreterError as e:
            return {
                "success": False,
                "output": None,
                "logs": "",
                "is_final_answer": False,
                "error": f"执行错误: {str(e)}"
            }

        except Exception as e:
            return {
                "success": False,
                "output": None,
                "logs": "",
                "is_final_answer": False,
                "error": f"{type(e).__name__}: {str(e)}"
            }
    
    # 以下为状态管理方法，暂时注释掉
    # 如需在多次执行之间保持变量状态，可以取消注释
    
    # def get_state(self):
    #     """获取当前执行器状态
        
    #     Returns:
    #         dict: 当前执行器中的所有变量
    #     """
    #     return self.executor.state.copy()
    
    # def set_state(self, state: dict):
    #     """设置执行器状态
        
    #     Args:
    #         state: 要设置的变量字典
    #     """
    #     self.executor.state.update(state)
    
    # def reset_state(self):
    #     """重置执行器状态为初始状态"""
    #     self.executor.state = {"__name__": "__main__"}
