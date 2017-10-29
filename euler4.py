def abc(p):
	k=str(p)
	l=k[::-1]
	
	if(k==l):
		return 1
	else:
		return 0
p=0	
for i in range(999,800,-1):
	for j in range(999,800,-1):
		p=i*j
		if(abc(p)==1):
			print(p,"MULTIPLE OF ",i," ",j)
			quit()
			

