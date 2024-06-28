-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: restofinder
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `reserva`
--

DROP TABLE IF EXISTS `reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reserva` (
  `idreserva` int NOT NULL,
  `Mail` varchar(100) NOT NULL,
  `Telefono` int NOT NULL,
  `Fecha_reserva` date NOT NULL,
  `Nombre` varchar(100) DEFAULT NULL,
  `Numero de personas` int NOT NULL,
  `Hora de reserva` time NOT NULL,
  `Restaurante` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idreserva`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserva`
--

LOCK TABLES `reserva` WRITE;
/*!40000 ALTER TABLE `reserva` DISABLE KEYS */;
INSERT INTO `reserva` VALUES (1,'luciahernandez@gmail.com',1135768943,'2024-08-21','Lucia Hernandez',2,'12:00:00','Hierba Buena'),(2,'carlosgomez@gmail.com',1133456789,'2024-08-21','Carlos Gomez',3,'13:00:00','Saigon'),(3,'victorsueiro@gmail.com',1123233114,'2024-08-22','Victor Sueiro',2,'14:00:00','Petit Colon'),(4,'j.sanchez@hotmail.com',1165789087,'2024-10-22','Jorge Sanchez',3,'14:00:00','El Pobre Luis'),(5,'juan.diaz@gmail.com',1156778869,'2024-09-03','Juan Diaz',4,'20:00:00','Clemenza'),(6,'yamilagomez@yahoo.com',1145457777,'2024-10-22','Yamila Gomez',5,'14:00:00','La Continental'),(7,'v.jara@yahoo.com',1135689087,'2024-10-22','Victor Jara',2,'13:00:00','El Ferroviario'),(8,'e.galeano76@gmail.com',1145679087,'2024-09-06','Eduardo Galeano',3,'21:00:00','Petit Colon'),(9,'a.delprado@hotmail.com',1145346789,'2024-09-07','Alejandra del Prado',4,'13:00:00','El Pobre Luis'),(10,'nancyanka@gmail.com',1165478645,'2024-09-07','Nancy Anka',2,'14:00:00','Saigon'),(11,'mariaclarap@gmail.com',1156536309,'2024-08-09','Maria Clara Pazos',3,'15:00:00','Trixie'),(12,'normapilaria@gmail.com',1145690832,'2024-07-03','Norma Pilaria',8,'12:00:00','El Ceibo'),(13,'carlau@gmail.com',1145782830,'2024-08-19','Carla Udaondo',2,'18:00:00','Senses New York'),(14,'mariaduarte@gmail.com',1198464383,'2024-08-05','Maria Duarte',4,'11:00:00','Pizzeria La Meseta'),(15,'Ismagonzalez@gmail.com',1143596960,'2024-07-14','Ismael Gonzalez',9,'21:00:00','Petit Colon'),(16,'norberto1087@gmail.com',1156563800,'2024-08-17','Norberto Maria',2,'19:00:00','Madero Tango'),(17,'luzmaria@gmial.com',1177639022,'2024-07-31','Luz Duarte ',10,'23:00:00','Madero Tango'),(18,'vale1965@gmail.com',1154583055,'2024-07-15','Valeria Munoz',5,'12:00:00','Saigon'),(19,'quimeydiaz@gmail.com',1156839202,'2024-08-27','Quimey Diaz',4,'13:00:00','Clemenza'),(20,'juanidiaz@gmail.com',1158585822,'2024-07-17','Juan Ignacio Diaz',3,'14:00:00','Senses New York');
/*!40000 ALTER TABLE `reserva` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-27 19:44:54
