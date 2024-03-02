def print_inverted_triangle(n):
    m = n - 1
    for i in range(n, 0, -1):
        for j in range(0, n - i):
            print(end=" ")
        for j in range(0, i):
            print("*", end=" ")
        print("")

n=7
if n % 2 == 0:
    print("Give an Odd Number for a perfect Triangle shape")
else:
    print_inverted_triangle(n)
