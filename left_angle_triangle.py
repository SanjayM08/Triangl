def tri(n):
    for i in range(n):
        for j in range(n):
            print("* ",end=" ")
        n=n-1
        print("")

n=7
tri(n)
