
name_man = input("Введите имя оператора: ")
davlenie = input("Введите текущее значение давления (Па): ")

with open("sensor_log.txt", "w", encoding="utf-8") as card:
   
    card.write(f"{name_man}\t Значение: {davlenie}\n")
    print(f"{name_man}\nЗначение: {davlenie}")
    
    print("Данные успешно сохранены в sensor_log.txt")