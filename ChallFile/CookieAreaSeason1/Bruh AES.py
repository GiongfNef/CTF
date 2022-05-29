import base64
from Crypto.Cipher import AES

#flag = ###FINDME###
algorithm = AES.MODE_CBC
key = 'supersecretkey!?'
iv_part1 = "0xcafedeadbeef"
iv_part2 = ###FINDME###""
iv = iv_part1 + iv_part2
#assert(len(flag)) == 38

def encrypt(payload, key, iv):
    return AES.new(key, algorithm, iv).encrypt(r_pad(payload))

def r_pad(payload, block_size=16):
    length = block_size - (len(payload) % block_size)
    return payload + chr(length) * length

with open('cipher.txt', 'wb') as f:
    f.write(encrypt(flag, key, iv))
