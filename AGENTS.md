python 环境为UV

## CodeAgent

CodeAgent是一个基于LangGraph的代码生成、执行、修复、验证工作流系统。

### 结构

```
Script/code_agent/
├── __init__.py       # 导出CodeAgent
├── agent.py          # 主Agent类
├── state.py          # 状态定义
├── nodes.py          # 节点实现
├── graph.py          # LangGraph图构建
└── fix_agent.py      # 独立修复Agent
```

### 工作流

```
需求 → 生成 → 执行 → 检查错误 → 验证 → 结束
                     ↓ (错误)
                  修复 → 重新执行
```

### 使用示例

```python
from Script.code_agent import CodeAgent

# 初始化Agent
agent = CodeAgent(max_retries=3, max_fix_attempts=2)

# 运行
result = agent.run(
    requirements="计算斐波那契数列前10项",
    validation_rules=None  # 可选，暂时不启用
)

# 输出
if result["success"]:
    print(f"结果: {result['output']}")
    print(f"重试次数: {result['retry_count']}")
else:
    print(f"错误: {result['error']}")
```

### 测试

项目使用pytest进行测试。

#### 测试方案

采用**组合A**测试方案，共**5个测试案例**：

| # | 测试名称 | 类别 | 描述 |
|---|---------|------|------|
| 1 | `test_fibonacci_simple` | 简单 | 斐波那契数列 |
| 2 | `test_excel_statistics` | 复杂-Excel | Excel数据统计 |
| 3 | `test_text_analysis` | 复杂-文本 | 文本分析 |
| 4 | `test_agent_structure` | 结构 | Agent结构 |
| 5 | `test_result_structure` | 结构 | 结果结构 |

#### 测试特点

- ✅ 精确值验证：所有测试采用精确值断言
- ✅ 真实场景：使用真实Excel和文本文件
- ✅ 复杂逻辑：Excel和文本测试涵盖复杂业务逻辑
- ✅ 不同方向：覆盖简单算法、Excel处理、文本分析等领域

#### 测试资源

```
tests/resource/
├── test_students.xlsx     # 学生成绩Excel文件（8行7列）
└── test_text.txt          # Python介绍文本（10行99词）
```

#### 安装测试依赖

```bash
uv pip install pytest pytest-cov
```

#### 运行测试

```bash
# 运行所有测试（包括API调用）
uv run pytest tests/ --runslow -v

# 运行特定测试
uv run pytest tests/test_code_agent.py::test_fibonacci_simple --runslow -v
uv run pytest tests/test_code_agent.py::test_excel_statistics --runslow -v
uv run pytest tests/test_code_agent.py::test_text_analysis --runslow -v

# 运行不涉及API的测试
uv run pytest tests/ -m "not slow" -v

# 测试覆盖率
uv run pytest tests/ --runslow --cov=Script --cov-report=html
```

#### 测试文件

- `tests/test_code_agent.py` - 完整测试套件（5个测试）
- `tests/conftest.py` - pytest配置
- `tests/README.md` - 详细的测试使用文档
- `tests/TESTING_SUMMARY.md` - 测试总结

详细说明见 `tests/README.md` 和 `tests/TESTING_SUMMARY.md`

### 依赖

- `langgraph>=0.2.0` - LangGraph框架
- `pydantic-ai>=0.0.0` - AI模型集成
- `pytest>=8.0.0` - 测试框架（开发依赖）
- `pytest-cov>=4.0.0` - 测试覆盖率（开发依赖）
