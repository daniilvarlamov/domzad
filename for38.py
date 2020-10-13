N = int(input())
sum = 1
for i in range (2,N) :
	a = i
	for j in range (2,N+1) :
		a = a*i
		sum = sum + a
print("Результат", sum)
