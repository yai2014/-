#!/bin/bash

readonly CURRENT_YEAR=2026
echo "==================================="
echo "   Калькулятор возраста"
echo "==================================="
echo -n "Введите ваш год рождения: "
read birth_year

age=$((CURRENT_YEAR - birth_year))

echo "-----------------------------------"
echo "Вам $age лет"
echo "-----------------------------------"
echo "Текущий год: $CURRENT_YEAR (константа)"

