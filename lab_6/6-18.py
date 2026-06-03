# =====================================================
# ЗАДАНИЕ 1: Анализ данных из PostgreSQL
# =====================================================

import psycopg2
import pandas as pd
import numpy as np

# =====================================================
# 1. Подключение к PostgreSQL-контейнеру
# =====================================================

def connect_to_db():
    """Подключение к базе данных"""
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5430",
            user="postgres_user",
            password="postgres_password",
            database="postgres_db",
            options="-c client_encoding=utf8"
        )
        print("✅ Соединение с PostgreSQL-контейнером установлено корректно")
        return connection
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return None

# =====================================================
# 2. JOIN запрос и загрузка в DataFrame
# =====================================================

def load_data_to_dataframe(connection):
    """Выполнение JOIN и загрузка в pandas DataFrame"""
    query = """
        SELECT 
            p.name AS product_name,
            p.category,
            pr.price,
            pr.created_at
        FROM prices pr
        JOIN products p ON pr.product_id = p.id
        ORDER BY pr.created_at;
    """
    
    try:
        df = pd.read_sql(query, connection)
        print(f"\n✅ Загружено записей: {len(df)}")
        print(f"   Столбцы: {list(df.columns)}")
        print("\nПервые 5 строк:")
        print(df.head())
        return df
    except Exception as e:
        print(f"❌ Ошибка загрузки данных: {e}")
        return None

# =====================================================
# 3. Основные статистики по цене
# =====================================================

def calculate_basic_statistics(df):
    """Расчет основных статистических показателей"""
    print("\n" + "="*60)
    print("📊 ОСНОВНЫЕ СТАТИСТИЧЕСКИЕ ПОКАЗАТЕЛИ")
    print("="*60)
    
    mean_price = df['price'].mean()
    median_price = df['price'].median()
    std_price = df['price'].std()
    min_price = df['price'].min()
    max_price = df['price'].max()
    
    print(f"Среднее значение:          {mean_price:>12.2f} руб.")
    print(f"Медиана:                   {median_price:>12.2f} руб.")
    print(f"Стандартное отклонение:    {std_price:>12.2f} руб.")
    print(f"Минимальная цена:          {min_price:>12.2f} руб.")
    print(f"Максимальная цена:         {max_price:>12.2f} руб.")
    
    return {
        'mean': mean_price,
        'median': median_price,
        'std': std_price,
        'min': min_price,
        'max': max_price
    }

# =====================================================
# 4. Квартили, IQR и товары выше Q3
# =====================================================

def calculate_quartiles_and_outliers(df):
    """Расчет квартилей и вывод товаров с ценой выше Q3"""
    print("\n" + "="*60)
    print("📐 КВАРТИЛИ И МЕЖКВАРТИЛЬНЫЙ РАЗМАХ")
    print("="*60)
    
    Q1 = df['price'].quantile(0.25)
    Q2 = df['price'].quantile(0.50)  # медиана
    Q3 = df['price'].quantile(0.75)
    IQR = Q3 - Q1
    
    print(f"Первый квартиль (Q1, 25%):   {Q1:>12.2f} руб.")
    print(f"Второй квартиль (Q2, 50%):   {Q2:>12.2f} руб. (медиана)")
    print(f"Третий квартиль (Q3, 75%):   {Q3:>12.2f} руб.")
    print(f"Межквартильный размах (IQR): {IQR:>12.2f} руб.")
    
    # Товары с ценой выше Q3
    high_price_products = df[df['price'] > Q3][['product_name', 'category', 'price']].drop_duplicates()
    
    print(f"\n🔥 ТОВАРЫ С ЦЕНОЙ ВЫШЕ Q3 (> {Q3:.2f} руб.):")
    print("-" * 60)
    
    if len(high_price_products) > 0:
        for _, row in high_price_products.iterrows():
            print(f"   {row['product_name']:<35} | {row['category']:<15} | {row['price']:>10.2f} руб.")
        print(f"\n   Всего товаров: {len(high_price_products)}")
    else:
        print("   Нет товаров с ценой выше Q3")
    
    return {'Q1': Q1, 'Q2': Q2, 'Q3': Q3, 'IQR': IQR}

# =====================================================
# 5. Группировка по категориям
# =====================================================

def group_by_category(df):
    """Группировка данных по категориям"""
    print("\n" + "="*60)
    print("📂 СТАТИСТИКА ПО КАТЕГОРИЯМ")
    print("="*60)
    
    category_stats = df.groupby('category')['price'].agg([
        ('Количество записей', 'count'),
        ('Средняя цена', 'mean'),
        ('Медиана', 'median'),
        ('Станд. отклонение', 'std')
    ]).round(2)
    
    # Сортировка по убыванию средней цены
    category_stats_sorted = category_stats.sort_values('Средняя цена', ascending=False)
    
    print(category_stats_sorted.to_string())
    
    return category_stats_sorted

# =====================================================
# 6. Топ-5 товаров с наибольшим разбросом цен
# =====================================================

def calculate_price_range(df):
    """Расчет разброса цен для каждого товара и вывод топ-5"""
    print("\n" + "="*60)
    print("📈 ТОП-5 ТОВАРОВ С НАИБОЛЬШИМ РАЗБРОСОМ ЦЕН")
    print("="*60)
    
    # Группировка по товарам
    price_range = df.groupby('product_name')['price'].agg([
        ('min_price', 'min'),
        ('max_price', 'max')
    ]).reset_index()
    
    price_range['price_range'] = price_range['max_price'] - price_range['min_price']
    price_range['price_range'] = price_range['price_range'].round(2)
    
    # Сортировка и топ-5
    top5_range = price_range.nlargest(5, 'price_range')
    
    print(f"\n{'Название товара':<40} {'Мин. цена':>12} {'Макс. цена':>12} {'Разброс':>12}")
    print("-" * 80)
    
    for _, row in top5_range.iterrows():
        print(f"{row['product_name']:<40} {row['min_price']:>12.2f} руб. {row['max_price']:>12.2f} руб. {row['price_range']:>12.2f} руб.")
    
    return top5_range

# =====================================================
# Дополнительная визуализация (опционально)
# =====================================================

def print_summary_statistics(df):
    """Вывод сводной статистики по всему DataFrame"""
    print("\n" + "="*60)
    print("📋 СВОДНАЯ СТАТИСТИКА")
    print("="*60)
    print(df['price'].describe().round(2))

# =====================================================
# ГЛАВНАЯ ФУНКЦИЯ
# =====================================================

def main():
    """Главная функция выполнения всего задания"""
    print("="*60)
    print("🐘 АНАЛИЗ ДАННЫХ ИЗ POSTGRESQL")
    print("="*60)
    
    # 1. Подключение к базе данных
    connection = connect_to_db()
    
    if connection is None:
        print("❌ Не удалось подключиться к базе данных")
        return
    
    # 2. Загрузка данных в DataFrame
    df = load_data_to_dataframe(connection)
    
    if df is None or len(df) == 0:
        print("❌ Нет данных для анализа")
        connection.close()
        return
    
    # 3. Основные статистики
    basic_stats = calculate_basic_statistics(df)
    
    # 4. Квартили и товары выше Q3
    quartiles = calculate_quartiles_and_outliers(df)
    
    # 5. Группировка по категориям
    category_stats = group_by_category(df)
    
    # 6. Топ-5 товаров с наибольшим разбросом цен
    top5_range = calculate_price_range(df)
    
    # Дополнительная статистика
    print_summary_statistics(df)
    
    # Закрытие соединения
    connection.close()
    print("\n" + "="*60)
    print("🔌 Соединение с PostgreSQL закрыто")
    print("="*60)

# =====================================================
# Запуск программы
# =====================================================
if __name__ == "__main__":
    main()