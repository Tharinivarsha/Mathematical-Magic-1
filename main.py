#Activity1
number=int(input("Enter a number to check whether Armstrong number or not: "))
result=0
temp=number
while temp!=0:
    digit=temp%10
    result=result+digit**3
    temp=temp//10
print(result)
if number==result:
    print("It is an armstrong number",number)
else:
    print("It is not an armstrong number",number)