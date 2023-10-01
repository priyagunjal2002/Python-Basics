# file objects


# open file
f=open('test.txt','r')                      

print(f.name)
print(f.mode)
f_contents=f.read()
f_contents=f.readlines()

for lines in f:
    print(lines,end='')
    
print(f_contents)
f.close()



f=open('test2.txt','w')
pass
f.write('test.txt')

f=open('test2.txt','w')
f.write('test')
f.seek(0)
# f.write('R')