import libnum
import base64
with open('./result.bin', 'r') as f:
    data = f.read()

key_64 = ''.join(data.split('\n')[1:-1])
key_num = libnum.s2n(base64.b64decode(key_64))
key_hex = hex(key_num)[2:]
print(key_hex)

'''

30819f300d06092a864886f70d010101050003818d0030818902818100a0d154d5bf97c40f7797b44819d09c608fa4b5c38e70d83bc13267138c6eff4c1aacefe3ddb571e1b41d911c7ab6136cf90493189563450e1f4270cabbc4207c54c4da7b84a20311cfbbabe82b9fe60bdf48a08d57839d0cdf9464d84262bcc06bc308095a6987f60ad07d669a312b5a7e4133213788eecf25863248b91349ef0203010001

'''
