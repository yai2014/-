n = int(input("Введите размер массива n: "))

count = 0
i = 0

while i < n:
    element = float(input(f"Введите элемент A[{i}]: "))
    A_i = element
    
    if A_i > 0:
        count = count + 1
    i = i + 1

print(f"Количество положительных чисел в массиве: {count}")