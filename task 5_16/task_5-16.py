# =====================================================
# Задание 1: Подключение к СУБД и выполнение SQL-запроса
# =====================================================

import psycopg2

def main():
    """Главная функция: подключение и выполнение запроса"""
    
    connection = None
    cursor = None
    
    try:
        # Подключение к базе данных (параметры из docker-compose.yml)
        connection = psycopg2.connect(
            host="localhost",              # Хост
            port="5430",                   # Порт
            user="postgres_user",          # Пользователь
            password="postgres_password",  # Пароль
            database="postgres_db"         # База данных
        )
        
        cursor = connection.cursor()
        
        # Выполнение SQL-запроса
        # Запрос: получить топ-5 самых дорогих товаров с их ценами
        cursor.execute("""
            SELECT 
                p.name AS product_name,
                p.category,
                MAX(pr.price) AS max_price
            FROM products p
            JOIN prices pr ON p.id = pr.product_id
            GROUP BY p.id, p.name, p.category
            ORDER BY max_price DESC
            LIMIT 5;
        """)
        
        # Получение результатов
        results = cursor.fetchall()
        
        # Вывод результатов
        print("=" * 60)
        print("ТОП-5 САМЫХ ДОРОГИХ ТОВАРОВ")
        print("=" * 60)
        print(f"{'№':<3} {'Название товара':<35} {'Категория':<15} {'Цена, руб.':>10}")
        print("-" * 60)
        
        for i, row in enumerate(results, 1):
            name, category, price = row
            print(f"{i:<3} {name[:34]:<35} {category:<15} {price:>10.2f}")
        
        print("=" * 60)
        print(f"✅ Запрос выполнен успешно. Найдено записей: {len(results)}")
        
    except psycopg2.Error as e:
        print(f"❌ Ошибка PostgreSQL: {e}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        
    finally:
        # Закрытие курсора и соединения
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("\n🔌 Соединение с базой данных закрыто")

# Запуск программы
if __name__ == "__main__":
    main()