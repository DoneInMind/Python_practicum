count = 0
pos = 1

while (x := int(input())) != 0:
	if (x == pos): count += 1
	pos += 1

print(count)
