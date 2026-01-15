"""修复拼写错误的脚本"""

import re

# 读取文件
with open(
    "D:/code/DataAgent/Script/generate_code/test_generator.py", "r", encoding="utf-8"
) as f:
    content = f.read()

# 替换所有 AICodeExecutor (不区分大小写）
content = re.sub(r"AICodeExecutor", "AICodeExecutor", content)

# 写回文件
with open(
    "D:/code/DataAgent/Script/generate_code/test_generator.py", "w", encoding="utf-8"
) as f:
    f.write(content)

print("修复完成！")
