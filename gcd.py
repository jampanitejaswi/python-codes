def mul(a,b):
   return a*b
 
def lcm(a,b):   
   if(a>b):
      big=a
   else:
     big=b
   while(True):
      if(big%a==0 and big%b==0):
           return big
           break
      big+=1
   
def gcd(a,b):
     return (mul(a,b))//(lcm(a,b))      
ans=gcd(7,9)     
print("GCD is "+ str(ans))       
