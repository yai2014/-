
echo "=========================================="
echo "     ПОДСЧЁТ НУКЛЕОТИДОВ В FASTA-ФАЙЛАХ"
echo "=========================================="
echo ""


printf "%-20s %-8s %-8s %-8s %-8s\n" "Файл" "A" "T" "G" "C"
printf "%-20s %-8s %-8s %-8s %-8s\n" "--------------------" "--------" "--------" "--------" "--------"

for file in *.fasta; done
    
    if [ ! -f "$file" ]; then
        echo "Нет FASTA-файлов в текущей папке."
        exit 1
    fi
    
    
    if [ ! -s "$file" ]; then
        echo "Пропущен пустой файл: $file"
        continue
    fi
    
   
    sequence=$(grep -v "^>" "$file" | tr -d '\n' | tr -d '\r' | tr '[:lower:]' '[:upper:]')
    
    
    count_A=$(echo "$sequence" | grep -o "A" | wc -l)
    count_T=$(echo "$sequence" | grep -o "T" | wc -l)
    count_G=$(echo "$sequence" | grep -o "G" | wc -l)
    count_C=$(echo "$sequence" | grep -o "C" | wc -l)
    
    printf "%-20s %-8s %-8s %-8s %-8s\n" "$file" "$count_A" "$count_T" "$count_G" "$count_C"
done

echo ""
echo "=========================================="
echo "Подсчёт завершён."
echo "=========================================="
