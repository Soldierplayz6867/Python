h = int(input("height: "))
w = int(input("weight: "))

bmi = w/h^2
print("bmi: ", end='')
print(bmi)

if (bmi>=24):
    print("體重過重")
elif (bmi<=18.5):
    print("體重過輕")
else:
    print("體重標準")