import glob

file_path='*'
print(glob.glob(file_path))
print('\n')

file_path='*[0-9]'
print(glob.glob(file_path))
print('\n')

file_path='*b'
print(glob.glob(file_path))
print('\n')

file_path='?'
print(glob.glob(file_path))
print('\n')


file_path='*'
generator=glob.iglob(file_path)
for item in generator:
    print(item)
    
    
    
import os
filePath = '.'
for i,j,k in os.walk(filePath):
    print(i,j,k)

filePath = '.'    
print(os.listdir(filePath))
