-- 1. Таблицы заполнил через сервис fillbd


-- 2. Скрипт возвращающий уникальные имена по алфаиту
SELECT DISTINCT firstname FROM users ORDER BY firstname;


-- 3. Скрипт, отмечающий несовершеннолетних пользователей как неактивных

/*
`is_active` BIGINT(1) DEFAULT TRUE

или

`is_active` BIGINT(1) DEFAULT 1
*/


UPDATE 
 profiles 
SET 
 is_active = FALSE 
WHERE 
 ((YEAR(CURRENT_DATE) - YEAR(birthday)) - (DATE_FORMAT(CURRENT_DATE, '%m%d') < DATE_FORMAT(birthday, '%m%d'))) < 18;

-- 4. Скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней)

INSERT INTO `messages` VALUES ('52','1','2','Labore at aut qui rerum qui voluptas molestiae voluptas. Iure unde recusandae repellendus id deleniti.','2021-10-17 14:33:01');

DELETE FROM messages WHERE (CURRENT_DATE < created_at);
