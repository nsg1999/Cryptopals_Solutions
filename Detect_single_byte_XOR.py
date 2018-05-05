import binascii
file1 = open("ques4.txt" , "r")

l1=""
l2=""
str1=""

for i in range(327):
	for j in range(0,255):
		 l1 +=(file1.readline())
		 l2 +=line[:-1].decode("hex")
	 	 str1+=chr(ord(l2[i]^j))
	print(str1) 	 	 
