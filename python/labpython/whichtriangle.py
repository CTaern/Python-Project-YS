x = int(input("Enter a integer: "))
y = int(input("Enter a integer: "))
z = int(input("Enter a integer: "))

def isTriangle(a, b, c):
	if a < b + c and b < a + c and c < a + b:
		return True
	return False

def whichTriangle(a, b, c):
	if isTriangle(a, b, c):
		if a == b and a == c and b == c:
			return "Eq"
		elif a == b or a == c or b == c:
			return "Is"
		else:
			return "Sc"	
	return "Invalid"
	
print(whichTriangle(x, y, z))
