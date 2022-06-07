n=int(input())
if(n%2==0):
    print("even")
else:
    print("odd")
if(n%5==0):
    print("divisible")
else:
    print("not divisible")
print(n*(n+1)/2)
a=int(n**0.5)
c=0
for i in range(2,a+1):
    if(n%i==0):
        c+=1
if(c==0):
    print("prime")
else:
    print("not prime")
