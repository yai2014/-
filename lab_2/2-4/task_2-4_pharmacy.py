total_capsules = int(input("Введите общее количество произведенных капсул: "))

pack_capacity = int(input("Введите количество капсул в одной упаковке: "))

full_packs = total_capsules // pack_capacity

remaining_capsules = total_capsules % pack_capacity

print("\n\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packs}")
print(f"Остаток капсул:\t\t{remaining_capsules}")
print(f"\nПроверка: {full_packs} упаковок по {pack_capacity} капсул + {remaining_capsules} капсул = {full_packs * pack_capacity + remaining_capsules} капсул")