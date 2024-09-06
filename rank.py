# Read the content of the file
with open('555.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Parse the lines to extract title and result
data = []
for line in lines:
    if line.strip():  # Skip empty lines
        parts = line.strip().split(', ')
        title = parts[0].split(': ')[1].strip("'")
        result = float(parts[1].split(': ')[1].split('}')[0])
        data.append({'title': title, 'result': result})

# Sort the data based on result in descending order
sorted_data = sorted(data, key=lambda x: x['result'], reverse=True)

# Write the sorted data back to a new file
with open('sorted_rank.txt', 'w', encoding='utf-8') as file:
    for item in sorted_data:
        file.write(f"{{'title': '{item['title']}', 'result': {item['result']}}}\n")