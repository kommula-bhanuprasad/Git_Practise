
#this is the second file

def pow(n):
	if n>0:
		pow(n-1)
		k=n**2
		print(k)
		pow(n-1)
pow(4)
