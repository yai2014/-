reactiv_1 = input("Введите название реактива:")
user_reactiv_1 = reactiv_1
quantity_1 = input("Введите количество реактива:")
user_quantity_1 = quantity_1
reactiv_2 = input("Введите название реактива:")
user_reactiv_2 = reactiv_2
quantity_2 = input("Введите количество реактива:")
user_quantity_2 = quantity_2
reactiv_3 = input("Введите название реактива:")
user_reactiv_3 = reactiv_3
quantity_3 = input("Введите количество реактива:")
user_quantity_3 = quantity_3


f = open("output.txt", "w", encoding="utf-8")

print(f"Реактив {user_reactiv_1} поступил на склад в количестве {user_quantity_1} шт\nРеактив {user_reactiv_2} поступил на склад в количестве {user_quantity_2} шт\nРеактив {user_reactiv_3} поступил на склад в количестве {user_quantity_3} шт", file=f)
f.close()