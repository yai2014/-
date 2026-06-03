user_fio = input("Введите ФИО исследователя: ").upper()
date_today = input("Введите дату: ")
user_experiment = input("Введите название эксперимента: ")
user_conclusion = ("|В ходе эксперимента выявлены нарушения  |\n| долговременной памяти у экспериментальной|\n| группы животных.                         | ")
conclusion = input("Введите вывод: ")

paragraphs = user_conclusion.split('\n\n')

with open("journal.txt", "w", encoding="utf-8") as card: card.write(f"Электронный лабораторный журнал\nФИО исследователя:{user_fio}\n Дата\t: {date_today}\nЭксперимент\t:{user_experiment}\nВывод:\n{conclusion}")

print("+------------------------------------------+")
print(f"|\t Электронный лабораторный журнал    |")
print("+------------------------------------------+")
print(f"| ФИО исследователя: {user_fio}  |\n| Дата\t: {date_today}                       |\n| Эксперимент\t:{user_experiment} |")
print("+------------------------------------------+")
print("|\t Вывод:\t                           | ")
print(f" {user_conclusion}")
print("+------------------------------------------+")