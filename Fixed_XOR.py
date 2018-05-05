string_1 = '1c0111001f010100061a024b53535009181c'
string_2 = '686974207468652062756c6c277320657965'

st1 = string_1.decode("hex")
print("after decoding:string 1 is:")
print(st1)

st2 = string_2.decode("hex")
print("after decoding:string 2 is:")
print(st2)

zip_of_strings = zip(st1,st2)

print("the zip of both the strings:")
print(zip_of_strings)

xor = ''.join(chr(ord(x)^ord(y))for x,y in zip_of_strings)

print("answer without encoding:")
print(xor)

print("THE FINAL XOR OPERATION	:")
print(xor.encode("hex"))
