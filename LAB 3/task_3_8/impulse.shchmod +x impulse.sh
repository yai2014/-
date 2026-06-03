#!/bin/bash

if [ $# -ne 2 ]; then
    echo "ОШИБКА: Недостаточно входящих данных!"
    echo ""
    echo "Правильное использование:"
    echo "  ./impulse.sh [ИМЯ_ГЕНА] [УРОВЕНЬ_ЭКСПРЕССИИ]"
    echo ""
    echo "Пример:"
    echo "  ./impulse.sh BRCA1 150"
    exit 1
fi

gene_name=$1
expression_level=$2

echo "Экспрессия гена $gene_name составляет $expression_level единиц"



