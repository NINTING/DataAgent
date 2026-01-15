"""计算测试文本的预期统计结果"""

import re

text_file = "tests/resource/test_text.txt"

with open(text_file, "r", encoding="utf-8") as f:
    text = f.read()

# 基础统计
lines = text.strip().split("\n")
total_lines = len(lines)

words = text.split()
total_words = len(words)

total_chars = len(text)
total_chars_no_spaces = len(text.replace(" ", "").replace("\n", ""))

# 提取数字
numbers = re.findall(r"\d+", text)
numbers = [int(n) for n in numbers]
total_numbers = len(numbers)
number_average = sum(numbers) / len(numbers) if numbers else 0

# 单词频率（统计长度>3的单词）
word_freq = {}
for word in words:
    word_clean = re.sub(r"[^\w]", "", word.lower())
    if len(word_clean) > 3:
        word_freq[word_clean] = word_freq.get(word_clean, 0) + 1

top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]

print("测试文本预期统计结果:")
print(f"总行数: {total_lines}")
print(f"总单词数: {total_words}")
print(f"总字符数 (含空格): {total_chars}")
print(f"总字符数 (不含空格): {total_chars_no_spaces}")
print(f"提取的数字: {numbers}")
print(f"数字总数: {total_numbers}")
print(f"数字平均值: {number_average}")
print(f"高频词 (前5): {top_words}")
