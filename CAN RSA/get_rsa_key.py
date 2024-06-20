from Crypto.PublicKey import RSA

rsa = RSA.generate(1024)
sk = rsa.exportKey()
pk = rsa.publickey().exportKey()

with open ('./pub.pem', 'wb') as f:
    f.write(pk)

with open ('./priv.pem', 'wb') as f:
    f.write(sk)