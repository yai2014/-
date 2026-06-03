n = int(input("Введите размер массива n: "))

A = []
for j in range(n):
    element = float(input(f"Введите элемент A[{j}]: "))
    A.append(element)

summa = 0
i = 0 

while i < n:
    summa = summa + A[i]
    i = i + 1

avg = summa / n

print(f"Среднее арифметическое элементов массива: {avg}")