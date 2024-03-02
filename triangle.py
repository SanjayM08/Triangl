def tri(n):
    m=n-1
    for i in range(0,n):
        for j in range(0,m):
            print(end=" ")
        m=m-1
        for j in range(0,i+1):
            print("*",end=" ")
        print("")

n=7
if(n%2==0):
    print("Give Odd Number is perfect for Triangle shape")
    tri(n)

else:
    tri(n)



