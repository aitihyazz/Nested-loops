a=input("Please enter your own word:")
b=input("Enter the character:")
i=0
count=0
while (i<len(a)):
    if (a[i] ==b):
        count=count+1
    i=1+i    
        
print("Total number of times",b,"has occurred=",count)