# DataAgent

一个专门针对 Excel 数据清洗的 AI Agent 库，提供高效、可靠的 Excel 数据处理和转换功能。

## 特性

- **合并单元格处理**：自动处理 Excel 中的合并单元格，将值填充到所有相关单元格
- **Markdown 转换**：将 Excel 工作表转换为标准的 Markdown 表格格式
- **批量处理**：支持一次性转换 Excel 文件中的所有工作表
- **保留数据完整性**：确保数据在转换过程中不会丢失或损坏
- **灵活的文件命名**：自动处理特殊字符，生成安全的文件名

## 安装

本项目使用 [uv](https://github.com/astral-sh/uv) 作为包管理器和开发环境工具。

### 环境要求

- Python >= 3.12
- uv (包管理器)

### 安装步骤

```bash
# 克隆项目
git clone <repository-url>
cd DataAgent

# 使用 uv 创建虚拟环境并安装依赖
uv sync

# 激活虚拟环境（可选，uv run 会自动处理）
uv venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/macOS
```

## 快速开始

### Excel 转 Markdown

将 Excel 文件的所有工作表转换为 Markdown 格式：

```python
from Script.excel_to_markdown import convert_excel_to_markdown

# 转换整个 Excel 文件
output_files = convert_excel_to_markdown('path/to/excel.xlsx', 'output/directory')
print(f'生成文件: {output_files}')
```

### 处理合并单元格

单独处理工作表中的合并单元格：

```python
from Script.excel_to_markdown import unmerge_cells
import openpyxl

# 加载工作簿
wb = openpyxl.load_workbook('path/to/excel.xlsx')

# 处理指定工作表的合并单元格
wb = unmerge_cells(wb, 'Sheet1')

# 保存结果
wb.save('output.xlsx')
```

## 项目结构

```
DataAgent/
├── Script/
│   └── excel_to_markdown.py    # Excel 转 Markdown 核心模块
├── ExcelData/                  # Excel 数据目录
├── ExcelData/Structured_MD/    # 转换后的 Markdown 输出目录
├── pyproject.toml             # 项目配置文件
├── uv.lock                    # 依赖锁定文件
└── README.md                  # 项目文档
```

## 核心功能

### 1. 合并单元格处理

`unmerge_cells(wb, sheet_name)` 函数能够：
- 识别工作表中的所有合并单元格
- 提取合并区域的值
- 将值填充到合并区域的所有单元格
- 保持数据的一致性和完整性

### 2. Markdown 转换

`convert_excel_to_markdown(excel_file, output_dir)` 函数提供：
- 自动处理所有工作表
- 保留原始数据结构
- 使用标准的 Markdown 表格格式
- 自动生成安全的文件名

## 开发

### 运行测试

```bash
# 使用 uv 运行脚本
uv run python Script/excel_to_markdown.py

# 或激活虚拟环境后直接运行
python Script/excel_to_markdown.py
```

### 添加新功能

项目采用模块化设计，易于扩展：
- 在 `Script/` 目录下添加新模块
- 在 `pyproject.toml` 中添加所需依赖
- 使用 `uv sync` 同步依赖

## 依赖

- `openpyxl` >= 3.1.5 - Excel 文件读写
- `pandas` >= 2.3.3 - 数据处理
- `tabulate` >= 0.9.0 - 表格格式化

## 注意事项

- 程序会自动隐藏 openpyxl 的条件格式警告
- 合并单元格处理会在临时文件中进行，不会修改原始文件
- 输出目录不存在时会自动创建
- 文件名中的空格和斜杠会被替换为下划线

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
