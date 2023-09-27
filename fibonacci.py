num=int(input("enter range: "))
a=0
b=1
print(a,b,end=" ")
for i in range (num+1):
    fibonacci=a+b
    print(fibonacci, end=" ")
    a=b
    b=fibonacci
    

