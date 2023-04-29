def change_integer(n):
	x = n // 100	# 1 
	y = (n % 100) // 10	# 2
	z = n % 10		# 3
	return z * 100 + y * 10 + x
	
print(change_integer(123))
print(change_integer(654))
