rows = 7

for i in range(1, rows + 1):
    for j in range(1, 7 + 1):
        if(j <= rows - i):
            print(' ', end = '  ')
        else:
            print("*", end = '  ')
    print()
