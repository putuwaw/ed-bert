DROP TABLE IF EXISTS `report`;
CREATE TABLE `report` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text` varchar(500) DEFAULT NULL,
  `predicted` varchar(45) DEFAULT NULL,
  `actual` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

