eee = input("輸入: ")
awa = eee.split(" ")

print("輸出: ", end="")
if(awa[0] > awa[1]):
    print("a 大於 b")
elif(awa[1] > awa[0]):
    print("b 大於 a")
elif(awa[0] == awa[1]):
    print("a 等於 b")

