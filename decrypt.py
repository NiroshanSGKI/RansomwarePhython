#!usr/bin/env python3

import os
from cryptography.fernet import Fernet

#let's find some files


files=[]

for file in os.listdir():
	if file == "voldermort.py" or file=="thekey.key" or file=="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)



#print(key)

with open("thekey.key","rb") as thekey:
	key = thekey.read()
print(key)

for file in files:
	with open(file,"rb") as thefile:
		content= thefile.read()
		print(content)
	content_decypted= Fernet(key).decrypt(content)
	with open(file,"wb") as thefile:
		thefile.write(content_decypted)
		
