-- 1)

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
  
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INT UNSIGNED,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  KEY index_of_user_id(user_id)
) COMMENT = 'Заказы';

INSERT INTO orders (user_id, created_at, updated_at) VALUES
 (1, '2020-05-20 ', '2020-05-21'),
 (5, '2020-09-01', '2020-09-03'),
 (3, '2020-10-01', '2020-10-02');

SELECT u.id AS user_id, u.name, o.id AS order_id, o.created_at AS date_of_order FROM orders AS o JOIN users AS u ON u.id = o.user_id;

-- 2)

DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Название раздела',
  UNIQUE unique_name(name(10))
) COMMENT = 'Разделы интернет-магазина';

INSERT INTO catalogs VALUES
  (NULL, 'Процессоры'),
  (NULL, 'Материнские платы'),
  (NULL, 'Видеокарты'),
  (NULL, 'Жесткие диски'),
  (NULL, 'Оперативная память');
 
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

SELECT p.name AS product, c.name AS catalog FROM catalogs AS c JOIN products AS p ON c.id = p.catalog_id;

-- 3)


DROP TABLE IF EXISTS flights;
CREATE TABLE flights (
 id SERIAL PRIMARY KEY,
 from_city VARCHAR(255),
 to_city VARCHAR(255)
);

INSERT INTO flights (from_city, to_city) VALUES 
 ('moscow', 'omsk'),
 ('novgorod', 'kazan'),
 ('irkutsk', 'moscow'),
 ('omsk', 'irkutsk'),
 ('moscow', 'kazan');

DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
 label VARCHAR(255),
 name VARCHAR(255)
);

INSERT INTO cities (label, name) VALUES
 ('moscow', 'Москва'),
 ('irkutsk', 'Иркутск'),
 ('novgorod', 'Новгород'),
 ('kazan', 'Казань'),
 ('omsk', 'Омск');


SELECT c.name FROM cities AS c JOIN flights AS f ON c.label = f.from_city;

SELECT c.name FROM cities AS c JOIN flights AS f ON c.label = f.to_city;


SELECT 
* 
FROM
(SELECT f.id, c.name AS from_city FROM cities AS c JOIN flights AS f ON c.label = f.from_city) AS tbl1 
JOIN 
(SELECT * FROM(SELECT f.id, c.name AS to_city FROM cities AS c JOIN flights AS f ON c.label = f.to_city) AS tbl2)
AS 
total_tbl 
ON 
tbl1.id = total_tbl.id 
ORDER BY 
tbl1.id;



 
 
 
 
 
 
 
 
 