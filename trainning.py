'''n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    
    if x < y:
        num1 = x
        num2 = y
    else:
         num2 = x
         num1 = y 
    k = 0
    for num in range(num1 + 1, num2):
        if num % 2 == 0:
            k += 0
        else:
            k += num
    print(k)'''

'''n = int(input())
x = 0
y = 1
print(f"| 0 -- {x} | 1 -- {y} |", end=" ")

for c in range (n):
    k = x + y
    x = y
    y = k
    print(f"{c+2} -- {k} |", end=" ")
'''



'''n = int(input())

for k in range(1, n+1):
    quadrado = k**2
    cubo = k**3
    print(k, quadrado, cubo)
    print(k, quadrado + 1, cubo + 1)'''



'''n = int(input())
x = 0
y = 1
print(x, y, end=" ")
for c in range(n):
    k = x + y
    x = y
    y = k
    print(k, end=" ")'''

'''print("-"*39)
print("|x = 35" + " "*31 + "|")
print("|" + " "*37 + "|")
print("|" + " "*15 + "x = 35" + " "*16 + "|")
print("|" + " "*37 + "|")
print("|" + " "*31 + "x = 35|")
print("-"*39)'''


# -*- coding: utf-8 -*-

print("-"*39)
print("| decimal   |  octal  |  Hexadecimal  |")
print("-"*39)
o = -1
h = -1
for n in range(15):
    
    if o < 8:
        o += 1
    else:
        o = 9
        o += 1
    
    
    if h < 10:
        h += 1
    else:
        h += 1
        h = chr(h + 54).upper()
    
    print(f"|      {n}    |    {o}    |       {h}       |")
    

print("-"*39)