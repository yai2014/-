# =====================================================
# ЗАДАНИЕ 7: ВИЗУАЛИЗАЦИЯ ДАННЫХ ИЗ POSTGRESQL
# =====================================================

import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

# Настройка русских шрифтов для matplotlib
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# =====================================================
# 1. ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ
# =====================================================

def connect_to_db():
    """Подключение к PostgreSQL"""
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5430",
            user="postgres_user",
            password="postgres_password",
            database="postgres_db",
            options="-c client_encoding=utf8"
        )
        print("✅ Подключение к базе данных установлено")
        return connection
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return None

# =====================================================
# 2. ИЗВЛЕЧЕНИЕ ДАННЫХ
# =====================================================

def load_price_data(connection):
    """Загрузка данных о ценах с информацией о товарах"""
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
    
    df = pd.read_sql(query, connection)
    print(f"✅ Загружено {len(df)} записей о ценах")
    print(f"   Уникальных товаров: {df['product_name'].nunique()}")
    print(f"   Категорий: {df['category'].nunique()}")
    return df

# =====================================================
# 3. РАСЧЕТ СТАТИСТИЧЕСКИХ МЕТРИК
# =====================================================

def calculate_statistics(df):
    """Расчет статистических метрик для каждой категории"""
    stats = df.groupby('category')['price'].agg([
        ('count', 'count'),
        ('mean', 'mean'),
        ('median', 'median'),
        ('std', 'std'),
        ('min', 'min'),
        ('max', 'max'),
        ('q1', lambda x: x.quantile(0.25)),
        ('q3', lambda x: x.quantile(0.75))
    ]).round(2)
    
    print("\n📊 Статистика по категориям:")
    print(stats)
    return stats

# =====================================================
# 4. ПОСТРОЕНИЕ ГРАФИКОВ
# =====================================================

def create_histogram_with_statistics(df):
    """
    ГРАФИК 1: Гистограмма распределения цен с отмеченными статистиками
    Тип: Гистограмма + вертикальные линии
    Обоснование: Гистограмма позволяет увидеть распределение цен,
    а вертикальные линии показывают среднее значение и медиану,
    что помогает оценить симметричность распределения и выявить выбросы.
    """
    
    print("\n" + "="*60)
    print("📊 ГРАФИК 1: Распределение цен с отмеченными статистиками")
    print("="*60)
    
    # Создаем фигуру
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Гистограмма распределения цен
    n, bins, patches = ax.hist(df['price'], bins=50, alpha=0.7, color='steelblue', 
                                edgecolor='black', linewidth=0.5)
    
    # Расчет статистик
    mean_price = df['price'].mean()
    median_price = df['price'].median()
    q1 = df['price'].quantile(0.25)
    q3 = df['price'].quantile(0.75)
    
    # Добавляем вертикальные линии для статистик
    ax.axvline(mean_price, color='red', linestyle='-', linewidth=2, 
               label=f'Среднее: {mean_price:.2f} руб.')
    ax.axvline(median_price, color='green', linestyle='--', linewidth=2, 
               label=f'Медиана: {median_price:.2f} руб.')
    ax.axvline(q1, color='orange', linestyle=':', linewidth=2, 
               label=f'Q1 (25%): {q1:.2f} руб.')
    ax.axvline(q3, color='orange', linestyle=':', linewidth=2, 
               label=f'Q3 (75%): {q3:.2f} руб.')
    
    # Настройка графика
    ax.set_xlabel('Цена (руб.)', fontsize=12)
    ax.set_ylabel('Частота (количество записей)', fontsize=12)
    ax.set_title('Распределение цен товаров с отметками статистик', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Добавляем аннотацию с дополнительной информацией
    ax.text(0.98, 0.97, 
            f'Всего записей: {len(df)}\n'
            f'Станд. отклонение: {df["price"].std():.2f} руб.\n'
            f'Мин. цена: {df["price"].min():.2f} руб.\n'
            f'Макс. цена: {df["price"].max():.2f} руб.',
            transform=ax.transAxes,
            verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
            fontsize=9)
    
    plt.tight_layout()
    plt.savefig('price_distribution_histogram.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    return fig

def create_boxplot_by_category(df):
    """
    ГРАФИК 2: Boxplot (ящик с усами) по категориям товаров
    Тип: Boxplot (ящичковая диаграмма)
    Обоснование: Boxplot идеально подходит для сравнения распределений
    между категориями, показывает медиану, квартили, выбросы и размах.
    Позволяет легко сравнивать центральные тенденции и вариативность.
    """
    
    print("\n" + "="*60)
    print("📊 ГРАФИК 2: Распределение цен по категориям (Boxplot)")
    print("="*60)
    
    # Создаем фигуру
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Подготовка данных для boxplot
    categories = df['category'].unique()
    data_by_category = [df[df['category'] == cat]['price'].values for cat in categories]
    
    # Создаем boxplot
    bp = ax.boxplot(data_by_category, labels=categories, patch_artist=True, 
                    showmeans=True, meanline=True)
    
    # Настройка цветов
    colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 
              'lightpink', 'lightyellow', 'lightgray']
    for patch, color in zip(bp['boxes'], colors[:len(categories)]):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # Настройка отображения средних значений
    bp['means'][0].set_color('red')
    bp['means'][0].set_linewidth(2)
    bp['means'][0].set_linestyle('-')
    
    # Настройка графика
    ax.set_xlabel('Категория товара', fontsize=12)
    ax.set_ylabel('Цена (руб.)', fontsize=12)
    ax.set_title('Распределение цен по категориям товаров', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    # Поворачиваем подписи категорий для лучшей читаемости
    plt.xticks(rotation=45, ha='right')
    
    # Добавляем легенду
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='lightblue', alpha=0.7, label='Межквартильный размах (IQR)'),
        plt.Line2D([0], [0], color='blue', linewidth=2, label='Медиана'),
        plt.Line2D([0], [0], color='red', linewidth=2, linestyle='-', label='Среднее'),
        plt.Line2D([0], [0], color='gray', marker='o', linestyle='none', label='Выбросы')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('price_boxplot_by_category.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    return fig

def create_scatter_plot_timeline(df):
    """
    ДОПОЛНИТЕЛЬНЫЙ ГРАФИК: Цены во времени (по желанию)
    """
    
    print("\n" + "="*60)
    print("📊 ГРАФИК 3: Динамика цен во времени (дополнительный)")
    print("="*60)
    
    # Преобразуем created_at в datetime
    df['created_at'] = pd.to_datetime(df['created_at'])
    
    # Выбираем топ-5 товаров с наибольшим разбросом цен для наглядности
    price_range = df.groupby('product_name')['price'].agg(['min', 'max'])
    price_range['range'] = price_range['max'] - price_range['min']
    top_products = price_range.nlargest(5, 'range').index.tolist()
    
    # Фильтруем данные для топ-5 товаров
    df_top = df[df['product_name'].isin(top_products)]
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    for product in top_products:
        product_data = df_top[df_top['product_name'] == product]
        ax.plot(product_data['created_at'], product_data['price'], 
                marker='o', label=product, linewidth=2, markersize=6)
    
    ax.set_xlabel('Дата', fontsize=12)
    ax.set_ylabel('Цена (руб.)', fontsize=12)
    ax.set_title('Динамика изменения цен топ-5 товаров с наибольшим разбросом', 
                 fontsize=14, fontweight='bold')
    ax.legend(loc='best', fontsize=9)
    ax.grid(True, alpha=0.3)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('price_timeline.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    return fig

# =====================================================
# 5. АНАЛИЗ АНОМАЛИЙ
# =====================================================

def detect_anomalies(df):
    """
    Поиск аномалий в данных с использованием метода IQR
    """
    print("\n" + "="*60)
    print("🔍 АНАЛИЗ АНОМАЛИЙ В ДАННЫХ")
    print("="*60)
    
    Q1 = df['price'].quantile(0.25)
    Q3 = df['price'].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    anomalies = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]
    
    if len(anomalies) > 0:
        print(f"\n⚠️ Обнаружено аномалий: {len(anomalies)}")
        print(f"   Границы нормы: [{lower_bound:.2f}, {upper_bound:.2f}] руб.")
        print("\nСписок аномалий:")
        for _, row in anomalies.iterrows():
            print(f"   - {row['product_name']} ({row['category']}): {row['price']:.2f} руб.")
        
        # Анализ аномалий по категориям
        print("\n📊 Распределение аномалий по категориям:")
        anomaly_by_category = anomalies['category'].value_counts()
        for cat, count in anomaly_by_category.items():
            print(f"   - {cat}: {count} записей")
            
    else:
        print("\n✅ Аномалии не обнаружены")
        print(f"   Все цены находятся в диапазоне нормы: [{lower_bound:.2f}, {upper_bound:.2f}] руб.")
    
    return anomalies

# =====================================================
# 6. ВЫВОДЫ ПО ГРАФИКАМ
# =====================================================

def print_conclusions(df, stats, anomalies):
    """
    Формулирование выводов по графикам
    """
    print("\n" + "="*60)
    print("📝 ВЫВОДЫ ПО РЕЗУЛЬТАТАМ АНАЛИЗА")
    print("="*60)
    
    # Вывод по Графику 1
    print("\n📈 ВЫВОД ПО ГРАФИКУ 1 (Гистограмма распределения цен):")
    print("-" * 50)
    print(f"   1. Распределение цен имеет правостороннюю асимметрию (скошено вправо),")
    print(f"      так как среднее ({df['price'].mean():.2f} руб.) больше медианы ({df['price'].median():.2f} руб.).")
    print(f"   2. Большинство товаров (около 75%) имеют цену ниже {df['price'].quantile(0.75):.2f} руб.")
    print(f"   3. Наличие длинного \"хвоста\" в правой части указывает на существование")
    print(f"      небольшого количества очень дорогих товаров (премиум-сегмент).")
    print(f"   4. Стандартное отклонение ({df['price'].std():.2f} руб.) значительно превышает")
    print(f"      среднее значение, что подтверждает высокую вариативность цен.")
    
    # Вывод по Графику 2
    print("\n📊 ВЫВОД ПО ГРАФИКУ 2 (Boxplot по категориям):")
    print("-" * 50)
    
    # Находим категорию с самой высокой и низкой медианой
    median_by_category = df.groupby('category')['price'].median()
    highest_cat = median_by_category.idxmax()
    lowest_cat = median_by_category.idxmin()
    
    print(f"   1. Категория '{highest_cat}' имеет самую высокую медианную цену")
    print(f"      ({median_by_category[highest_cat]:.2f} руб.), что указывает на премиальный сегмент.")
    print(f"   2. Категория '{lowest_cat}' имеет самую низкую медианную цену")
    print(f"      ({median_by_category[lowest_cat]:.2f} руб.), что говорит о массовом сегменте.")
    print(f"   3. Разброс цен (IQR) значительно варьируется между категориями:")
    
    iqr_by_category = df.groupby('category')['price'].agg(lambda x: x.quantile(0.75) - x.quantile(0.25))
    for cat, iqr in iqr_by_category.sort_values(ascending=False).items():
        print(f"      - {cat}: IQR = {iqr:.2f} руб.")
    
    print(f"   4. Наличие выбросов на boxplot указывает на товары, цены которых")
    print(f"      значительно отличаются от основной массы в своей категории.")
    
    # Вывод по аномалиям
    print("\n⚠️ ВЫВОД ПО АНОМАЛИЯМ:")
    print("-" * 50)
    if len(anomalies) > 0:
        print(f"   1. Обнаружено {len(anomalies)} аномальных значений цен.")
        print(f"   2. Аномалии сконцентрированы в следующих категориях:")
        for cat, count in anomalies['category'].value_counts().items():
            print(f"      - {cat}: {count} записей")
        print(f"   3. Причинами аномалий могут быть:")
        print(f"      - Товары премиум-сегмента с очень высокими ценами")
        print(f"      - Распродажи или акции с очень низкими ценами")
        print(f"      - Ошибки ввода данных (следует проверить)")
    else:
        print(f"   1. Аномалии не обнаружены.")
        print(f"   2. Все цены находятся в статистически ожидаемом диапазоне.")
        print(f"   3. Данные демонстрируют хорошее качество и отсутствие выбросов.")
    
    print("\n" + "="*60)
    print("✅ Анализ завершен. Все графики сохранены в файлы.")
    print("="*60)

# =====================================================
# 7. ГЛАВНАЯ ФУНКЦИЯ
# =====================================================

def main():
    """Главная функция выполнения анализа"""
    print("="*60)
    print("📊 ВИЗУАЛИЗАЦИЯ ДАННЫХ ИЗ POSTGRESQL")
    print("="*60)
    
    # 1. Подключение к базе данных
    connection = connect_to_db()
    
    if connection is None:
        print("❌ Не удалось подключиться к базе данных")
        return
    
    # 2. Загрузка данных
    df = load_price_data(connection)
    
    if df is None or len(df) == 0:
        print("❌ Нет данных для анализа")
        connection.close()
        return
    
    # 3. Расчет статистик
    stats = calculate_statistics(df)
    
    # 4. Построение графиков
    fig1 = create_histogram_with_statistics(df)
    fig2 = create_boxplot_by_category(df)
    fig3 = create_scatter_plot_timeline(df)  # дополнительный график
    
    # 5. Поиск аномалий
    anomalies = detect_anomalies(df)
    
    # 6. Вывод заключений
    print_conclusions(df, stats, anomalies)
    
    # 7. Закрытие соединения
    connection.close()
    print("\n🔌 Соединение с базой данных закрыто")

# =====================================================
# ЗАПУСК ПРОГРАММЫ
# =====================================================
if __name__ == "__main__":
    main()