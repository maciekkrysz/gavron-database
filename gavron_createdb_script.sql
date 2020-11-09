SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `account` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `Login` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL CHECK (length(Password) >= 10),
  PRIMARY KEY (Id),
  UNIQUE (Login)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `drone` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `Model` varchar(50) NOT NULL,
  PRIMARY KEY (Id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `flaw` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `IdUser` int(10) NOT NULL,
  `IdFlight` int(10) NOT NULL,
  `IdDrone` int(10) NOT NULL,
  `Description` varchar(255) NOT NULL,
  PRIMARY KEY (Id),
  KEY `IdDrone` (`IdDrone`),
  KEY `IdFlight` (`IdFlight`),
  KEY `IdUser` (`IdUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `flight` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `IdDrone` int(10) NOT NULL,
  `IdFlightSchedule` int(10) NOT NULL,
  `StartDate` datetime DEFAULT NULL,
  PRIMARY KEY (Id),
  KEY `FK_FlightSchedule` (`IdFlightSchedule`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `flightschedule` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `IdUser` int(11) NOT NULL,
  `IdRoute` int(11) NOT NULL,
  `StartDate` date NOT NULL,
  `StartMinute` time NOT NULL,
  `Interval_` int(11) NOT NULL,
  PRIMARY KEY (Id),
  KEY `IdUser` (`IdUser`),
  KEY `IdRoute` (`IdRoute`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `log` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `IdFlight` int(10) NOT NULL,
  `SecondsSinceStart` int(10) NOT NULL,
  `Longitude` float NOT NULL CHECK (Longitude > -180 && Longitude < 180),
  `Latitude` float NOT NULL CHECK (Latitude > -90 && Latitude < 90),
  `Altitude` float NOT NULL,
  PRIMARY KEY (Id),
  KEY `IdFlight` (`IdFlight`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `object` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `IdFlight` int(10) NOT NULL,
  `IdObjectType` int(10) NOT NULL,
  `PathToPhoto` varchar(255) NOT NULL,
  PRIMARY KEY (Id),
  KEY `FK_ObjectType` (`IdObjectType`),
  KEY `FK_Flight` (`IdFlight`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `objecttype` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  PRIMARY KEY (Id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `point` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `IdPointType` int(10) NOT NULL,
  `Longitude` float NOT NULL CHECK (Longitude > -180 && Longitude < 180),
  `Latitude` float NOT NULL CHECK (Latitude > -90 && Latitude < 90),
  PRIMARY KEY (Id),
  KEY `IdPointType` (`IdPointType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `pointonroute` (
  `IdRoute` int(10) NOT NULL AUTO_INCREMENT,
  `IdPoint` int(10) NOT NULL,
  `Order_` int(10) DEFAULT NULL,
  PRIMARY KEY (`IdRoute`,`IdPoint`, `Order_`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `pointtype` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `NamePointType` varchar(50) DEFAULT NULL,
  PRIMARY KEY (Id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `role` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `NameRole` int(11) NOT NULL,
  PRIMARY KEY (Id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `route` (
  `Id` int(10) NOT NULL AUTO_INCREMENT,
  `Description` varchar(50) NOT NULL,
  PRIMARY KEY (Id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `user` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `IdAccount` int(11) NOT NULL,
  `IdRole` int(11) NOT NULL,
  PRIMARY KEY (Id),
  KEY `IdRole` (`IdRole`),
  KEY `IdAccount` (`IdAccount`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `flaw`
  ADD CONSTRAINT `flaw_ibfk_1` FOREIGN KEY (`IdDrone`) REFERENCES `drone` (`Id`),
  ADD CONSTRAINT `flaw_ibfk_2` FOREIGN KEY (`IdFlight`) REFERENCES `flight` (`Id`),
  ADD CONSTRAINT `flaw_ibfk_3` FOREIGN KEY (`IdUser`) REFERENCES `user` (`Id`);

ALTER TABLE `flight`
  ADD CONSTRAINT `FK_Drone` FOREIGN KEY (`IdDrone`) REFERENCES `drone` (`Id`),
  ADD CONSTRAINT `FK_FlightSchedule` FOREIGN KEY (`IdFlightSchedule`) REFERENCES `flightschedule` (`Id`);

ALTER TABLE `flightschedule`
  ADD CONSTRAINT `flightschedule_ibfk_1` FOREIGN KEY (`IdUser`) REFERENCES `user` (`Id`),
  ADD CONSTRAINT `flightschedule_ibfk_2` FOREIGN KEY (`IdRoute`) REFERENCES `route` (`Id`);

ALTER TABLE `log`
  ADD CONSTRAINT `log_ibfk_1` FOREIGN KEY (`IdFlight`) REFERENCES `flight` (`Id`);

ALTER TABLE `object`
  ADD CONSTRAINT `FK_Flight` FOREIGN KEY (`IdFlight`) REFERENCES `flight` (`Id`),
  ADD CONSTRAINT `FK_ObjectType` FOREIGN KEY (`IdObjectType`) REFERENCES `objecttype` (`Id`);

ALTER TABLE `point`
  ADD CONSTRAINT `point_ibfk_1` FOREIGN KEY (`IdPointType`) REFERENCES `pointtype` (`Id`);

ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`IdRole`) REFERENCES `role` (`Id`),
  ADD CONSTRAINT `user_ibfk_2` FOREIGN KEY (`IdAccount`) REFERENCES `account` (`Id`);
COMMIT;