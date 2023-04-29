def add_string(str1):
	if len(str1) < 3:
		return str1
	elif str1[-3:] == "ing":
		return (str1 + "ly")
	else :
		return (str1 + "ing")
print(add_string("ab"))
print(add_string("abc"))
print(add_string("string"))
