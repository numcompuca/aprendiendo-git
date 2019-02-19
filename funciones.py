def esPrimo(n):
	for k in range(2,n/2):
		if k%n==0: return False
		
	return True