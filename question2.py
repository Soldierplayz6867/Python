l = int(input('長度: '))
h = int(input('高度: '))
w = int(input('寬度: '))

print('+===========+')

q1 = l * h * w
print('體積: ', end='')
print(q1)

q2 = (l*w*2) + (h*w*2) + (l*w*2)
print('表面積: ', end='')
print(q2)