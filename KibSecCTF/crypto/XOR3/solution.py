from Crypto.Util.strxor import strxor

k1 = b'this_is_one_key1'
k2 = b'this_another_one'
#k3 = ?

message = b'xor_is_so_cool!!'
mk1 = strxor(message, k1)
mk2 = strxor(mk1, k2)
print(mk2)
#xor_result = strxor(strxor(strxor(message, k1), k2), k3)
xor_res = bytes.fromhex("0c071b2c00081d371c3c3c36330f4411")

k3 = strxor(xor_res, mk2)
print(k3)
#print(xor_result.hex())
# 0c071b2c00081d371c3c3c36330f4411
