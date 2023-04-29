x = 562
year = 0
while x <= 20000:
	x = x * 0.1 + x
	year = year + 1
	print(year, x)
print("Population is", x, "in", year, "years")

