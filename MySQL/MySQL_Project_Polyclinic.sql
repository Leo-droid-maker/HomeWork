-- CREATE DATABASE IF NOT EXISTS polyclinic;
-- USE polyclinic;

-- DROP TABLE IF EXISTS outpatient_department;
CREATE TABLE IF NOT EXISTS outpatient_department (
	id SERIAL PRIMARY KEY,
	department_name VARCHAR(255) COMMENT 'Название отделения',
	INDEX department_idx(department_name)
) COMMENT 'Отделения поликлиники'; 

-- DROP TABLE IF EXISTS prof_position;
CREATE TABLE IF NOT EXISTS prof_position (
	id SERIAL PRIMARY KEY,
	position_name VARCHAR(255) COMMENT 'Название должности',
	department_id BIGINT UNSIGNED NOT NULL, 
	INDEX position_idx(position_name),
	FOREIGN KEY (department_id) REFERENCES outpatient_department(id)
) COMMENT 'Должности';

-- DROP TABLE IF EXISTS adress;
CREATE TABLE IF NOT EXISTS adress (
	id SERIAL PRIMARY KEY,
	city VARCHAR(255),
	street_name VARCHAR(255),
	building BIGINT UNSIGNED NOT NULL
) COMMENT 'Обслуживаемые адреса';

-- DROP TABLE IF EXISTS disrtrict;
CREATE TABLE IF NOT EXISTS district (
	district_id BIGINT UNSIGNED NOT NULL,
	adress_id BIGINT UNSIGNED NOT NULL,
	PRIMARY KEY (district_id, adress_id),
	FOREIGN KEY (adress_id) REFERENCES adress(id)
) COMMENT 'Участки';

-- DROP TABLE IF EXISTS doctors;
CREATE TABLE IF NOT EXISTS doctors (
	id SERIAL PRIMARY KEY,
	first_middle_last_name VARCHAR(255),
	doctor_position BIGINT UNSIGNED NOT NULL,
	work_district BIGINT UNSIGNED,
	education TEXT,
	department BIGINT UNSIGNED NOT NULL,
	qualification_category TEXT,
	INDEX first_middle_last_name_idx(first_middle_last_name),
	FOREIGN KEY (doctor_position) REFERENCES prof_position(id),
	FOREIGN KEY (work_district) REFERENCES district(district_id),
	FOREIGN KEY (department) REFERENCES outpatient_department(id)
) COMMENT 'Доктора';

CREATE TABLE IF NOT EXISTS diagnosis (
	id SERIAL PRIMARY KEY,
	diagnosis_name VARCHAR(255),
	INDEX diagnosis_name_idx(diagnosis_name)
) COMMENT 'Диагноз';

CREATE TABLE IF NOT EXISTS visit_purpose (
	id SERIAL PRIMARY KEY,
	discription VARCHAR(255)
) COMMENT 'Цель посещения';

/*Причинами для посещений, 
не связанных с оказанием медицинской помощи, являются: выписка льготного рецепта, 
получение заключения при оформлении посыльного листа на медико-социальную экспертизу, 
санаторно-курортной карты, для предоставления в другие учреждения, справок; выписка направлений на анализы, 
исследования и получения их результатов, направлений на консультации, госпитализации в другие учреждения*/

-- DROP TABLE IF EXISTS patient;
CREATE TABLE IF NOT EXISTS patient (
	medical_card_id BIGINT UNSIGNED NOT NULL,
	full_name VARCHAR(255),
	birthday DATE,
	patient_adress VARCHAR(255),
	gender CHAR(1),
	disability ENUM('отсутствует', 'первая', 'вторая', 'третья', 'ребенок-инвалид'),
	INDEX medical_card_idx(medical_card_id),
	PRIMARY KEY (medical_card_id)
) COMMENT 'Пациент';

CREATE TABLE IF NOT EXISTS visit (
	id SERIAL PRIMARY KEY,
	status ENUM('первичное', 'вторичное'),
	diagnosis_id BIGINT UNSIGNED DEFAULT NULL,
	purpose_id BIGINT UNSIGNED NOT NULL,
	patient_medical_card_id BIGINT UNSIGNED NOT NULL,
	doctor_id BIGINT UNSIGNED NOT NULL,
	date_of_visit DATETIME DEFAULT NOW(),
	INDEX visit_idx(id),
	FOREIGN KEY (diagnosis_id) REFERENCES diagnosis(id),
	FOREIGN KEY (purpose_id) REFERENCES visit_purpose(id),
	FOREIGN KEY (patient_medical_card_id) REFERENCES patient(medical_card_id),
	FOREIGN KEY (doctor_id) REFERENCES doctors(id)
) COMMENT 'Посещение';






















