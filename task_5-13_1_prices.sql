-- =====================================================
-- Задание: Обновление цен в таблице prices
-- Увеличьте цену на 10% для всех товаров, у которых текущая цена меньше 1000
-- =====================================================

-- Проверочный запрос: посмотреть, какие цены будут изменены (до обновления)
SELECT id, product_id, price, price * 1.10 AS new_price, created_at
FROM prices 
WHERE price < 1000
ORDER BY price;

-- Основной запрос: обновление цен (+10%)
UPDATE prices 
SET price = price * 1.10 
WHERE price < 1000;

-- Проверочный запрос: убедиться, что обновление прошло успешно (после обновления)
SELECT id, product_id, price, created_at
FROM prices 
WHERE price < 1000
ORDER BY price;