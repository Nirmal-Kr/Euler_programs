n=60085
s=2
def abc(z):
	for i in range(2,z):
		if(z%i==0):
			return 1
	return 0
x=[i for i in range(2,n) if n%i==0]
for i in x:
	t=abc(i)
	if(t==0):
		s=i;
print(s)

