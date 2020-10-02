DROP TABLE IF EXISTS friends;
CREATE TABLE friends (
	user_id BIGINT UNSIGNED NOT NULL,
	friend_user_id BIGINT UNSIGNED NOT NULL,
	friend_photo_id BIGINT UNSIGNED NULL, -- создал после таблицы media
	friend_firstname VARCHAR(50),
	friend_lastname VARCHAR(50) COMMENT 'Фамилия',
	
	PRIMARY KEY (user_id, friend_user_id),
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (friend_user_id) REFERENCES users(id),
	FOREIGN KEY (friend_photo_id) REFERENCES media(id),
	
	INDEX friend_firstname_lastname_idx(friend_firstname, friend_lastname) -- для поиска по друзьям
) COMMENT 'друзья';

ALTER TABLE friends 
ADD CHECK(user_id <> friend_user_id);

/* Дальше я попробовал посчитать сколько всего друзей у пользователей.
 * Логика такова: Создается таблица total_count_of_friends(столбцы user_id и friend_total_number -  сколько раз он упоминается в таблице friends)
 */
DROP TABLE IF EXISTS total_count_of_friends;
CREATE TABLE total_count_of_friends (
	SELECT user_id, COUNT(user_id) AS friend_total_number FROM friends GROUP BY user_id
);

DROP TABLE IF EXISTS video_albums;
CREATE TABLE video_albums (
	id SERIAL,
	name VARCHAR(255) DEFAULT NULL,
    user_id BIGINT UNSIGNED DEFAULT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS videos;
CREATE TABLE videos (
	id SERIAL,
	album_id BIGINT UNSIGNED NOT NULL,
	media_id BIGINT UNSIGNED NOT NULL,

	FOREIGN KEY (album_id) REFERENCES video_albums(id),
    FOREIGN KEY (media_id) REFERENCES media(id)
);