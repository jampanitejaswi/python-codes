l=[]
n=int(input("Enter the no of elements "))
for i in range(n):
    ele=int(input("Enter the element"))
    ele=l.append(ele)
print(l)
d=int(input("Enter element to be removed: "))
l.remove(d)
print(l)
