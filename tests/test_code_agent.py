"""CodeAgent集成测试 - 组合A

测试案例：
1. 简单案例：斐波那契数列
2. 复杂案例-Excel：Excel数据统计
3. 复杂案例-其他：文本分析
4. 结构验证：Agent结构
"""

import pytest
import os
from Script.code_agent import CodeAgent


# ============== pytest Fixtures ==============


@pytest.fixture
def agent():
    """创建CodeAgent实例"""
    return CodeAgent(max_retries=2, max_fix_attempts=1)


@pytest.fixture
def resource_path():
    """获取测试资源路径"""
    return "tests/resource"


# ============== 测试1：简单案例 - 斐波那契数列 ==============


@pytest.mark.slow
def test_fibonacci_simple(agent):
    """测试1: 简单案例 - 斐波那契数列

    验证CodeAgent能够正确生成、执行简单的算法代码
    """
    result = agent.run("生成一个函数，计算斐波那契数列前10项", verbose=False)

    # 验证执行成功
    assert result["success"], f"执行失败: {result.get('error')}"

    # 验证输出
    assert result["output"] is not None, "输出为空"
    assert isinstance(result["output"], list), "输出应该是列表"
    assert len(result["output"]) == 10, "输出应该包含10个元素"

    # 精确验证斐波那契数列
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert result["output"] == expected, (
        f"斐波那契数列不匹配: 期望 {expected}, 实际 {result['output']}"
    )


# ============== 测试2：复杂案例 - Excel数据统计 ==============


@pytest.mark.slow
def test_excel_statistics(agent, resource_path):
    """测试2: 复杂案例 - Excel数据统计

    验证CodeAgent能够：
    1. 读取Excel文件
    2. 计算数值列的统计信息（平均值、最大值、最小值）
    3. 统计数据行数和列数
    4. 返回结构化的统计结果

    测试文件：tests/resource/test_students.xlsx
    """
    excel_file = os.path.join(resource_path, "test_students.xlsx")

    # 确保测试文件存在
    assert os.path.exists(excel_file), f"测试文件不存在: {excel_file}"

    # 构建需求
    requirements = f"""读取Excel文件 '{excel_file}' 并进行以下统计分析：
1. 计算数据行数和列数
2. 对数值列（年龄、语文、数学、英语、总分）计算平均值、最大值、最小值
3. 返回一个字典，包含所有统计信息，格式如下：
   {{
       "数据行数": int,
       "数据列数": int,
       "年龄统计": {{"平均值": float, "最大值": int, "最小值": int}},
       "语文统计": {{"平均值": float, "最大值": int, "最小值": int}},
       "数学统计": {{"平均值": float, "最大值": int, "最小值": int}},
       "英语统计": {{"平均值": float, "最大值": int, "最小值": int}},
       "总分统计": {{"平均值": float, "最大值": int, "最小值": int}}
   }}"""

    result = agent.run(requirements, verbose=False)

    # 验证执行成功
    assert result["success"], f"执行失败: {result.get('error')}"

    # 验证输出
    output = result["output"]
    assert output is not None, "输出为空"
    assert isinstance(output, dict), "输出应该是字典"

    # 精确验证数据行数和列数
    assert "数据行数" in output, "输出应该包含'数据行数'"
    assert output["数据行数"] == 8, f"数据行数不匹配: 期望 8, 实际 {output['数据行数']}"

    assert "数据列数" in output, "输出应该包含'数据列数'"
    assert output["数据列数"] == 7, f"数据列数不匹配: 期望 7, 实际 {output['数据列数']}"

    # 精确验证各列统计信息
    expected_stats = {
        "年龄统计": {"平均值": 30.0, "最大值": 40, "最小值": 22},
        "语文统计": {"平均值": 81.875, "最大值": 95, "最小值": 65},
        "数学统计": {"平均值": 84.75, "最大值": 98, "最小值": 70},
        "英语统计": {"平均值": 81.625, "最大值": 90, "最小值": 68},
        "总分统计": {"平均值": 248.25, "最大值": 283, "最小值": 203},
    }

    for col_name, expected in expected_stats.items():
        assert col_name in output, f"输出应该包含'{col_name}'"

        col_stats = output[col_name]

        # 验证平均值（允许±0.1的误差）
        assert "平均值" in col_stats, f"{col_name}应该包含'平均值'"
        assert abs(col_stats["平均值"] - expected["平均值"]) < 0.1, (
            f"{col_name}平均值不匹配: 期望 {expected['平均值']}, "
            f"实际 {col_stats['平均值']}"
        )

        # 验证最大值
        assert "最大值" in col_stats, f"{col_name}应该包含'最大值'"
        assert col_stats["最大值"] == expected["最大值"], (
            f"{col_name}最大值不匹配: 期望 {expected['最大值']}, "
            f"实际 {col_stats['最大值']}"
        )

        # 验证最小值
        assert "最小值" in col_stats, f"{col_name}应该包含'最小值'"
        assert col_stats["最小值"] == expected["最小值"], (
            f"{col_name}最小值不匹配: 期望 {expected['最小值']}, "
            f"实际 {col_stats['最小值']}"
        )


# ============== 测试3：复杂案例 - 文本分析 ==============


@pytest.mark.slow
def test_text_analysis(agent, resource_path):
    """测试3: 复杂案例 - 文本分析

    验证CodeAgent能够：
    1. 读取文本文件
    2. 统计基础信息（行数、单词数、字符数）
    3. 提取所有数字并计算平均值
    4. 统计高频词（长度>3的单词）
    5. 返回结构化的分析结果

    测试文件：tests/resource/test_text.txt
    """
    text_file = os.path.join(resource_path, "test_text.txt")

    # 确保测试文件存在
    assert os.path.exists(text_file), f"测试文件不存在: {text_file}"

    # 构建需求
    requirements = f"""读取文本文件 '{text_file}' 并进行以下分析：
1. 统计总行数（以换行符分割）
2. 统计总单词数（以空格分割）
3. 统计总字符数（含空格）和总字符数（不含空格）
4. 使用正则表达式提取所有数字（包括整数和浮点数），转换为整数列表
5. 计算数字的个数和平均值
6. 统计单词频率（只统计长度大于3的单词，不区分大小写）
7. 返回频率最高的5个单词及其出现次数
8. 返回一个字典，包含所有统计信息，格式如下：
   {{
       "总行数": int,
       "总单词数": int,
       "总字符数_含空格": int,
       "总字符数_不含空格": int,
       "提取的数字": list[int],
       "数字个数": int,
       "数字平均值": float,
       "高频词_前5": [(str, int), ...]  # (单词, 频率)的列表
   }}"""

    result = agent.run(requirements, verbose=False)

    # 验证执行成功
    assert result["success"], f"执行失败: {result.get('error')}"

    # 验证输出
    output = result["output"]
    assert output is not None, "输出为空"
    assert isinstance(output, dict), "输出应该是字典"

    # 精确验证基础统计
    assert "总行数" in output, "输出应该包含'总行数'"
    assert output["总行数"] == 10, f"总行数不匹配: 期望 10, 实际 {output['总行数']}"

    assert "总单词数" in output, "输出应该包含'总单词数'"
    assert output["总单词数"] == 99, (
        f"总单词数不匹配: 期望 99, 实际 {output['总单词数']}"
    )

    assert "总字符数_含空格" in output, "输出应该包含'总字符数_含空格'"
    assert output["总字符数_含空格"] == 594, (
        f"总字符数_含空格不匹配: 期望 594, 实际 {output['总字符数_含空格']}"
    )

    assert "总字符数_不含空格" in output, "输出应该包含'总字符数_不含空格'"
    assert output["总字符数_不含空格"] == 495, (
        f"总字符数_不含空格不匹配: 期望 495, 实际 {output['总字符数_不含空格']}"
    )

    # 验证数字提取
    assert "提取的数字" in output, "输出应该包含'提取的数字'"
    numbers = output["提取的数字"]
    assert isinstance(numbers, list), "提取的数字应该是列表"
    assert len(numbers) == 16, f"数字个数不匹配: 期望 16, 实际 {len(numbers)}"

    expected_numbers = [
        1991,
        2001,
        2,
        0,
        2000,
        3,
        0,
        2008,
        5000,
        2023,
        19,
        1000,
        5000,
        3,
        12,
        0,
    ]
    assert numbers == expected_numbers, (
        f"提取的数字不匹配: 期望 {expected_numbers}, 实际 {numbers}"
    )

    # 验证数字统计
    assert "数字个数" in output, "输出应该包含'数字个数'"
    assert output["数字个数"] == 16, (
        f"数字个数不匹配: 期望 16, 实际 {output['数字个数']}"
    )

    assert "数字平均值" in output, "输出应该包含'数字平均值'"
    # 允许±1的误差
    assert abs(output["数字平均值"] - 1316.375) < 1, (
        f"数字平均值不匹配: 期望 1316.375, 实际 {output['数字平均值']}"
    )

    # 验证高频词
    assert "高频词_前5" in output, "输出应该包含'高频词_前5'"
    top_words = output["高频词_前5"]
    assert isinstance(top_words, list), "高频词应该是列表"
    assert len(top_words) == 5, f"高频词数量不匹配: 期望 5, 实际 {len(top_words)}"

    # 验证最高频词是'python'，出现10次
    python_word = top_words[0]
    assert python_word[0] == "python", (
        f"最高频词不匹配: 期望 'python', 实际 {python_word[0]}"
    )
    assert python_word[1] == 10, (
        f"'python'出现次数不匹配: 期望 10, 实际 {python_word[1]}"
    )

    # 验证其他高频词
    # 预期：python(10), programming(2), language(2), released(2), 5000(2)
    word_list = [w[0].lower() for w in top_words]
    assert "programming" in word_list, "高频词应该包含'programming'"
    assert "language" in word_list, "高频词应该包含'language'"
    assert "released" in word_list, "高频词应该包含'released'"


# ============== 测试4：结构验证 ==============


def test_agent_structure():
    """测试4: Agent结构验证

    验证CodeAgent的初始化和基本结构
    """
    agent = CodeAgent(max_retries=3, max_fix_attempts=2)

    # 验证配置
    assert agent.max_retries == 3, "max_retries配置不正确"
    assert agent.max_fix_attempts == 2, "max_fix_attempts配置不正确"

    # 验证图已编译
    assert agent.compiled_graph is not None, "图应该已编译"

    # 验证图结构可以获取
    graph_structure = agent.get_graph_structure()
    assert graph_structure is not None, "图结构不应该为空"
    assert len(graph_structure) > 0, "图结构字符串不应该为空"


def test_result_structure(agent):
    """测试5: 结果结构验证

    验证Agent.run()返回的结果结构
    """
    result = agent.run("计算1+1", verbose=False)

    # 验证结果包含所有必需的字段
    required_fields = [
        "success",
        "output",
        "code",
        "retry_count",
        "fix_attempts",
        "messages",
        "error",
    ]
    for field in required_fields:
        assert field in result, f"结果应该包含字段: {field}"

    # 验证字段类型
    assert isinstance(result["success"], bool), "success应该是布尔值"
    assert isinstance(result["retry_count"], int), "retry_count应该是整数"
    assert isinstance(result["fix_attempts"], int), "fix_attempts应该是整数"
    assert isinstance(result["messages"], list), "messages应该是列表"
    assert isinstance(result["code"], str), "code应该是字符串"

    # 验证消息列表不为空
    assert len(result["messages"]) > 0, "消息列表不应该为空"

    # 验证至少包含开始消息
    has_start_message = any("[开始]" in msg for msg in result["messages"])
    assert has_start_message, "应该包含开始消息"


# ============== Pytest 配置 ==============


def pytest_configure(config):
    """pytest配置"""
    config.addinivalue_line("markers", "slow: 标记慢速测试（涉及API调用）")
    config.addinivalue_line("markers", "excel: 标记Excel相关测试")
    config.addinivalue_line("markers", "text: 标记文本分析测试")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
