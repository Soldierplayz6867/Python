n = int(input("棋盤大小: "))
loop = 0
board = []
o = 0
x = 0

total_O = 0
total_X = 0

while loop < n:
    data = input()
    sto = []
    for i in data:
        if i == 'O':
            sto.append(0)
            total_O += 1
        else:
            sto.append(1)
            total_X += 1
    board.append(sto)
    loop = loop + 1

print('版面: ', end='')
print(board)

# row
loop = 0
while loop < n:
    count_O = 0
    count_X = 0
    for i in board[loop]:
        if i == 0:
            count_O += 1
        elif i == 1:
            count_X += 1
    if count_O == n:
        o += 1
    if count_X == n:
        x += 1
    loop += 1

# col
loop = 0
while loop < n:
    count_O = 0
    count_X = 0
    a = 0
    while a < n:
        i = board[a][loop]
        if i == 0:
            count_O += 1
        elif i == 1:
            count_X += 1
        a += 1
    if count_O == n:
        o += 1
    if count_X == n:
        x += 1
    loop += 1

# sli-left-right
count_O = 0
count_X = 0
i = 0
while i < n:
    opt = board[i][i]
    if opt == 0:
        count_O += 1
    elif opt == 1:
        count_X += 1
    i += 1
if count_O == n:
    o += 1
if count_X == n:
    x += 1

# sli-left-right
count_O = 0
count_X = 0
i = 0
while i < n:
    opt = board[i][n-i-1]
    if opt == 0:
        count_O += 1
    elif opt == 1:
        count_X += 1
    i += 1
if count_O == n:
    o += 1
if count_X == n:
    x += 1

if abs(total_X - total_O) > 1:
    print("Impossible")
else:
    # end
    print("X:", end='')
    print(x, end='  ')
    print("O:", end='')
    print(o)