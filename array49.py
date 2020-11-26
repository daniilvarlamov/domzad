N = int(input())
a = []
for i in range (N):
    a.append(int(input()))
for i in range(N-1):
    if (a[i+1]-a[i]==1):
        k = 1
    else:
        k = i
        print(k)
        break
if (k == 1):
    print(0)
    

    
    
