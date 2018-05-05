import binascii
print("ENTER THE STRING")
input_string = raw_input()
str1 = binascii.unhexlify(input_string)
length = len(str1)

for i in range(0,255):
	str2=""
	for j in range(length):
		str2 += chr(ord(str1[j])^i)
	print(str2)
	
