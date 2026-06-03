-- =====================================================
-- Задание: Обновление цен в таблице prices
-- Обновите цены товаров для записей, где product_id ≤ 5 и цена меньше 10000, 
-- увеличить цену на 5%
-- =====================================================

-- Проверочный запрос: посмотреть, какие цены будут изменены (до обновления)
SELECT id, product_id, price, price * 1.05 AS new_price, created_at
FROM prices 
WHERE product_id <= 5 AND price < 10000
ORDER BY product_id, price;

-- Основной запрос: обновление цен (+5%)
UPDATE prices 
SET price = price * 1.05 
WHERE product_id <= 5 AND price < 10000;

-- Проверочный запрос: убедиться, что обновление прошло успешно (после обновления)
SELECT id, product_id, price, created_at
FROM prices 
WHERE product_id <= 5
ORDER BY product_id, price;