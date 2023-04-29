def odd_values_string(str1):
	str2 = ""
	for i in range(len(str1)):
		if i % 2 == 0:
			str2 = str2 + str1[i]
	return str2

print(odd_values_string("abcdef"))
print(odd_values_string("python"))
