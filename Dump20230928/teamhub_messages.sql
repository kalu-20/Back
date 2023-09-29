-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: teamhub
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id_message` int NOT NULL AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `id_channel` int NOT NULL,
  `content` text COLLATE utf8mb4_general_ci,
  `creation` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_message`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,1,1,'Hola a todos... Tengo un problema con las variables globales. uso una variable \'Time\' que necesito consultar desde varias funciones y me da error. no sé qué hacer.','2023-09-26 14:07:16'),(2,5,1,'Te conviene definir la variable en las primeras líneas de código, para que no te arroje el error al referenciar la variable en las siguientes líneas.','2023-09-26 14:07:16'),(3,3,1,'Hola buen día, actualmente tengo conocimientos en java, C++ y Python. me recomiendan un framework en particular para ciencia de datos? Gracias','2023-09-26 14:07:16'),(4,2,1,'La verdad que este canal me encanta, porque es muy activo y colaborativo en todo sentido. en lo particular me ayudaron bastante. Son Súper!','2023-09-26 14:07:16'),(90,26,4,'sadf','2023-09-28 19:24:16'),(91,26,6,'hola como anadan','2023-09-28 21:08:08'),(92,26,4,'ksnfforhej','2023-09-28 21:09:29'),(93,26,32,'Me gusta','2023-09-28 22:15:23'),(94,26,4,'Acabo de comer budin','2023-09-28 23:44:02'),(95,26,4,'Y me tome muho cafe','2023-09-28 23:44:18'),(96,27,32,'yo conozco un par de sus temas, habia uno que sonaba a un tema de Michael Jackson','2023-09-28 23:55:27');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-28 22:25:32
