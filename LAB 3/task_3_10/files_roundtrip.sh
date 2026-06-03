#!/bin/bash

echo "=========================================="
echo "         СОЗДАНИЕ И УДАЛЕНИЕ ФАЙЛОВ"
echo "=========================================="
echo "Этап 1: Создание файлов test1.txt - test10.txt"

for i in {1..10}; do
    touch "test${i}.txt"
    echo "  Создан файл: test${i}.txt"
done

echo ""
echo "Список созданных файлов:"
ls -la test*.txt
echo ""
echo "=========================================="
echo "Этап 2: Удаление файлов в обратном порядке"

counter=10

while [ $counter -ge 1 ]; do
    echo "  Удаляется файл: test${counter}.txt"
    rm "test${counter}.txt"
   
    if [ ! -f "test${counter}.txt" ]; then
        echo "    Файл test${counter}.txt успешно удалён"
    fi

    counter=$((counter - 1))
 sleep 0.5
done

echo ""
echo "=========================================="
echo "Проверка: файлы должны отсутствовать"
ls -la test*.txt 2>/dev/null || echo "  Нет файлов test*.txt (все удалены)"
echo "=========================================="
echo "Программа завершена."
echo "=========================================="
