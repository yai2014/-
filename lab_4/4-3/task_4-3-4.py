n = int(input("Введите размер массива n: "))

summa = 0
i = 0

while i < n:
    element = float(input(f"Введите элемент A[{i}]: "))
    A_i = element

    if i % 2 != 0:
        summa = summa + A_i
    
    i = i + 1

print(f"Сумма элементов с нечётными индексами: {summa}")