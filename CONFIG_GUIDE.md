# 配置管理 - 快速开始

## 新的配置方式

我们已将配置管理升级为使用 **python-dotenv**，更简单、更标准、更易用。

## 配置方式

### 方式1: 使用 .env 文件（推荐）

#### 快速配置

运行配置向导：

```bash
cd D:\code\DataAgent
uv run python setup_config.py
```

按提示选择"1. 创建 .env 文件"，填入你的 API Key。

#### 手动配置

1. 复制配置模板：
```bash
cd D:\code\DataAgent
copy .env.example .env
```

2. 编辑 `.env` 文件，填入你的配置：

```bash
# GLM API 配置
# GLM API 密钥（必填）
GLM_API=your_actual_api_key_here

# GLM API 基础 URL（可选）
GLM_BASE_URL=https://open.bigmodel.cn/api/coding/paas/v4

# 模型名称（可选）
GLM_MODEL=GLM-4.7
```

### 方式2: 使用环境变量（临时）

设置环境变量（仅当前会话有效）：

**Windows (CMD):**
```cmd
set GLM_API=your_api_key_here
set GLM_BASE_URL=https://open.bigmodel.cn/api/coding/paas/v4
set GLM_MODEL=GLM-4.7
```

**Windows (PowerShell):**
```powershell
$env:GLM_API="your_api_key_here"
$env:GLM_BASE_URL="https://open.bigmodel.cn/api/coding/paas/v4"
$env:GLM_MODEL="GLM-4.7"
```

**Linux/Mac:**
```bash
export GLM_API=your_api_key_here
export GLM_BASE_URL=https://open.bigmodel.cn/api/coding/paas/v4
export GLM_MODEL=GLM-4.7
```

### 方式3: 代码中设置（临时）

```python
from Script.custom_provider import set_glm_config

# 设置配置（仅当前 Python 进程）
set_glm_config(
    api_key="your_api_key_here",
    base_url="https://open.bigmodel.cn/api/coding/paas/v4",
    model="GLM-4.7"
)
```

### 方式4: 保存配置到文件

```python
from Script.custom_provider import save_glm_config

# 保存到 .env 文件
save_glm_config(
    api_key="your_api_key_here",
    base_url="https://open.bigmodel.cn/api/coding/paas/v4",
    model="GLM-4.7"
)
```

## 配置优先级

配置读取按以下优先级：

1. **环境变量**（最高优先级）
2. **.env 文件**
3. **默认值**（最低优先级）

## 验证配置

运行配置验证：

```bash
cd D:\code\DataAgent
uv run python setup_config.py --verify
```

或使用 Python 代码：

```python
from Script.custom_provider import get_glm_config

api_key, base_url, model = get_glm_config()

print(f"API Key: {api_key[:10] if api_key else 'Not configured'}...")
print(f"Base URL: {base_url}")
print(f"Model: {model}")
```

## 获取 API Key

1. 访问智谱 AI 开放平台：https://open.bigmodel.cn/
2. 注册并登录账号
3. 在控制台中创建 API Key
4. 将 API Key 复制到配置文件

## 安全说明

- `.env` 文件已添加到 `.gitignore`，不会提交到 Git
- 不要将 `.env` 文件分享给他人
- 不要在公开代码中包含 API Key
- 定期更换 API Key

## 配置示例

### 开发环境（.env）

```bash
# .env 文件内容
GLM_API=sk-dev-api-key-123456
GLM_BASE_URL=https://open.bigmodel.cn/api/coding/paas/v4
GLM_MODEL=GLM-4
```

### 生产环境（环境变量）

```bash
# 生产环境脚本
export GLM_API=sk-prod-api-key-789012
export GLM_BASE_URL=https://open.bigmodel.cn/api/coding/paas/v4
export GLM_MODEL=GLM-4.7
```

### 测试环境（代码设置）

```python
# 测试代码
from Script.custom_provider import set_glm_config

set_glm_config(api_key="sk-test-api-key-345678")
```

## 故障排除

### 问题1: 配置未生效

**检查步骤**:

1. 验证 .env 文件是否存在：
```bash
dir .env
```

2. 检查 .env 文件内容：
```bash
type .env
```

3. 验证配置读取：
```bash
uv run python setup_config.py --verify
```

### 问题2: API Key 错误

**可能原因**:
- API Key 复制不完整
- API Key 已过期
- API Key 格式错误

**解决方法**:
- 重新从智谱 AI 控制台复制 API Key
- 确保没有多余空格
- 确认 API Key 以 `sk-` 开头

### 问题3: 环境变量未生效

**可能原因**:
- 环境变量设置错误
- Python 进程已启动，环境变量未加载

**解决方法**:
- 重新启动终端
- 在启动 Python 前设置环境变量
- 使用 .env 文件替代环境变量

## 配置管理 API

### Script.custom_provider

可用的配置管理函数：

#### get_glm_config()

读取 GLM 配置。

```python
from Script.custom_provider import get_glm_config

api_key, base_url, model = get_glm_config()
```

#### set_glm_config(api_key, base_url, model)

设置 GLM 配置到环境变量（仅当前会话）。

```python
from Script.custom_provider import set_glm_config

set_glm_config(
    api_key="your_api_key",
    base_url="https://open.bigmodel.cn/api/coding/paas/v4",
    model="GLM-4.7"
)
```

#### save_glm_config(api_key, base_url, model, env_file)

保存 GLM 配置到 .env 文件。

```python
from Script.custom_provider import save_glm_config

save_glm_config(
    api_key="your_api_key",
    base_url="https://open.bigmodel.cn/api/coding/paas/v4",
    model="GLM-4.7"
)
```

## 从旧配置迁移

如果你之前使用 `config.config` 或 `config.example`，可以迁移到新的 `.env` 格式：

### 自动迁移

```python
from Script.custom_provider import save_glm_config

# 保存到 .env 文件
save_glm_config(
    api_key="your_old_api_key",
    base_url="https://open.bigmodel.cn/api/coding/paas/v4",
    model="GLM-4.7"
)
```

### 手动迁移

1. 打开旧的 `config.config` 或 `config.example`
2. 复制 `GLM_API` 的值
3. 创建或编辑 `.env` 文件
4. 粘贴到 `GLM_API=` 后面
5. 复制其他配置项

## 示例代码

### 读取配置

```python
from Script.custom_provider import get_glm_config

api_key, base_url, model = get_glm_config()

print(f"使用模型: {model}")
print(f"API 地址: {base_url}")
```

### 生成代码

```python
from Script.generate_code import generate_code

# 使用配置自动加载
code = generate_code("计算斐波那契数列前10项")

print(code)
```

### 完整示例

```python
from Script.custom_provider import get_glm_config
from Script.generate_code import generate_code
from Script.codebox import AICodeExecutor

# 1. 读取配置
api_key, base_url, model = get_glm_config()
print(f"使用模型: {model}")

# 2. 生成代码
code = generate_code("生成一个函数，计算列表的平均值")

# 3. 执行代码
executor = AICodeExecutor()
result = executor.execute(code)

# 4. 显示结果
if result["success"]:
    print(f"结果: {result['output']}")
else:
    print(f"错误: {result['error']}")
```

## 常见问题

### Q: 我应该使用哪种配置方式？

**A:**
- **开发**: 使用 `.env` 文件（推荐）
- **生产**: 使用环境变量
- **测试**: 使用代码设置

### Q: .env 文件会被提交到 Git 吗？

**A:** 不会。`.env` 已添加到 `.gitignore`。

### Q: 如何切换不同的配置？

**A:**
- 创建多个 `.env` 文件（如 `.env.dev`, `.env.prod`）
- 手动重命名需要的文件为 `.env`
- 或使用环境变量覆盖特定配置

### Q: 配置文件放在哪里？

**A:** 默认放在项目根目录（`D:\code\DataAgent\.env`）。

### Q: 我可以在不同的项目中使用同一个配置吗？

**A:** 可以，将 `.env` 文件复制到其他项目，或使用环境变量。

---

**需要帮助？** 查看故障排除部分或提交 Issue。
