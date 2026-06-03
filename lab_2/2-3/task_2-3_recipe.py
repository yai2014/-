nutrient_medium = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temperature = input("Введите температуру стерилизации (°C): ")
with open("recipe.txt", "w", encoding="utf-8") as card:
    
    
    card.write(f"{nutrient_medium}\nКонцентрация агара: {agar_concentration}\nТемпература стерилизации:{sterilization_temperature}")
    print(f"{nutrient_medium}\nКонцентрация агара: {agar_concentration}\nТемпература стерилизации:{sterilization_temperature}")
    
    print("Файл 'recipe.txt' успешно сформирован!")