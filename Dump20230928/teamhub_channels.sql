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
-- Table structure for table `channels`
--

DROP TABLE IF EXISTS `channels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `channels` (
  `id_channel` int NOT NULL AUTO_INCREMENT,
  `id_server` int NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `description` text COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`id_channel`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channels`
--

LOCK TABLES `channels` WRITE;
/*!40000 ALTER TABLE `channels` DISABLE KEYS */;
INSERT INTO `channels` VALUES (1,1,'#Mundo Fantástico','Si eres un buscador de tesoros literarios, un fanático de lo épico o simplemente alguien que busca escapar por un rato, \"Mundos Fantásticos\" es tu destino definitivo.'),(2,1,'#Escritores Emergentes','Adéntrate en los mundos de la literatura fantástica con los escritores emergentes más prometedores de nuestro tiempo.'),(3,1,'#Recomendaciones','Cada semana, te ofrecemos reseñas de libros, análisis profundos de los personajes y las tramas, recomendaciones para todos los gustos y debates apasionados del género.'),(4,8,'#Preguntas Técnicas','Este es tu destino para resolver todas tus dudas y explorar el intrincado mundo de la programación web.'),(5,8,'#Proyectos Compartidos','Nuestro canal es un espacio de aprendizaje colaborativo donde puedes compartir tus conocimientos, proyectos, hacer preguntas técnicas y mantenerte al día con las últimas herramientas y tecnología web.'),(6,8,'#Recursos Útiles','Nuestro canal es un espacio de aprendizaje colaborativo donde puedes compartir tus conocimientos, proyectos, hacer preguntas técnicas y mantenerte al día con las últimas herramientas y tecnología web.'),(31,20,'chanel 1',NULL),(32,7,'luis miguel',NULL),(33,7,'luis miguel',NULL);
/*!40000 ALTER TABLE `channels` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-28 22:25:31
