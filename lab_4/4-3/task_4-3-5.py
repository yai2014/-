N = int(input("Введите размер массива N: "))

if N > 0:
    A = [0] * N
    
    S = 0      
    count = 0  
    i = 1      
    
    while i <= N:
        element = float(input(f"Введите элемент A[{i}]: "))
        A[i-1] = element  
        
        if i % 2 == 0:
            S = S + element
            count = count + 1
        
        i = i + 1
    
    if count > 0:
        Avg = S / count
        print(f"Среднее арифметическое элементов с чётными индексами: {Avg}")
    else:
        print("Нет элементов с чётными индексами")
else:
    print("Размер массива должен быть больше 0")