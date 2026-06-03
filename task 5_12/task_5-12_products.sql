-- =====================================================
-- Задание: Группировка данных в таблице products
-- Все запросы разделены точкой с запятой
-- =====================================================

-- 1. Выведите количество товаров в таблице products, сгруппировав результат по категориям
SELECT category, COUNT(*) AS product_count FROM products GROUP BY category;

-- 2. Выведите количество товаров в каждой категории из таблицы products, отсортировав результат по убыванию количества
SELECT category, COUNT(*) AS product_count FROM products GROUP BY category ORDER BY product_count DESC;