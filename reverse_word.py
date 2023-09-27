name=input("Enter a value: ")
length=len(name)
print("Original word: ",name)
sum=""
for j in range(-1,(-length-1),-1):
 
    sum=sum+name[j]

print("Reverse word: ", sum)