M = int(input())
N = int(input())
a = []
k = 0
for g in range(M):
    a.append([])
    for i in range (N):
        a[g].append(int(input()))
for g in range(M):
    for i in range (0,N,2):
        k+=a[g][i]
print(a,k)
    
