x=1
y=10
print(x)
print(y)
for i in range(0,5):
    print(x+y)
    temp=x
    x=y
    y=temp+y
