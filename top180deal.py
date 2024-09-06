with open('top180.txt', 'r', encoding='utf-8') as file:
    data = []
    for line in file:
        data.append(line.strip())

with open('top180afterdeal.txt', 'w', encoding='utf-8') as file:
    for line in data:
        num = line.split(':')[1]
        # num保留4位小数
        num = round(float(num), 4)
        file.write(f'{line.split(":")[0]}: {num}\n')
print("文件已成功处理并保存为top180afterdeal.txt")
