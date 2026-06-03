#!/bin/bash

echo "=========================================="
echo "     АНАЛИЗ УСПЕВАЕМОСТИ СТУДЕНТОВ"
echo "=========================================="

if [ ! -f "students.txt" ]; then
    echo "Файл students.txt не найден. Создаю новый файл..."
    cat > students.txt << 'DATA'
Ivan 78
Maria 92
Oleg 67
Anna 85
DATA
    echo "Файл students.txt успешно создан!"
    echo ""
fi

echo "Данные из файла students.txt:"
echo "------------------------------------------"
cat students.txt
echo "------------------------------------------"
echo ""

echo "1. Студенты с оценкой ВЫШЕ 80:"
echo "------------------------------------------"
awk '$2 > 80 {print "  " $1 " - " $2 " баллов"}' students.txt
count=$(awk '$2 > 80 {count++} END {print count}' students.txt)
[ $count -eq 0 ] && echo "  Нет студентов с оценкой выше 80"
echo "------------------------------------------"

echo ""
echo "2. Студенты с оценкой НИЖЕ 70:"
echo "------------------------------------------"
awk '$2 < 70 {print "  " $1 " - " $2 " баллов"}' students.txt
count=$(awk '$2 < 70 {count++} END {print count}' students.txt)
[ $count -eq 0 ] && echo "  Нет студентов с оценкой ниже 70"
echo "------------------------------------------"

echo ""
echo "3. Первая строка файла:"
echo "------------------------------------------"
head -n 1 students.txt
echo "------------------------------------------"

echo ""
echo "Дополнительная статистика:"
echo "------------------------------------------"
average=$(awk '{sum+=$2; count++} END {print sum/count}' students.txt)
printf "Средняя оценка: %.2f баллов\n" $average

max_score=$(awk 'BEGIN{max=0}{if($2>max)max=$2}END{print max}' students.txt)
max_student=$(awk -v max="$max_score" '$2==max{print $1}' students.txt)
echo "Лучший студент: $max_student ($max_score баллов)"

min_score=$(awk 'BEGIN{min=100}{if($2<min)min=$2}END{print min}' students.txt)
min_student=$(awk -v min="$min_score" '$2==min{print $1}' students.txt)
echo "Студент с минимальной оценкой: $min_student ($min_score баллов)"
echo "------------------------------------------"
echo "=========================================="
echo "Анализ завершён."
echo "=========================================="
EOF
