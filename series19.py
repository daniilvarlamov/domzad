N = int(input())
k = 0
a = []
for i in range(N):
	a.append(int(input()))
for i in range(N-1):
	if (a[i] > a[i+1]):
		k += 1
		print("элемент: ",a[i+1])
print("количество = ",k)

