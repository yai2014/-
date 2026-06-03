#!/bin/bash
echo "=========================================="
echo "     ЗАМЕНА ПУТИ К БАЗЕ ДАННЫХ"
echo "=========================================="

if [ ! -f "settings.php" ]; then
    echo "Ошибка: Файл settings.php не найден!"
    exit 1
fi
cp settings.php settings.php.bak
echo "Создана резервная копия: settings.php.bak"

sed -i "s|/var/lib/mysql/data|/mnt/ssd/mysql|" settings.php
if [ $? -eq 0 ]; then
    echo "Замена выполнена успешно!"
    echo ""
    echo "Изменённая строка:"
    grep "db_data_path" settings.php
else
    echo "Ошибка при выполнении замены!"
    exit 1
fi

echo "=========================================="

