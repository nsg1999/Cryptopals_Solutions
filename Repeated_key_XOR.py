def xor(s1,s3):
	return "".join(chr((ord(a)^ord(b))) for a,b in zip(s1,s3)).encode("hex")
  
print("ENTER THE CIPHER:")
s1 = raw_input()

print("ENTER THE KEY:")
s2 = raw_input()

l1 = len(s2)	
l = len(s1)

s3 = (s2) * (l/l1)
print(s3)
ans=""
ans = xor(s1,s3)

print(ans)
