l=[]
n=int(input("Enter the no of elements: "))
for i in range(n):
    ele=int(input("Enter elements: "))
    l.append(ele)
print(l) 
print(l.index(max(l)))
print(l.index(min(l)))
#
