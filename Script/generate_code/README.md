# Generate Code Tool

基于 pydantic-ai 的 Python 代码生成器，专门生成符合 AICodeExecutor 环境约束的单函数工具代码。

## 功能特性

- ✅ **AI 驱动**: 使用 pydantic-ai 调用 GLM-4 模型生成代码
- ✅ **环境适配**: 严格遵循 AICodeExecutor 的模块和约束
- ✅ **单函数生成**: 生成简洁、可复用的单函数工具代码
- ✅ **自动验证**: 验证生成的代码符合环境约束
- ✅ **即用即行**: 生成的代码可直接在 AICodeExecutor 中执行

## 项目结构

```
Script/generate_code/
├── __init__.py           # 导出 generate_code 函数
├── generator.py          # 核心实现
├── test_generator.py     # 测试套件
└── examples.py          # 使用示例

Script/
└── custom_provider.py    # 公有配置读取函数
```

## 安装

依赖已添加到 `pyproject.toml`，运行以下命令安装：

```bash
uv sync
```

## 配置

### 1. 创建配置文件

复制 `config.example` 为 `config.config`：

```bash
cp config.example config.config
```

### 2. 填写 API 配置

编辑 `config.config`，填入你的 GLM API 信息：

```ini
GLM_API = your_actual_api_key_here
GLM_BASE_URL = https://open.bigmodel.cn/api/coding/paas/v4
GLM_MODEL = GLM-4.7
```

**如何获取 API Key**:
1. 访问智谱 AI 开放平台：https://open.bigmodel.cn/
2. 注册并登录账号
3. 在控制台中创建 API Key
4. 将 API Key 复制到 `config.config` 文件中

**注意**: 如果没有创建 `config.config`，系统会自动使用 `config.example`。

## 快速开始

### 基本用法

```python
from Script.generate_code import generate_code

# 生成代码
code = generate_code("计算斐波那契数列前10项")

print(code)
```

### 生成并执行

```python
from Script.generate_code import generate_code
from Script.codebox import AICodeExecutor

# 生成代码
code = generate_code("生成一个函数，计算列表的平均值")

# 在 AICodeExecutor 中执行
executor = AICodeExecutor()
result = executor.execute(code)

if result["success"]:
    print(f"结果: {result['output']}")
else:
    print(f"错误: {result['error']}")
```

## 环境约束

### 可用模块

```
math, re, datetime, collections, itertools, random, statistics
pandas, openpyxl, tabulate
```

### 禁止使用

**禁止的模块**:
- os, sys, subprocess, pathlib, socket, builtins

**禁止的函数**:
- eval(), exec(), compile(), __import__()

### 执行限制

- 最大操作数: 10,000,000
- print 输出限制: 50,000 字符

## 测试

### 快速测试

```bash
uv run python test_generate_code.py
```

### 完整测试套件

```bash
uv run python Script/generate_code/test_generator.py
```

### 运行示例

```bash
uv run python Script/generate_code/examples.py
```

## API 文档

### generate_code(requirements: str) -> str

根据需求生成 Python 代码。

**参数**:
- `requirements` (str): 代码需求描述

**返回值**:
- `str`: 生成的 Python 代码字符串

**示例**:
```python
code = generate_code("创建一个DataFrame并计算平均值")
```

## 使用示例

### 示例 1: 斐波那契数列

```python
from Script.generate_code import generate_code
from Script.codebox import AICodeExecutor

code = generate_code("生成斐波那契数列前10项")

executor = AICodeExecutor()
result = executor.execute(code)

print(result['output'])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### 示例 2: 数据处理

```python
code = generate_code("""
生成一个函数，读取Excel文件并计算某列的平均值
参数: file_path (文件路径), column_name (列名)
""")

executor = AICodeExecutor()
# 注意：需要实际的 Excel 文件
result = executor.execute(code, variables={
    'file_path': 'data.xlsx',
    'column_name': 'score'
})
```

### 示例 3: 数学计算

```python
code = generate_code("计算1到100的整数和")

executor = AICodeExecutor()
result = executor.execute(code)

print(result['output'])  # 5050
```

## 设计原则

1. **精简高效**: 生成单函数代码，避免过度设计
2. **环境适配**: 严格遵循 AICodeExecutor 约束
3. **即时可用**: 生成的代码可直接执行，无需额外修改
4. **安全第一**: 内置验证，防止危险代码
5. **易于维护**: 代码结构清晰，便于理解和修改

## 常见问题

### Q: 为什么生成的代码执行失败？

A: 可能的原因：
1. API Key 配置错误或无效
2. 生成的代码使用了禁止的模块或函数
3. 代码中有语法错误（AI 偶尔会出错）
4. 超过执行限制（如无限循环）

### Q: 如何添加新的可用模块？

A: 编辑 `Script/codebox/code_executor.py`，在 `authorized_imports` 列表中添加模块。

### Q: 生成的代码质量如何保证？

A: 
1. Prompt 中包含明确的编码规范和示例
2. 内置代码验证，检测禁止的模块和函数
3. 可通过在 AICodeExecutor 中执行来验证代码正确性

### Q: 支持哪些模型？

A: 目前支持 GLM-4 系列模型，通过 `GLM_MODEL` 配置项指定。

## 开发指南

### 修改 Prompt

编辑 `Script/generate_code/generator.py` 中的 `CODE_GENERATION_PROMPT` 常量。

### 添加新功能

1. 在 `generator.py` 中添加新的辅助函数
2. 在 `__init__.py` 中导出新函数
3. 在 `test_generator.py` 中添加测试用例

### 调试技巧

```python
from Script.generate_code import generate_code
from Script.codebox import AICodeExecutor

# 生成代码
code = generate_code("你的需求")

# 打印生成的代码
print("生成的代码:")
print(code)

# 在执行器中执行
executor = AICodeExecutor()
result = executor.execute(code)

# 查看详细结果
print(f"成功: {result['success']}")
print(f"输出: {result['output']}")
print(f"日志: {result['logs']}")
if result['error']:
    print(f"错误: {result['error']}")
```

## 依赖项

- pydantic-ai>=0.0.0
- openpyxl>=3.1.5
- pandas>=2.3.3
- smolagents[openai,toolkit]>=1.23.0
- tabulate>=0.9.0

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
