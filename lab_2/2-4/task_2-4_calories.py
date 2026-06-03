protein = float(input("Введите массу белков (г): "))

fat = float(input("Введите массу жиров (г): "))

carbohydrates = float(input("Введите массу углеводов (г): "))

calories = (protein * 4) + (fat * 9) + (carbohydrates * 4)

print(f"\nОбщая калорийность продукта: {calories:.1f} ккал")

print(f"\n--- Детальный расчет ---")
print(f"Белки: {protein} г × 4 = {protein * 4:.1f} ккал")
print(f"Жиры: {fat} г × 9 = {fat * 9:.1f} ккал")
print(f"Углеводы: {carbohydrates} г × 4 = {carbohydrates * 4:.1f} ккал")