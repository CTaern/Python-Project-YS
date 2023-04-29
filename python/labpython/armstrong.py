def isArmstrong(a, b, c):
	x = a**3
	y = b**3
	z = c**3
	return x + y + z

print(isArmstrong(1,5,3) == 153)
