#!/bin/bash

echo "=========================================="
echo "     СТАТИСТИЧЕСКИЙ АНАЛИЗ ОЦЕНОК"
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

echo "1. Сумма всех оценок:"
echo "------------------------------------------"
sum=$(awk '{sum += $2} END {print sum}' students.txt)
echo "Сумма оценок: $sum баллов"
echo "------------------------------------------"

echo ""
echo "2. Средняя оценка:"
echo "------------------------------------------"
average=$(awk '{sum += $2; count++} END {print sum/count}' students.txt)
printf "Средняя оценка: %.2f баллов\n" $average
echo "------------------------------------------"

echo ""
echo "3. Максимальная оценка:"
echo "------------------------------------------"
max=$(awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt)
max_student=$(awk -v max="$max" '$2 == max {print $1}' students.txt)
echo "Максимальная оценка: $max баллов"
echo "Лучший студент: $max_student"
echo "------------------------------------------"

echo ""
echo "Дополнительная информация:"
echo "------------------------------------------"
min=$(awk 'NR==1{min=$2} $2<min{min=$2} END{print min}' students.txt)
min_student=$(awk -v min="$min" '$2 == min {print $1}' students.txt)
echo "Минимальная оценка: $min баллов"
echo "Студент с минимальной оценкой: $min_student"
count=$(awk 'END{print NR}' students.txt)
echo "Количество студентов: $count"
echo "------------------------------------------"
echo "=========================================="
echo "Анализ завершён."
echo "=========================================="
EOF

