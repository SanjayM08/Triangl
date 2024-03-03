def inverted(height):
    for i in range(height, 0, -1):
        spaces = (height - i) * 3
        print("" * spaces + "*" * i)


inverted(7)
