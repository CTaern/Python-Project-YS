def isArmstrong(n):
	a = n // 100
	b = (n // 10) % 10
	c = n % 10
	return n == (a**3 + b**3 + c**3)

for i in range(100,1000):
	 if i == isArmstrong()
	 print(i,isArmstrong(i))
	 
