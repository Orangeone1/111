from chardet import detect
from os.path import isfile
count,blanks=0,0
with open("a.txt",'rb') as fp:
	#检测文件编码，编码信息保存为code
	code=detect(fp.read())['encoding']
	print(code)

with open("a.txt",'r',encoding=code) as fp:
	while True:
		line = fp.readline()
		if not line:
			break
		if len(line.strip())==0:
			blanks+=1
		#print(len(line.strip()))
		count+=1
print(count,blanks)
path=r"C:\Users\Administrator\.android\ty.txt"
print(isfile(path))