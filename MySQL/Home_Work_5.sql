-- Операторы, фильтрация, сортировка и ограничение
-- 1)

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at DATETIME DEFAULT NOW(),
  updated_at DATETIME DEFAULT NOW()
) COMMENT = 'Покупатели';

-- 2)

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at VARCHAR(255),
  updated_at VARCHAR(255)
) COMMENT = 'Покупатели';

INSERT INTO users (name, birthday_at, created_at, updated_at) VALUES
 ('Ivan', '1984-02-28', '20.10.2017 8:10', '20.10.2017 8:10'),
 ('Maria', '2001-02-28', '20.10.2017 8:10', '20.10.2017 8:10');

UPDATE users SET created_at = STR_TO_DATE (created_at, '%d.%m.%Y %h:%i:%s');
UPDATE users SET updated_at = STR_TO_DATE (updated_at, '%d.%m.%Y %h:%i:%s');

ALTER TABLE users CHANGE created_at created_at DATETIME;
ALTER TABLE users CHANGE updated_at updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP;

SELECT * FROM users;

-- 3)

DROP TABLE IF EXISTS storehouses_products;
CREATE TABLE storehouses_products (
  id SERIAL PRIMARY KEY,
  -- storehouse_id INT UNSIGNED,
  -- product_id INT UNSIGNED,
  value INT UNSIGNED COMMENT 'Запас товарной позиции на складе',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Запасы на складе';

INSERT INTO storehouses_products (value) VALUES
 (0),
 (2500),
 (0),
 (30),
 (500),
 (1);

SELECT value FROM storehouses_products ORDER BY value = 0, value;

-- 4)

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

SELECT * FROM
 catalogs
WHERE
 id IN (5, 1, 2) 
ORDER BY 
 id = 5 DESC, 
 id = 1 DESC, 
 id = 2 DESC;

-- 5)

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
  ('Мария', '1992-08-29'),
  ('Светлана', '1988-02-04'),
  ('Олег', '1998-03-20'),
  ('Юлия', '2006-07-12');


SELECT * FROM users WHERE DATE_FORMAT(birthday_at, '%M') IN ('may', 'august');

-- Агрегация данных
-- 1)

SELECT ROUND(AVG(TIMESTAMPDIFF(YEAR, birthday_at, NOW()))) AS average_age FROM users;

-- 2)

SELECT DAYNAME(DATE_FORMAT(birthday_at, '2020-%m-%d')) AS day_of_week, COUNT(*) AS quantity_of_birthdays FROM users GROUP BY day_of_week;

-- 3)


















