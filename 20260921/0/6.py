while (x := input()) != "":
	if not(int(x) & 1): print(x)
	if (int(x) == 13): break
else: print("Congrats! 13 wasnt found")
