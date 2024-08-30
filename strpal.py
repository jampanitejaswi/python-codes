s=input("Enter string")
rev=""
for i in s:
    rev=i+rev       
if s==rev:
     print("It's a String Palindrome")
else:
     print("It's not a String Palindrome")   
