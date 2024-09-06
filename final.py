import pandas as pd

# 读取文件内容
data = []
with open('5556667777.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data.append(line.strip())

# 提取change_ratio并排序
df = pd.DataFrame(data, columns=['line'])
df['change'] = df['line'].apply(lambda x: float(x.split('"change": ')[1]))
df = df.sort_values(by='change', ascending=False)

# 将排序后的内容写入新文件
with open('sorted_555666777.txt', 'w', encoding='utf-8') as file:
    for line in df['line']:
        file.write(line + '\n')

print("文件已成功排序并保存为sorted_555666.txt")
