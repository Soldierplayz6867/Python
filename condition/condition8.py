sides = input("輸入: ").split(" ")

a = int(sides[0])
b = int(sides[1])
c = int(sides[2])

avaliable = False

if (a + b > c):
    avaliable = True
    
if (b + c > a):
    avaliable = True

if (c + a > b):
    avaliable = True
    
print('輸出: ', end='')
if (avaliable):
    print('1')
else: 
    print('0')