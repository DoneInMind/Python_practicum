a, b, c = eval(input())

if (a > 0 and b > 0 and c > 0 and (max(a, b, c) * 2 < a + b + c)):
	print("TRUE")
else: print("FALSE")

