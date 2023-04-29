

def isPrime(n):
	p = True
	if n == 1:
		p = False
	elif n == 2:
		p = True
	else:
		for i in range(2, n // 2):
			if n % i == 0:
				p = False
	return p

print(isPrime(6))
print(isPrime(17))
