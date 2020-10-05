-- 1)

SELECT from_user_id, COUNT(*) AS number_of_messages FROM messages WHERE to_user_id = 1 GROUP BY from_user_id ORDER BY number_of_messages DESC LIMIT 1;

-- 2)

DROP TABLE IF EXISTS likes;
CREATE TABLE likes(
	id SERIAL PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    media_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME DEFAULT NOW()
    , FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE restrict
    , FOREIGN KEY (media_id) REFERENCES media(id)
);
INSERT INTO `likes` VALUES 
('1','1','1','1988-10-14 18:47:39'),
('2','2','1','1988-09-04 16:08:30'),
('3','3','1','1994-07-10 22:07:03'),
('4','4','1','1991-05-12 20:32:08'),
('5','5','2','1978-09-10 14:36:01'),
('6','6','2','1992-04-15 01:27:31'),
('7','7','2','2003-02-03 04:56:27'),
('8','8','8','2017-04-24 09:30:19'),
('9','9','9','1974-02-07 20:53:55'),
('10','10','10','1973-05-11 03:21:40'),
('11','11','11','2008-12-17 13:03:56'),
('12','12','12','1995-07-17 21:22:38'),
('13','13','13','1985-09-07 23:34:21'),
('14','14','14','1973-01-27 23:11:53'),
('15', '27', '1', '1973-05-11 03:21:40'),
('16', '27', '2', '1973-05-11 03:21:40')
; 

SELECT 
 user_id, 
COUNT(*) 
AS 
 number_of_likes 
FROM 
 likes 
WHERE 
 user_id IN (SELECT user_id FROM profiles WHERE TIMESTAMPDIFF(YEAR, birthday, NOW()) < 10) 
GROUP BY 
 user_id;

-- 3)

-- общее количество профилей мужчин и женщин по полу

SELECT gender, COUNT(*) FROM profiles GROUP BY gender;

-- общее количество лайков от женщин

SELECT COUNT(*) FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'f');

-- общее количество лайков от мужчин

SELECT COUNT(*) FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'm');


-- задание

SELECT
CASE
WHEN
(SELECT COUNT(*) FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'm'))
  > 
(SELECT COUNT(*) FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'f'))
THEN 'количество лайков от мужчин больше'
WHEN
(SELECT COUNT(*) FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'm'))
  < 
(SELECT COUNT(*) FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'f'))
THEN 'количество лайков от женщин больше'
ELSE 'количество лайков одинаково от мужчин и женщин'
END AS total_likes
FROM likes GROUP BY total_likes;








