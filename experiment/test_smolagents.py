import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from smolagents import CodeAgent
from experiment.custom_provider import get_custom_provider

def test_read_excel_first_row():
    """测试 smolagents 的 CodeAgent 读取 Excel 文件第一行"""
    
    # 获取自定义模型提供者
    model = get_custom_provider()
    
    # 创建 CodeAgent（不提供任何工具，让 agent 自主编写代码）
    agent = CodeAgent(
        model=model,
        tools=[],
        stream_outputs=True
    )
    
    # 定义任务：读取 Excel 文件的 Sheet1 的第一行
    excel_path = r"D:\Code\DataAgent\ExcelData\Covid Dashboard.xlsx"
    task = f"""
    请编写 Python 代码读取 Excel 文件 '{excel_path}' 中的 Sheet1 工作表的全部数据。
    使用 pandas 或 openpyxl 读取数据，并返回第一行的内容。
    
    要求：
    1. 使用 pandas 或 openpyxl 读取 Excel 文件
    2. 获取 Sheet1 工作表
    3. 提取第一行的所有列数据
    4. 使用 final_answer 返回结果
    """
    
    # 运行 agent
    print("正在运行 CodeAgent...")
    print("-" * 60)
    
    result = agent.run(task)
    
    print("-" * 60)
    print("\n最终结果:")
    print(result)
    
    return result


if __name__ == '__main__':
    test_read_excel_first_row()
