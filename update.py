import psycopg2

connection = None
cursor = None

def add_new_product(name, category):
    """Добавление нового товара"""
    try:
        cursor.execute("""
            INSERT INTO products (name, category) 
            VALUES (%s, %s)
            RETURNING id;
        """, (name, category))
        
        product_id = cursor.fetchone()[0]
        connection.commit()
        print(f"   ✅ Товар добавлен с ID: {product_id}")
        return product_id
        
    except Exception as e:
        connection.rollback()
        print(f"   ❌ Ошибка при добавлении: {e}")
        return None

def add_price(product_id, price):
    """Добавление цены для товара"""
    try:
        cursor.execute("""
            INSERT INTO prices (product_id, price) 
            VALUES (%s, %s);
        """, (product_id, price))
        connection.commit()
        print(f"   ✅ Цена {price} руб. добавлена для товара ID: {product_id}")
        
    except Exception as e:
        connection.rollback()
        print(f"   ❌ Ошибка при добавлении цены: {e}")

def update_product_price(product_id, new_price):
    """Обновление цены товара"""
    try:
        cursor.execute("""
            UPDATE prices 
            SET price = %s 
            WHERE product_id = %s 
            ORDER BY created_at DESC 
            LIMIT 1;
        """, (new_price, product_id))
        
        connection.commit()
        print(f"   ✅ Цена товара ID {product_id} обновлена на {new_price} руб.")
        
    except Exception as e:
        connection.rollback()
        print(f"   ❌ Ошибка при обновлении: {e}")

def delete_product(product_id):
    """Удаление товара и всех его цен"""
    try:
        # Удаляем цены
        cursor.execute("DELETE FROM prices WHERE product_id = %s;", (product_id,))
        prices_deleted = cursor.rowcount
        
        # Удаляем товар
        cursor.execute("DELETE FROM products WHERE id = %s;", (product_id,))
        product_deleted = cursor.rowcount
        
        connection.commit()
        print(f"   ✅ Удалено цен: {prices_deleted}, удалено товаров: {product_deleted}")
        
    except Exception as e:
        connection.rollback()
        print(f"   ❌ Ошибка при удалении: {e}")

# =====================================================
# ГЛАВНАЯ ПРОГРАММА
# =====================================================
try:
    # Подключение
    connection = psycopg2.connect(
        host="localhost",
        port="5430",
        user="postgres_user",
        password="postgres_password",
        database="postgres_db"
    )
    cursor = connection.cursor()
    
    print("✅ Подключение установлено")
    print("="*50)
    
    # 1. Добавляем новый товар
    print("\n📝 Добавление нового товара:")
    product_id = add_new_product("Тестовый ноутбук", "Электроника")
    
    if product_id:
        # 2. Добавляем цены для нового товара
        print("\n💰 Добавление цен:")
        add_price(product_id, 50000.00)
        add_price(product_id, 45000.00)
        
        # 3. Обновляем цену
        print("\n🔄 Обновление цены:")
        update_product_price(product_id, 48000.00)
        
        # 4. Проверяем результат
        print("\n📊 Проверка результатов:")
        cursor.execute("""
            SELECT p.name, pr.price, pr.created_at 
            FROM products p
            JOIN prices pr ON p.id = pr.product_id
            WHERE p.id = %s
            ORDER BY pr.created_at DESC;
        """, (product_id,))
        
        results = cursor.fetchall()
        for row in results:
            print(f"   {row[0]}: {row[1]} руб. ({row[2]})")
        
        # 5. Удаляем тестовые данные
        print("\n🗑️ Удаление тестовых данных:")
        delete_product(product_id)
    
    print("\n" + "="*50)
    print("✅ Все операции выполнены успешно!")
    
except Exception as error:
    if connection:
        connection.rollback()
    print(f"❌ Ошибка: {error}")
    
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
    print("\n🔌 Соединение закрыто")