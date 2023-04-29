def isPerfect(n):
	x = 0
	for i in range(1, n):
		if n % i == 0:
			x = x + i
	return x == n
		
for i in range(1,100000):
	if  isPerfect(i):
		print(i, isPerfect(i))
