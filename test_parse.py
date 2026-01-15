"""测试 parse_code_response 函数"""

from Script.generate_code import parse_code_response

# 测试代码解析
response1 = """```python
def test():
    return 42
```"""
code1 = parse_code_response(response1)
print(f"解析结果1:")
print(code1)
print()

response2 = "没有代码块标记的代码"
code2 = parse_code_response(response2)
print(f"解析结果2:")
print(code2)
