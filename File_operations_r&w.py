#!/usr/bin/python

fo=open("test.txt","wb")
file=fo.name
print(file)
print("file open or close",fo.closed)
print("file names is",fo.name)
print("file mode is",fo.mode)
#print("file softspace",fo.softspace)


if file=="test1.txt":
    print("okay")