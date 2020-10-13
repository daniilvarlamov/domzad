N = int(input())
F1 = 1
F2 = 1
while (F2 <= N) :
	c = F2
	F2 = F1 + F2
	F1 = c
print(F2)

	
