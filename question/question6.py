money = int(input("輸入金額: "))

fifty = money//50
fifty_left = money%50

ten = fifty_left//10
ten_left = fifty_left%10

five = ten_left//5
five_left = ten_left%5

one = five_left

print(fifty)
print(ten)
print(five)
print(one)