# smolagents 测试项目

## 项目结构
```
experiment/
├── custom_provider.py      # 自定义模型提供者，从 config.config 读取配置
├── test_smolagents.py      # 测试代码，测试 CodeAgent 读取 Excel 文件
└── README.md              # 本文档
```

## 配置说明

### 1. API 密钥配置

编辑项目根目录下的 `config.config` 文件，填入你的 GLM-4 API 信息：

```ini
[smolagents]
base_url = https://open.bigmodel.cn/api/paas/v4
api_key = your_actual_api_key_here
model_id = glm-4
```

**注意**：将 `your_actual_api_key_here` 替换为你的智谱 AI (Zhipu AI) API key。

### 2. 如何获取 API Key

1. 访问智谱 AI 开放平台：https://open.bigmodel.cn/
2. 注册并登录账号
3. 在控制台中创建 API Key
4. 将 API Key 复制到 `config.config` 文件中

## 运行测试

配置完成后，运行以下命令：

```bash
uv run python experiment/test_smolagents.py
```

## 功能说明

### custom_provider.py
- 从 `config.config` 读取 GLM-4 API 配置
- 返回配置好的 `OpenAIModel` 实例
- 支持自定义 base_url 和 model_id

### test_smolagents.py
- 使用自定义的模型提供者创建 CodeAgent
- 要求 agent 编写 Python 代码读取 Excel 文件
- 读取 `D:\Code\DataAgent\ExcelData\Covid Dashboard.xlsx` 的 Sheet1 工作表
- 提取并返回第一行的数据

## 测试任务说明

测试代码会给 CodeAgent 下达以下任务：

```
请编写 Python 代码读取 Excel 文件 'D:\Code\DataAgent\ExcelData\Covid Dashboard.xlsx' 中的 Sheet1 工作表的全部数据。
使用 pandas 或 openpyxl 读取数据，并返回第一行的内容。

要求：
1. 使用 pandas 或 openpyxl 读取 Excel 文件
2. 获取 Sheet1 工作表
3. 提取第一行的所有列数据
4. 使用 final_answer 返回结果
```

## 依赖项

- smolagents >= 1.23.0
- openai (通过 smolagents[openai] 安装)
- openpyxl (项目中已安装)
- pandas (项目中已安装)

## 预期输出

成功运行后，agent 将：
1. 生成 Python 代码读取 Excel 文件
2. 执行代码提取第一行数据
3. 返回第一行的内容，类似：
   ```
   ['列1', '列2', '列3', ...]
   ```
