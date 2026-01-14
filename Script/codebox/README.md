# Codebox - AI代码执行器

基于smolagents的LocalPythonExecutor构建的安全Python代码执行环境，专门用于执行AI生成的代码。

## 功能特性

- ✅ **安全执行环境**：沙箱化执行，限制危险模块和函数
- ✅ **Excel库支持**：内置支持pandas、openpyxl、tabulate等数据处理库
- ✅ **变量注入**：可以向执行环境注入自定义变量
- ✅ **工具注册**：支持注册自定义工具函数
- ✅ **输出捕获**：分离返回值和print输出
- ✅ **错误处理**：友好的错误信息返回

## 安装

本模块是DataAgent项目的一部分，依赖项已在`pyproject.toml`中配置：

```toml
dependencies = [
    "openpyxl>=3.1.5",
    "pandas>=2.3.3",
    "smolagents[openai,toolkit]>=1.23.0",
    "tabulate>=0.9.0",
]
```

## 快速开始

### 基本用法

```python
from Script.codebox import AICodeExecutor

# 创建执行器
executor = AICodeExecutor()

# 执行简单代码
result = executor.execute("""
result = 2 + 3
print("计算完成")
result * 10
""")

# 检查结果
if result["success"]:
    print(f"返回值: {result['output']}")  # 50
    print(f"日志: {result['logs']}")       # "计算完成\n"
else:
    print(f"错误: {result['error']}")
```

### 变量注入

```python
executor = AICodeExecutor()

result = executor.execute(
    code="""
result = data['a'] + data['b']
print(f"计算结果: {result}")
result
    """,
    variables={"data": {"a": 10, "b": 20}}
)

print(result["output"])  # 30
```

### 读取Excel文件

```python
executor = AICodeExecutor()

result = executor.execute("""
import pandas as pd

df = pd.read_excel('path/to/your/excel.xlsx', sheet_name='Sheet1')
print(f"读取到 {len(df)} 行数据")

df.head(3)
""")

if result["success"]:
    print(result["logs"])     # print输出
    print(result["output"])    # DataFrame前3行
```

## API 文档

### AICodeExecutor

#### 构造函数

```python
AICodeExecutor(additional_imports=None)
```

**参数：**
- `additional_imports` (list, 可选): 额外授权导入的模块列表

#### execute 方法

```python
execute(code, variables=None, tools=None, clear_state=True) -> dict
```

**参数：**
- `code` (str): 要执行的Python代码字符串
- `variables` (dict, 可选): 要注入的变量字典
- `tools` (dict, 可选): 要注册的自定义工具字典
- `clear_state` (bool, 可选): 是否清除之前的状态（默认True）

**返回值：**

返回一个字典，包含以下字段：

| 字段 | 类型 | 说明 |
|------|------|------|
| `success` | bool | 是否执行成功 |
| `output` | Any | 代码的返回值 |
| `logs` | str | print输出内容 |
| `is_final_answer` | bool | 是否调用了final_answer |
| `error` | str | None | 错误信息（如果有） |

## 授权导入的模块

默认支持以下模块：

### 基础模块
- `math` - 数学函数
- `re` - 正则表达式
- `datetime` - 日期时间
- `collections` - 集合类型
- `itertools` - 迭代工具
- `random` - 随机数
- `statistics` - 统计函数

### Excel/数据处理
- `pandas` - 数据分析
- `openpyxl` - Excel文件读写
- `tabulate` - 表格格式化

## 安全性

### 禁止的模块

出于安全考虑，以下模块被禁止导入：
- `os` - 操作系统接口
- `sys` - 系统相关
- `subprocess` - 子进程
- `multiprocessing` - 多进程
- `pathlib` - 路径操作
- `socket` - 网络通信
- `builtins` - 内置函数（部分）

### 禁止的函数

- `eval()` - 执行表达式
- `exec()` - 执行代码
- `compile()` - 编译代码
- `__import__()` - 导入模块

## 错误处理

### 语法错误

```python
result = executor.execute("""
if True
    print("缺少冒号")
""")

# result["error"] = "执行错误: Code execution failed at line ..."
```

### 运行时错误

```python
result = executor.execute("""
x = 1 / 0
""")

# result["error"] = "执行错误: ZeroDivisionError: division by zero"
```

### 模块导入错误

```python
result = executor.execute("""
import os
print("这不会执行")
""")

# result["error"] = "执行错误: Import of os is not allowed..."
```

## 高级用法

### 自定义工具

```python
def custom_tool(x, y):
    """自定义工具函数"""
    return x * y + 10

executor = AICodeExecutor()

result = executor.execute(
    code="""
result = custom_tool(5, 3)
print(f"使用工具计算: {result}")
result
    """,
    tools={"custom_tool": custom_tool}
)

print(result["output"])  # 25
```

### 状态管理（已注释）

代码中包含状态管理功能，但已注释。如需在多次执行之间保持变量状态，可以取消注释`code_executor.py`中的相关方法：

```python
# 以下方法已注释，需要时可以启用
executor.get_state()      # 获取当前状态
executor.set_state(state)  # 设置状态
executor.reset_state()     # 重置状态
```

## 测试

运行完整的测试套件：

```bash
cd D:\Code\DataAgent
uv run python Script/codebox/test_executor.py
```

测试覆盖以下场景：
1. 简单的Python代码执行
2. 变量注入
3. Excel文件读取
4. 错误处理（除零错误）
5. 语法错误
6. 禁止的模块导入
7. 多语句执行
8. 数学运算
9. 字符串操作

## 项目结构

```
Script/codebox/
├── __init__.py           # 包初始化
├── code_executor.py      # 核心执行器
├── test_executor.py      # 测试用例
└── README.md            # 本文档
```

## 注意事项

1. **默认清除状态**：每次执行默认清除之前的状态，如需保持状态请设置`clear_state=False`并启用状态管理功能
2. **输出限制**：print输出默认限制为50,000字符
3. **操作限制**：最大操作次数限制为10,000,000次，防止无限循环
4. **编码问题**：Windows环境下建议避免在print输出中使用emoji字符
5. **路径转义**：在代码字符串中使用Windows路径时记得双反斜杠转义

## 常见问题

### Q: 如何添加新的导入模块？

A: 在创建执行器时传入`additional_imports`参数：

```python
executor = AICodeExecutor(additional_imports=["numpy", "matplotlib"])
```

### Q: 如何执行多行代码？

A: 直接传入完整的多行代码字符串即可，支持所有Python语法：

```python
code = """
for i in range(5):
    print(i)
sum(range(5))
"""

result = executor.execute(code)
```

### Q: 如何捕获print输出？

A: print输出会保存在返回结果的`logs`字段中：

```python
result = executor.execute("print('Hello'); 42")
print(result["logs"])  # "Hello\n"
```

## 许可证

MIT License
