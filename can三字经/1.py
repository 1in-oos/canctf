from collections import defaultdict

# 定义一个函数来解析CAN消息
def parse_can_message(line):
    parts = line.split()
    timestamp = float(parts[0][1:-1])
    interface = parts[1]
    can_info = parts[2].split('#')
    can_id = int(can_info[0], 16)
    data_bytes = can_info[1]
    return {
        'timestamp': timestamp,
        'interface': interface,
        'can_id': can_id,
        'data_bytes': data_bytes
    }

# 打开原始的can.log文件和要输出的sorted_can.log文件
input_file = 'candump.log'
output_file = 'sorted_can.log'

# 读取原始can.log文件并解析CAN消息
parsed_messages = []
with open(input_file, 'r') as f:
    for line in f:
        message = parse_can_message(line.strip())
        parsed_messages.append(message)

# 按CAN ID分类和排序
grouped_messages = defaultdict(list)
for msg in parsed_messages:
    grouped_messages[msg['can_id']].append(msg)

# 对每个CAN ID组内的消息按时间戳排序
for can_id, messages in grouped_messages.items():
    grouped_messages[can_id] = sorted(messages, key=lambda x: x['timestamp'])

# 将排序后的消息写入sorted_can.log文件
with open(output_file, 'w') as f:
    for can_id, messages in grouped_messages.items():
        for msg in messages:
            f.write(f"({msg['timestamp']}) {msg['interface']} {can_id:#X}#{msg['data_bytes']}\n")

print(f"排序后的消息已经写入到 {output_file} 文件中。")
