from Crypto.Util.number import inverse, long_to_bytes


n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373


# To compute primes of n I use Internet because the program did not give me the answer due to a too big value of n to compute


# primes
p = 752708788837165590355094155871
q = 986369682585281993933185289261

# compute phi
phi = (p - 1) * (q - 1)

# print(phi)


# compute private key 
d = inverse(e, phi)

# print(d)


# Ddecoding message
pt = pow(ct, d, n)
flag = long_to_bytes(pt)

print("Flag :", flag.decode())
