# https://archives.sector.ca/presentations17/Eric-Evenchick-REAutoDiag.pdf
with open('./candump.log', 'r') as f:
    fr = f.read()
data = [x.split(' ')[2].split('#')[1] for x in fr.split('\n')[:-1]][10: -4]
#data = ''.join([x[2:].split('7D')[0] for x in data])
key = ''
for i in range(len(data)):
    #print(i, data[i], bytes.fromhex(data[i][2:]))
    if '7D' in data[i]:
        tmp = data[i].split('7D')   # ????
        key += tmp[0][2:] + '4242' + tmp[1][2:]
    else:
        key += data[i][2:]

import base64
key = bytes.fromhex(key)
print(key.decode())
with open('./result1.bin', 'wb') as f1:
    f1.write(key)

#print(base64.b64decode(b''.join(key.split(b'\n')[1:-1])).hex())
