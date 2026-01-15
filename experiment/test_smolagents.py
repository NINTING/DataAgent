from Script.custom_provider import get_glm_config
from smolagents import OpenAIModel, CodeAgent


def test_read_excel_first_row():
    """测试 smolagents 的 CodeAgent 读取 Excel 文件第一行"""

    # 获取 GLM 配置
    api_key, base_url, model_name = get_glm_config()
    model = OpenAIModel(
        model_id=model_name,
        api_key=api_key,
        base_url=base_url,
    )

    # 创建 CodeAgent（不提供任何工具，让 agent 自主编写代码）
    agent = CodeAgent(model=model, tools=[], max_steps=10)

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


if __name__ == "__main__":
    test_read_excel_first_row()
