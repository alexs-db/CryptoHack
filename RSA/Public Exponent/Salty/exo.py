from Crypto.Util.number import inverse, long_to_bytes

ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485

flag = long_to_bytes(ct)

print(flag)
