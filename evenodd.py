l=[]
n=int(input("Enter the no of elements: "))
for i in range(n):
    ele=int(input("Enter elements: "))
    l.append(ele)
print(l) 
even=[]
odd=[]
for i in range(n):
    if(l[i]%2==0):
        even.append(l[i])
    else:
        odd.append(l[i])    
print(even)
print(odd)      
