N = int(input("введите длину массива\n"))
a = []
print("введите элементы массива")
for i in range(N):
    a.append(int(input()))
print(a)
napr = int(input("1 - сортировка по возрастанию, 2 - по убыванию\n"))
if napr == 1:
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)
elif napr == 2:
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)
else:
    print("нужно ввести 1 или 2")
