--  “Транзакции, представления”

-- 1)

USE sample;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Покупатели';

USE shop;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Покупатели';

INSERT INTO users (name, birthday_at) VALUES
  ('Геннадий', '1990-10-05'),
  ('Наталья', '1984-11-12'),
  ('Александр', '1985-05-20'),
  ('Сергей', '1988-02-14'),
  ('Иван', '1998-01-12'),
  ('Мария', '1992-08-29');
 
START TRANSACTION;

INSERT INTO sample.users SELECT * FROM shop.users WHERE id = 1;

COMMIT;

SELECT * FROM sample.users;

-- 2)

CREATE OR REPLACE VIEW cat AS 
 SELECT p.name AS product_name, c.name AS catalog_name FROM products AS p 
JOIN 
 catalogs AS c 
ON 
 p.catalog_id = c.id;

SELECT * FROM cat;

-- DROP VIEW cat;

-- Хранимые процедуры и функции, триггеры

-- 1)

DELIMITER //

DROP FUNCTION IF EXISTS hello//
CREATE FUNCTION hello ()
RETURNS VARCHAR(255) DETERMINISTIC
BEGIN
	IF (SELECT DATE_FORMAT(NOW(), '%H:%i') BETWEEN '06:00' AND '11:59') THEN 
	 RETURN 'Доброе утро!';
	ELSEIF (SELECT DATE_FORMAT(NOW(), '%H:%i') BETWEEN '12:00' AND '17:59') THEN
	 RETURN 'Добрый день!';
	ELSEIF (SELECT DATE_FORMAT(NOW(), '%H:%i') BETWEEN '18:00' AND '23:59') THEN
	 RETURN 'Добрый вечер!';
	ELSEIF (SELECT DATE_FORMAT(NOW(), '%H:%i') BETWEEN '00:00' AND '05:59') THEN
	 RETURN 'Доброй ночи!';
	END IF;
END//


SELECT hello()//

-- 2)

DELIMITER ;

DROP TABLE IF EXISTS products;
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Название',
  description TEXT COMMENT 'Описание',
  price DECIMAL (11,2) COMMENT 'Цена',
  catalog_id INT UNSIGNED,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  KEY index_of_catalog_id (catalog_id)
) COMMENT = 'Товарные позиции';

INSERT INTO products
  (name, description, price, catalog_id)
VALUES
  ('Intel Core i3-8100', 'Процессор для настольных персональных компьютеров, основанных на платформе Intel.', 7890.00, 1),
  ('Intel Core i5-7400', 'Процессор для настольных персональных компьютеров, основанных на платформе Intel.', 12700.00, 1),
  ('AMD FX-8320E', 'Процессор для настольных персональных компьютеров, основанных на платформе AMD.', 4780.00, 1),
  ('AMD FX-8320', 'Процессор для настольных персональных компьютеров, основанных на платформе AMD.', 7120.00, 1),
  ('ASUS ROG MAXIMUS X HERO', 'Материнская плата ASUS ROG MAXIMUS X HERO, Z370, Socket 1151-V2, DDR4, ATX', 19310.00, 2),
  ('Gigabyte H310M S2H', 'Материнская плата Gigabyte H310M S2H, H310, Socket 1151-V2, DDR4, mATX', 4790.00, 2),
  ('MSI B250M GAMING PRO', 'Материнская плата MSI B250M GAMING PRO, B250, Socket 1151, DDR4, mATX', 5060.00, 2);
 
 

DROP TRIGGER IF EXISTS check_products_name_description_insert;
DROP TRIGGER IF EXISTS check_products_name_description_update;
 
DELIMITER //

CREATE TRIGGER check_products_name_description_insert BEFORE INSERT ON products
FOR EACH ROW 
BEGIN 
	IF (NEW.name IS NULL AND NEW.description IS NULL) THEN 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Вы не ввели имя и описание товара.';
	END IF;
END//

CREATE TRIGGER check_products_name_description_update BEFORE UPDATE ON products
FOR EACH ROW 
BEGIN 
	IF NEW.name IS NULL THEN 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Вы не ввели новое названия товара';
	END IF;
END//

DELIMITER ;

-- INSERT INTO products (price, catalog_id) VALUES (80, 1);

UPDATE products SET name = NULL WHERE name = 'MSI B250M GAMING PRO';






















