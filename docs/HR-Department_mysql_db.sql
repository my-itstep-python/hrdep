CREATE TABLE `departments` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(100) NOT NULL UNIQUE,
	PRIMARY KEY (`id`)
);

CREATE TABLE `employees` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(100) NOT NULL,
	`age` int NOT NULL,
	`position` varchar(100) NOT NULL,
	`salary` FLOAT NOT NULL,
	`dep_id` int NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `employees` ADD CONSTRAINT `employees_fk0` FOREIGN KEY (`dep_id`) REFERENCES `departments`(`id`);

