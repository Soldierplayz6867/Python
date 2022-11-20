n = input("輸入: ").split(" ")
a = n[0]
b = n[1]
c = n[2]


print("輸出: ", end='')
if(a>b or a>c):
    print("a 大")
if(b>a or b>c):
    print("b 大")
if(c>a or c>b):
    print("c 大")