-- =====================================================
-- Задание: Группировка данных в таблице suppliers
-- =====================================================

-- Выведите количество поставщиков для каждого товара из таблицы suppliers, сгруппировав данные по product_id
SELECT product_id, COUNT(*) AS suppliers_count FROM suppliers GROUP BY product_id ORDER BY product_id;