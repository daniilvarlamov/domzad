N = int(input())
a = []
for i in range (N):
    a.append(int(input()))
b = []
for i in range (N):
    b.append(int(0))
    for k in range (i,N):
        b[i]+=a[k]
print(b)
