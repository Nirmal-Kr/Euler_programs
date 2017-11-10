n = 20
def prime(u):
    t = 0
    for i in range(1, u):
        if u % i == 0:
            t += 1
    if(t==1):
        return 1
    else:
        return 0
prod=1
for x in range(2,n+1):
    c=prime(x)
    if(c==1):
        y=x
        z=0
        while y<n:
            y=y*x
            z=1
        if z==1:
            y=y/x
        prod=prod*y
print(prod)


