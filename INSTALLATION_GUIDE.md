# 代码生成工具 - 安装和使用指南

## 📦 已完成的工作

### 1. 创建的文件

```
D:\code\DataAgent\
├── Script/
│   ├── custom_provider.py              # 公有配置读取函数
│   └── generate_code/
│       ├── __init__.py                # 导出 generate_code 函数
│       ├── generator.py               # 核心实现
│       ├── test_generator.py          # 测试套件
│       ├── examples.py               # 使用示例
│       └── README.md                # 详细文档
└── test_generate_code.py            # 快速测试脚本
```

### 2. 修改的文件

- `pyproject.toml` - 添加了 `pydantic-ai>=0.0.0` 依赖

### 3. 已安装的依赖

运行 `uv sync` 已安装了以下依赖：
- pydantic-ai==1.42.0 ✅
- 以及其他 169 个依赖包

## ⚠️ 重要提示：配置 API Key

### 当前状态

`config.example` 文件内容：
```ini
GLM_API = your_api_key_here  # ⚠️ 需要替换为实际的 API Key
GLM_BASE_URL = https://open.bigmodel.cn/api/coding/paas/v4
GLM_MODEL = GLM-4.7
```

### 配置步骤

#### 方式 1: 创建 config.config（推荐）

```bash
# 复制配置模板
cd D:\code\DataAgent
copy config.example config.config

# 编辑 config.config，填入实际的 API Key
```

编辑 `config.config`：
```ini
GLM_API = sk-xxxxxxxxxxxxxxxx  # 替换为你的实际 API Key
GLM_BASE_URL = https://open.bigmodel.cn/api/coding/paas/v4
GLM_MODEL = GLM-4.7
```

#### 方式 2: 直接修改 config.example（快速测试）

```bash
# 直接编辑 config.example，填入 API Key
```

### 获取 API Key

1. 访问智谱 AI 开放平台：https://open.bigmodel.cn/
2. 注册并登录账号
3. 在控制台中创建 API Key
4. 将 API Key 复制到配置文件中

## 🚀 快速开始

### 1. 验证配置

确保已配置 API Key 后，运行快速测试：

```bash
cd D:\code\DataAgent
uv run python test_generate_code.py
```

### 2. 基本使用

```python
from Script.generate_code import generate_code

# 生成代码
code = generate_code("计算斐波那契数列前10项")
print(code)
```

### 3. 生成并执行

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

## 📚 更多示例

### 运行完整测试套件

```bash
cd D:\code\DataAgent
uv run python Script/generate_code/test_generator.py
```

### 运行示例代码

```bash
cd D:\code\DataAgent
uv run python Script/generate_code/examples.py
```

## 🔍 功能特性

### ✅ 已实现

1. **AI 驱动代码生成**
   - 使用 pydantic-ai 框架
   - 调用 GLM-4 模型
   - 复用现有 GLM 配置

2. **环境约束遵循**
   - 严格限制可用模块
   - 禁止危险函数
   - 遵守执行限制

3. **单函数生成**
   - 生成简洁的工具函数
   - 包含清晰的文档字符串
   - 添加必要的错误处理

4. **自动验证**
   - 检测禁止的模块
   - 检测禁止的函数
   - 提供警告信息

5. **与 AICodeExecutor 集成**
   - 生成的代码可直接执行
   - 支持变量注入
   - 返回标准化的结果格式

### 📋 环境约束

#### 可用模块
```
math, re, datetime, collections, itertools, random, statistics
pandas, openpyxl, tabulate
```

#### 禁止使用
- 模块: os, sys, subprocess, pathlib, socket, builtins
- 函数: eval(), exec(), compile(), __import__()

#### 执行限制
- 最大操作数: 10,000,000
- print 输出限制: 50,000 字符

## 🎯 使用场景

### 场景 1: 数学计算

```python
code = generate_code("计算1到100的平方和")
executor = AICodeExecutor()
result = executor.execute(code)
```

### 场景 2: 数据处理

```python
code = generate_code("""
创建一个DataFrame，包含学生姓名和成绩，
计算平均分并找出最高分学生
""")
executor = AICodeExecutor()
result = executor.execute(code)
```

### 场景 3: Excel 处理

```python
code = generate_code("""
读取Excel文件，统计每列的非空值数量
""")
executor = AICodeExecutor()
result = executor.execute(code, variables={'file_path': 'data.xlsx'})
```

### 场景 4: 字符串处理

```python
code = generate_code("""
统计文本中的单词数量、字母数量和数字数量
""")
executor = AICodeExecutor()
result = executor.execute(code)
```

## 🐛 故障排除

### 问题 1: API Key 配置错误

**症状**: 提示 "代码生成失败: AuthenticationError"

**解决**:
1. 检查 `config.example` 或 `config.config` 中的 API Key
2. 确认 API Key 格式正确（通常以 `sk-` 开头）
3. 访问智谱 AI 控制台验证 API Key 是否有效

### 问题 2: 生成的代码执行失败

**症状**: `result['success']` 为 False

**解决**:
1. 查看 `result['error']` 了解具体错误
2. 检查是否超出了执行限制（如无限循环）
3. 验证生成的代码使用了正确的模块

### 问题 3: 依赖安装失败

**症状**: 运行 `uv sync` 时出错

**解决**:
```bash
# 清除缓存重新安装
cd D:\code\DataAgent
uv sync --reinstall
```

### 问题 4: 导入错误

**症状**: `ModuleNotFoundError: No module named 'pydantic_ai'`

**解决**:
```bash
# 确保在正确的虚拟环境中
cd D:\code\DataAgent
uv sync
uv run python your_script.py
```

## 📖 进一步阅读

- 详细文档: `Script/generate_code/README.md`
- 代码执行器文档: `Script/codebox/README.md`
- Pydantic-AI 文档: https://ai.pydantic.dev/

## 🎉 总结

### 已完成
✅ 创建 `Script/custom_provider.py` - 公有配置读取函数
✅ 创建 `Script/generate_code/` 目录结构
✅ 实现核心 `generate_code()` 函数
✅ 添加 pydantic-ai 依赖
✅ 安装所有依赖包
✅ 创建测试套件
✅ 创建使用示例
✅ 编写详细文档

### 下一步
1. **配置 API Key** - 复制 config.example 为 config.config 并填入 API Key
2. **运行测试** - 执行 `uv run python test_generate_code.py`
3. **开始使用** - 在您的代码中导入并使用 `generate_code()`

### 预期效果

当正确配置后，您将能够：
- 通过简单的需求描述生成 Python 代码
- 生成的代码严格遵循 AICodeExecutor 环境约束
- 代码可以直接在 AICodeExecutor 中执行
- 代码质量高，包含文档和错误处理

---

**祝您使用愉快！如有问题，请查看故障排除部分或提交 Issue。**
