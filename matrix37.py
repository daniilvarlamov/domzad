M = int(input())
N = int(input())
a = []
k = 0
for g in range(M):
    a.append([])
    for i in range (N):
        a[g].append(int(input()))
for i in range (N-1):
    if a[i]==a[N-1]:
        k+=1
print(a,k)
    
