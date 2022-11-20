while True: 
    check = int(input("請選擇您要輸入的樣式: \n[1] 攝氏溫度\n[2] 華氏溫度\n>> "))
    degree = float(input("請輸入您要轉換的溫度: \n>> "))
    if check == 1:
        ans = float(degree*(9/5)+32)
        print("=>", ans)
    elif check == 2:
        ans = float((degree-32)*(5/9))
        print("=>", ans)
    else:
        print("====請輸入正確樣式====\n")
    print("========================\n")