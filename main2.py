#Activity2
def printfac(n):
    print("The factors are: ")
    for i in range(1,n+1):
        if n%i==0:
            print(i)
number=int(input("Enter number to get the factors: "))
printfac(number)