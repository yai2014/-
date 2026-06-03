donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
patient = input("Введите фенотип группы крови пацента (I, II, III, IV): ").strip().upper()

if donor == patient :
    print("Переливание возможно")
elif donor == "I":
    print("ГПереливание возможно")
else:
    print("Донорство запрещено")