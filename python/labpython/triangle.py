x = int(input("Enter a value: "))
y = int(input("Enter a value: "))
z = int(input("Enter a value: "))

def isTriangle(a,b,c):
	if a < b + c and b < a + c and c < a + b:
		return True
	return False
		
print(isTriangle(x,y,z))
