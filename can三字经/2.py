import re

pattern = re.compile(r'911#03')

with open('candump.log', 'r') as f, open('result', 'wb') as f1:
    list1 = f.readlines()

    for line in list1:
        if pattern.search(line):
            data = line[31:37].strip()  # 根据实际的日志文件格式调整这个切片
            if data:
                try:
                    data_bytes = bytes.fromhex(data)
                    f1.write(data_bytes)
                except ValueError:
                    print(f"将 '{data}' 从十六进制转换为字节时出错。")
            else:
                print("在该行中未找到有效的十六进制数据。")

print("转换并写入文件完成。")
