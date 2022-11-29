a = int(input())
b = int(input())
c = int(input())
t = 0

if a + b == c:
    print(a ,'+', b ,'=', c)
    t +=1
if a - b == c:
    print(a ,'-', b ,'=', c)
    t +=1
if a * b == c:
    print(a ,'*', b ,'=', c)
    t +=1
if (b != 0):
    if (a // b == c):
        print(a ,'//', b ,'=', c)
        t +=1
if t == 0: 
    print('такое невозможно')

