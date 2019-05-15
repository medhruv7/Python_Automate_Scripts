import shutil,os,sys
from shutil import copy
os.chdir("C:\\Users\\Ranjit\\Desktop\\")

val = ['a','b','c','d','e','f']

path = 'C:\\Users\\Ranjit\\Desktop\\cpp\\'

name = '_'.join(sys.argv[1:])

path += name


os.makedirs(path)
src = 'C:\\Users\\Ranjit\\Desktop\\cpp\\start.cpp'

for i in val:
    des = path
    des += '\\'
    des += i
    des += '.cpp'
    copy(src,des)