K = int(input("Введите K:"))
g = int()
a = []
up = 0 
down = 0
for i in range(0,K):
	g = int(input())
	while(g != 0):
		a.append(g)
		g = int(input())
	for i in range (len(a)-1):
		if (a[i] > a[i+1]):
			down += 1
		elif a[i] == a[i+1]:
			down += 1
			up += 1
		elif a[i] < a[i+1]:
			up += 1
	if up == len(a)-1:
		print("Последовательность возрастает:1")
	elif down == len(a)-1:
		print("Последовательность убывает:-1")
	else:
		print("С последовательностью что то не так:0")
	up = 0
	down = 0
	a = []			
