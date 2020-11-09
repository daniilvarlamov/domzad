N = int(input("Введите число"))
n = [0]*N
for i in range (len(n)):
    n[i] = int(input())
    if (i==1):
        max1 = n[i]
        max2 = n[i]
for i in range (len(n)):
    if (n[i]>max1):
        max1 = n[i]
        max1num = i
    if (n[i]>= max2):
        max2 = n[i]
        max2num = i
print("Первое максимальное под номером",max1num," ", "Второе максимальное под номером ",max2num)
"""for i in range (N-1):
    minimum = min(n)
    maximum = max(n)
for i in range (N):
    if(minimum == n[i]):
        print("минимальный элемент под номером",i+1)
    if(maximum == n[i]):
        print("максимальный элемент под номером",i+1)"""

