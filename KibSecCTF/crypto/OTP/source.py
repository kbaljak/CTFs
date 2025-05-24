from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
from Crypto.Util.strxor import strxor

known_plaintext = b"Ja sam mislio da FERovci ne vole matematiku!"
flag = b"KibSec{...}"

key = get_random_bytes(16)
iv = get_random_bytes(8)
ctr = Counter.new(64, prefix=iv, initial_value=0, little_endian=False)

cipher1 = AES.new(key, AES.MODE_CTR, counter=ctr)
ciphertext1 = cipher1.encrypt(known_plaintext)

ctr2 = Counter.new(64, prefix=iv, initial_value=0, little_endian=False)
cipher2 = AES.new(key, AES.MODE_CTR, counter=ctr2)
ciphertext2 = cipher2.encrypt(flag)

print(ciphertext1.hex())
print(ciphertext2.hex())
# f87123b5de0d55167724126fd52aad6f56d7399d636e0f0f2375a21bc60d535d035970ea11899adb401be7b8
# f9796195da030e1a7b241b75db6fba6f05e219ae7f6b0d15667ab45ed1075a594649
