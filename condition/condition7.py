# 如果 18 歲以上，就輸出賣出電影票如果 18 歲以上，就 " 賣出電影票 "
# 否則 " 不能賣出電影票 " 
# 如果 60 歲以上，敬老票 1000; 
# 小於 60 歲 18 歲以上成人票 1800
# 並加入點數是否大於 5，提供 9 折優惠

price = 0
age = int(input('年紀: '))
if (age > 18):
    print("賣出電影票")
    if (age >= 60):
        price += 1000
    elif (age < 60):
        price += 1800
    point = int(input('點數: '))
    print('總價: ', end='')
    if (point > 5):
        print(round(price * 0.9))
    else:
        print(price)
        
else:
    print("不能賣出電影票")