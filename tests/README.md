# CodeAgent 测试文档

## 测试框架

本项目使用 **pytest** 作为测试框架。

## 测试案例

项目采用**组合A**测试方案，共**5个测试案例**，覆盖不同方向和复杂度。

### 测试案例清单

| # | 测试名称 | 类别 | 描述 | 验证方式 |
|---|---------|------|------|---------|
| 1 | `test_fibonacci_simple` | 简单 | 斐波那契数列 | 精确值验证 |
| 2 | `test_excel_statistics` | 复杂-Excel | Excel数据统计 | 精确值验证 |
| 3 | `test_text_analysis` | 复杂-文本 | 文本分析 | 精确值验证 |
| 4 | `test_agent_structure` | 结构 | Agent结构 | 配置验证 |
| 5 | `test_result_structure` | 结构 | 结果结构 | 类型验证 |

---

## 测试详情

### 1. 简单案例：斐波那契数列

**目的**：验证CodeAgent基础功能，能够生成和执行简单的算法代码

**需求**：
```
生成一个函数，计算斐波那契数列前10项
```

**预期输出**：
```python
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**验证点**：
- ✅ 执行成功
- ✅ 输出类型为列表
- ✅ 输出长度为10
- ✅ 精确匹配斐波那契数列

---

### 2. 复杂案例（Excel方向）：Excel数据统计

**目的**：验证CodeAgent能够读取外部Excel文件并执行复杂的数据分析

**需求**：
```
读取Excel文件 'tests/resource/test_students.xlsx' 并进行以下统计分析：
1. 计算数据行数和列数
2. 对数值列（年龄、语文、数学、英语、总分）计算平均值、最大值、最小值
3. 返回结构化的统计结果
```

**测试文件**：`tests/resource/test_students.xlsx`
- 8名学生数据
- 7列：姓名、年龄、语文、数学、英语、总分、班级

**预期输出**：
```python
{
    "数据行数": 8,
    "数据列数": 7,
    "年龄统计": {"平均值": 30.0, "最大值": 40, "最小值": 22},
    "语文统计": {"平均值": 81.875, "最大值": 95, "最小值": 65},
    "数学统计": {"平均值": 84.75, "最大值": 98, "最小值": 70},
    "英语统计": {"平均值": 81.625, "最大值": 90, "最小值": 68},
    "总分统计": {"平均值": 248.25, "最大值": 283, "最小值": 203}
}
```

**验证点**：
- ✅ 执行成功
- ✅ 读取Excel文件成功
- ✅ 数据行数精确匹配（8）
- ✅ 数据列数精确匹配（7）
- ✅ 各列统计值精确匹配（平均值允许±0.1误差）
- ✅ 输出结构正确

---

### 3. 复杂案例（文本方向）：文本分析

**目的**：验证CodeAgent能够处理文本数据，使用正则表达式，并执行复杂的文本分析

**需求**：
```
读取文本文件 'tests/resource/test_text.txt' 并进行以下分析：
1. 统计总行数、总单词数、总字符数
2. 使用正则表达式提取所有数字
3. 计算数字的平均值
4. 统计单词频率（长度>3的单词）
5. 返回频率最高的5个单词
```

**测试文件**：`tests/resource/test_text.txt`
- 10行文本
- 关于Python编程的介绍
- 包含16个数字

**预期输出**：
```python
{
    "总行数": 10,
    "总单词数": 99,
    "总字符数_含空格": 594,
    "总字符数_不含空格": 495,
    "提取的数字": [1991, 2001, 2, 0, 2000, 3, 0, 2008, 5000, 2023, 19, 1000, 5000, 3, 12, 0],
    "数字个数": 16,
    "数字平均值": 1316.375,
    "高频词_前5": [("python", 10), ("programming", 2), ("language", 2), ("released", 2), ("5000", 2)]
}
```

**验证点**：
- ✅ 执行成功
- ✅ 读取文本文件成功
- ✅ 基础统计精确匹配（行数、单词数、字符数）
- ✅ 数字提取精确匹配（16个数字）
- ✅ 数字平均值匹配（允许±1误差）
- ✅ 高频词精确匹配（'python'出现10次）

---

### 4. 结构验证：Agent结构

**目的**：验证CodeAgent的初始化和基本配置

**验证点**：
- ✅ max_retries配置正确
- ✅ max_fix_attempts配置正确
- ✅ 图已编译
- ✅ 图结构可获取

---

### 5. 结构验证：结果结构

**目的**：验证Agent.run()返回的结果结构完整性

**验证点**：
- ✅ 包含所有必需字段（success, output, code, retry_count, fix_attempts, messages, error）
- ✅ 字段类型正确
- ✅ 消息列表不为空
- ✅ 包含开始消息

---

## 运行测试

### 安装依赖

```bash
# 安装pytest和pytest-cov
uv pip install pytest pytest-cov
```

### 运行所有测试

```bash
# 运行所有测试（包括涉及API的慢速测试）
uv run pytest tests/ --runslow -v
```

### 运行特定测试

```bash
# 运行简单案例
uv run pytest tests/test_code_agent.py::test_fibonacci_simple -v

# 运行Excel测试
uv run pytest tests/test_code_agent.py::test_excel_statistics -v

# 运行文本分析测试
uv run pytest tests/test_code_agent.py::test_text_analysis -v

# 运行结构验证测试
uv run pytest tests/test_code_agent.py::test_agent_structure -v
```

### 按标记运行

```bash
# 只运行Excel相关测试
uv run pytest tests/ -m excel -v

# 只运行文本分析测试
uv run pytest tests/ -m text -v

# 只运行结构验证测试（不涉及API）
uv run pytest tests/ -m "not slow" -v
```

### 测试覆盖率

```bash
# 生成覆盖率报告
uv run pytest tests/ --runslow --cov=Script --cov-report=html

# 命令行覆盖率
uv run pytest tests/ --runslow --cov=Script --cov-report=term-missing
```

---

## 测试资源

### 测试文件结构

```
tests/
├── resource/
│   ├── test_students.xlsx     # 学生成绩Excel文件
│   └── test_text.txt          # Python介绍文本
├── create_test_excel.py       # 创建Excel文件的脚本
├── calculate_text_stats.py    # 计算文本统计的脚本
└── test_code_agent.py         # 测试代码
```

### 测试文件生成

如果需要重新生成测试文件：

```bash
# 生成Excel测试文件
uv run python tests/create_test_excel.py

# 计算文本统计
uv run python tests/calculate_text_stats.py
```

---

## 编写新测试

### 基本模板

```python
@pytest.mark.slow
def test_your_test(agent, resource_path):
    """测试描述"""
    # 准备测试数据或文件
    test_file = os.path.join(resource_path, "your_file.xlsx")
    
    # 构建需求
    requirements = f"""
    读取文件 '{test_file}' 并...
    """
    
    # 运行Agent
    result = agent.run(requirements, verbose=False)
    
    # 验证结果
    assert result["success"], f"执行失败: {result.get('error')}"
    assert result["output"] is not None, "输出为空"
    # 更多验证...
```

### 验证原则

1. **精确值验证**：对于确定性的计算结果，精确断言
2. **类型验证**：验证输出类型和结构
3. **误差容忍**：浮点数比较使用±误差范围
4. **结构完整性**：验证输出包含所有必需字段

---

## 常见问题

### 测试超时

某些测试（涉及API调用）可能需要较长时间。如果超时，可以：
- 增加超时时间：`pytest --timeout=300`
- 只运行非API测试：`pytest -m "not slow"`

### Excel文件路径问题

确保在项目根目录运行测试，Excel文件使用相对路径：
```python
excel_file = os.path.join(resource_path, "test_students.xlsx")
```

### 精度问题

对于浮点数计算，使用误差容忍：
```python
assert abs(actual - expected) < 0.01, "浮点数比较"
```

---

## 设计理念

### 测试策略

- **简单案例**：验证基础功能，快速迭代
- **复杂案例-Excel**：验证外部数据调用能力
- **复杂案例-文本**：验证不同领域的复杂逻辑
- **结构验证**：确保代码质量

### 精确验证

所有测试案例都采用精确值验证，避免模糊断言：
- 数字精确匹配
- 字符串精确匹配
- 结构精确验证

### 真实场景

使用真实的测试文件，模拟实际使用场景：
- Excel文件：真实的学生成绩数据
- 文本文件：真实的Python介绍文本

---

## 下一步

- [ ] 考虑添加Mock测试，避免实际API调用
- [ ] 添加性能测试
- [ ] 添加更多Excel相关的测试场景
- [ ] 添加数据库操作的测试场景
