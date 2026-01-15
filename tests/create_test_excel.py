"""创建测试用的Excel文件"""

import pandas as pd
import os

# 创建测试数据
data = {
    "姓名": ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十"],
    "年龄": [25, 30, 28, 35, 22, 40, 33, 27],
    "语文": [85, 92, 78, 88, 65, 95, 82, 70],
    "数学": [90, 88, 85, 92, 70, 98, 80, 75],
    "英语": [78, 85, 90, 82, 68, 90, 88, 72],
    "总分": [253, 265, 253, 262, 203, 283, 250, 217],
    "班级": ["A", "A", "B", "A", "B", "A", "B", "A"],
}

df = pd.DataFrame(data)

# 保存Excel文件
excel_path = "tests/resource/test_students.xlsx"
df.to_excel(excel_path, index=False, sheet_name="学生成绩")

print(f"测试Excel文件已创建: {excel_path}")
print(f"数据形状: {df.shape}")
print(f"数据预览:\n{df.head()}")

# 输出预期的统计结果（用于测试验证）
print("\n预期统计结果:")
print(f"数据行数: {len(df)}")
print(f"数据列数: {len(df.columns)}")
print(f"数值列统计:")
for col in ["年龄", "语文", "数学", "英语", "总分"]:
    print(
        f"  {col}: 平均值={df[col].mean():.2f}, 最大值={df[col].max()}, 最小值={df[col].min()}"
    )
