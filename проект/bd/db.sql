CREATE DATABASE IF NOT EXISTS `pythonlogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `pythonlogin`;

CREATE TABLE IF NOT EXISTS `accounts` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`username` varchar(50) NOT NULL,
`password` varchar(255) NOT NULL,
`email` varchar(100) NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `program` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`program_name` varchar(100) NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `company` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`company_name` varchar(100) NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `form` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`name` varchar(50) NOT NULL,
`email` varchar(50) NOT NULL,
`number` varchar(11) NOT NULL,
`prog` varchar(50) NOT NULL,
`comp` varchar(50) NOT NULL,
`date/comp` date NOT NULL,
`comment` varchar(250) NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (1, 'admin', 'admin', 'admin@admin.com');
INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (2, 'FunToYou', 'xwrsjfs54js', 'FunToYou.ru');
INSERT INTO `form` (`id`, `name`, `email`, `number`, `prog`, `comp`, `date/comp`, `comment`) VALUES (1, 'Яна', 'ypopkova02@mail.ru', '79121157137', 'Фиксики', 'FunToYOU', '20-05-2024','' );
INSERT INTO `form` (`id`, `name`, `email`, `number`, `prog`, `comp`, `date/comp`, `comment`) VALUES (9, 'Саша', 'alex@mail.ru', '79121157138', 'Шоу_мыльных_пузырей', 'FunToYOU', '06-06-2024','');
INSERT INTO `form` (`id`, `name`, `email`, `number`, `prog`, `comp`, `date/comp`, `comment`) VALUES (10, 'Мария', 'maria@mail.ru', '79121157139', '3D_анимация', 'FunToYOU', '07-06-2024','');
INSERT INTO `form` (`id`, `name`, `email`, `number`, `prog`, `comp`, `date/comp`, `comment`) VALUES (11, 'Даша', 'daria@mail.ru', '79121157140', 'Акробатическое_шоу', 'FunToYOU', '25-05-2024','');
INSERT INTO `form` (`id`, `name`, `email`, `number`, `prog`, `comp`, `date/comp`, `comment`) VALUES (12, 'Яна', 'FunToYou703@mail.ru', '79121157137', 'Заявкакомпании', 'Заявкакомпании', 'FunToYou', 'Фиксики, смешарики, ...');
INSERT INTO `form` (`id`, `name`, `email`, `number`, `prog`, `comp`, `date/comp`, `comment`) VALUES (14, 'Екатерина', 'Virtual@mail.ru', '79121157138', 'Заявкакомпании', 'Заявкакомпании', 'Virtual', 'Фиксики, смешарики, ...');
INSERT INTO `form` (`id`, `name`, `email`, `number`, `prog`, `comp`, `date/comp`, `comment`) VALUES (15, 'Сергей', 'serg@mail.ru', '79121157190', 'Заявкакомпании', 'Заявкакомпании', 'Арт-студио', 'Огненое шоу, ...');
INSERT INTO `form` (`id`, `name`, `email`, `number`, `prog`, `comp`, `date/comp`, `comment`) VALUES (16, 'Оксана', 'milankina@mail.ru', '79045567895', '3D_анимация', 'Virtual', '2024-06-17', '');
INSERT INTO `form` (`id`, `name`, `email`, `number`, `prog`, `comp`, `date/comp`, `comment`) VALUES (17, 'Станислав', 'fedotovST@mail.ru', '79129456846', 'Шоу_мыльных_пузырей', 'Арт-студио', '2024-05-12', 'Будет много детей.');

SELECT * FROM accounts;

SELECT * FROM form;

select * from form
WHERE prog = '3D_анимация';

select * from form
WHERE prog = 'Заявкакомпании';

select * from form
WHERE comp = 'FunToYOU';

DELETE FROM form
WHERE id=9;

UPDATE form SET prog = 'Шоу иллюзии'
WHERE id = 10;

DROP table form;
DROP table accounts;
DROP database pythonlogin;