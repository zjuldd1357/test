# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import fileinput
code = []
num = []
result = []
for line in fileinput.input("C:\code\DATA_dsz.txt"):
    data = line.split()
    print (data)
    code.append(data[0])
    num.append(int(data[1]))
    if data[4] != '99':
        result.append(1)
    else:
        result.append(0)
    print (result[-1])

result_file = open(r"C:\code\result.txt","w")
print (len(code))
i=0
tol=1
while 1:
    if num[i]==1:
        result_file.write(str(tol)+' '+code[i]+' '+str(result[i])+'\n')
    else:
        sum = 0
        for j in range(num[i]-1):
            sum += result[i+j]
        if sum:
            result_file.write(str(tol)+' '+code[i]+' '+'1'+'\n')
        else:
            result_file.write(str(tol)+' '+code[i]+' '+'0'+'\n')
    tol+=1
    i+=(num[i])
    if i > len(code) - 1:
        break

result_file.close()