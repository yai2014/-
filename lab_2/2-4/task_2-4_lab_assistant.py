volume = float(input("Введите нужный объем физиологического раствора (мл): "))

salt_mass = volume * 0.009

water_volume = volume

volume_rounded = round(volume, 2)
salt_mass_rounded = round(salt_mass, 2)
water_volume_rounded = round(water_volume, 2)

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    
    file.write("-" * 23 + "\n")
    
    file.write(f"Общий объем:\t{volume_rounded} мл\n")
    file.write(f"Масса соли:\t{salt_mass_rounded} г\n")
    file.write(f"Объем воды:\t{water_volume_rounded} мл\n")

print(f"\nРецепт успешно сохранен в файл recipe.txt")