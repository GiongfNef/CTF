from Crypto.Util.number import getPrime
import math

# string to decimal
pt = int(open('flag.txt','rb').read().hex(),16);

primes = [];
n = 1
# euler totient
phi = 1
# public key
e = 65537

while math.log2(n) < 640:
	primes.append(getPrime(32));
	n *= (primes[-1]);
	phi *= (primes[-1] - 1);

# No duplicates
assert(len(primes) == len(list(set(primes))));
# private key
d = pow(e,-1,phi);
# cipher text
ct = pow(pt,e,n);

def decrypt(ct):
	# decode ciphertext for plaintext
	pt = pow(ct,d,n);
	# convert decimal back to string
	return bytes.fromhex(hex()[2:]).decode("utf-8");

print("n = " + str(n));
print("e = 65537");
print("ct = " + str(ct));
#n = 10588750243470683238253385410274703579658358849388292003988652883382013203466393057371661939626562904071765474423122767301289214711332944602077015274586262780328721640431549232327069314664449442016399
#e = 65537
#ct = 5995952936037255929781924635247478684210608634033130708312547257115162490907542249878843535087479397093661825467058312432783733583919194527896596274111265902276347768535338414466405501311805051241244
