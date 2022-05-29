from Crypto.Util.number import bytes_to_long
import random

flag = bytes_to_long(open("flag.txt", "rb").read())
msg = bytes_to_long(b":roocursion:")

p = 82820875767540480278499859101602250644399117699549694231796720388646919033627
g = 2
a = random.randint(0, p)
b = random.randint(0, p)
s = pow(pow(g, a, p), b, p)

def encrypt(msg):
	return (s*msg) % p

print(f"{p = }")
print(f"{encrypt(flag) = }")
print(f"{encrypt(msg) = }")

# p = 82820875767540480278499859101602250644399117699549694231796720388646919033627
# encrypt(flag) = 26128737736971786465707543446495988011066430691718096828312365072463804029545
# encrypt(msg) = 15673067813634207159976639166112349879086089811595176161282638541391245739514

