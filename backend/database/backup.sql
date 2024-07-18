-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cinema
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
-- Table structure for table `asientos_reservados`
--

DROP TABLE IF EXISTS `asientos_reservados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asientos_reservados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `funcion_id` int DEFAULT NULL,
  `asientos` json DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `asientos_reservados_ibfk_1` (`funcion_id`),
  CONSTRAINT `asientos_reservados_ibfk_1` FOREIGN KEY (`funcion_id`) REFERENCES `funciones` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=226 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asientos_reservados`
--

LOCK TABLES `asientos_reservados` WRITE;
/*!40000 ALTER TABLE `asientos_reservados` DISABLE KEYS */;
INSERT INTO `asientos_reservados` VALUES (200,98,'[{\"user\": \"Bryan26\", \"asientos\": [[3, 4], [5, 4], [2, 5], [3, 3], [5, 6], [3, 6], [5, 3], [2, 4], [3, 5], [5, 5], [2, 3], [2, 6]]}, {\"user\": \"SteveSant\", \"asientos\": [[10, 5], [2, 8], [2, 7], [3, 7], [10, 6], [5, 2]]}, {\"user\": \"Saori\", \"asientos\": [[4, 4], [3, 8], [2, 7], [5, 8], [3, 7], [4, 6], [5, 1], [5, 7], [4, 5], [2, 6], [4, 8], [3, 6], [2, 5], [4, 7]]}, {\"user\": \"Luis16\", \"asientos\": [[4, 3], [4, 2]]}, {\"user\": \"Naomi\", \"asientos\": [[3, 1], [2, 2], [2, 1], [3, 2], [4, 1]]}, {\"user\": \"steven123\", \"asientos\": [[4, 10], [4, 9], [2, 10], [3, 10], [2, 9], [5, 10], [3, 9], [5, 9]]}]'),(201,97,'[{\"user\": \"Saori\", \"asientos\": [[2, 4], [3, 4], [2, 6], [3, 6], [2, 5], [3, 5]]}, {\"user\": \"Bryan26\", \"asientos\": [[2, 1], [2, 7], [3, 1], [3, 7], [2, 2], [3, 2]]}, {\"user\": \"Naomi\", \"asientos\": [[2, 3], [3, 3]]}, {\"user\": \"SteveSant\", \"asientos\": [[11, 5], [11, 6]]}]'),(202,13,'[{\"user\": \"Bryan26\", \"asientos\": [[2, 4], [2, 7], [2, 3], [2, 6], [2, 5], [2, 8]]}, {\"user\": \"Saori\", \"asientos\": [[3, 5], [3, 6]]}]'),(203,16,'[{\"user\": \"Bryan26\", \"asientos\": [[2, 7], [3, 7], [2, 6], [3, 6], [2, 5], [3, 5]]}, {\"user\": \"Saori\", \"asientos\": [[2, 3], [2, 4], [3, 3], [3, 4]]}]'),(204,28,'[{\"user\": \"Saori\", \"asientos\": [[2, 3], [2, 4], [2, 1], [2, 2]]}, {\"user\": \"Bryan26\", \"asientos\": [[3, 2], [3, 3]]}]'),(205,34,'[{\"user\": \"Saori\", \"asientos\": [[4, 4], [2, 4], [3, 4], [2, 3], [4, 5], [3, 3], [2, 6], [3, 6], [2, 5], [3, 5]]}]'),(206,37,'[{\"user\": \"Saori\", \"asientos\": [[2, 3], [2, 4], [2, 5], [2, 6]]}, {\"user\": \"steven123\", \"asientos\": [[3, 4]]}]'),(207,19,'[{\"user\": \"Bryan26\", \"asientos\": [[2, 5], [2, 6], [3, 5], [3, 6]]}]'),(208,31,'[{\"user\": \"Bryan26\", \"asientos\": [[4, 4], [2, 5], [2, 6], [3, 4]]}, {\"user\": \"Saori\", \"asientos\": [[2, 4], [2, 7], [4, 3], [3, 7], [4, 6], [2, 3], [4, 5], [3, 3], [3, 6], [4, 7], [3, 5]]}]'),(210,58,'[{\"user\": \"Saori\", \"asientos\": [[2, 3], [2, 4]]}]'),(211,25,'[{\"user\": \"Saori\", \"asientos\": [[2, 3], [3, 2], [3, 3], [2, 2]]}, {\"user\": \"Luis16\", \"asientos\": [[3, 1], [2, 1], [4, 1], [5, 1]]}]'),(212,24,'[{\"user\": \"Saori\", \"asientos\": [[3, 4], [3, 7], [3, 3], [3, 6], [3, 5]]}]'),(213,93,'[{\"user\": \"SteveSant\", \"asientos\": [[2, 7]]}, {\"user\": \"Saori\", \"asientos\": [[2, 4], [2, 5], [2, 6]]}]'),(214,94,'[{\"user\": \"Pablo\", \"asientos\": [[2, 1], [2, 2]]}]'),(215,88,'[{\"user\": \"Saori\", \"asientos\": [[2, 4], [3, 4], [2, 7], [3, 7], [2, 6], [3, 6], [2, 5], [3, 5]]}]'),(216,47,'[{\"user\": \"Saori\", \"asientos\": [[2, 7], [3, 7], [2, 6], [3, 6], [2, 5], [3, 5]]}]'),(218,26,NULL),(219,27,NULL),(220,89,NULL),(221,49,'[{\"user\": \"Saori\", \"asientos\": [[2, 3], [2, 4], [2, 2]]}]'),(222,52,'[{\"user\": \"Saori\", \"asientos\": [[2, 2]]}]'),(224,55,'[{\"user\": \"Saori\", \"asientos\": [[2, 3]]}]'),(225,103,NULL);
/*!40000 ALTER TABLE `asientos_reservados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comentarios`
--

DROP TABLE IF EXISTS `comentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comentarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `pelicula_id` int NOT NULL,
  `comentario` text NOT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `comentarios_ibfk_1` (`pelicula_id`),
  KEY `comentarios_ibfk_2` (`usuario_id`),
  CONSTRAINT `comentarios_ibfk_1` FOREIGN KEY (`pelicula_id`) REFERENCES `peliculas` (`id`) ON DELETE CASCADE,
  CONSTRAINT `comentarios_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comentarios`
--

LOCK TABLES `comentarios` WRITE;
/*!40000 ALTER TABLE `comentarios` DISABLE KEYS */;
INSERT INTO `comentarios` VALUES (19,26,315162,'Que bonito gato','2024-07-13 04:28:30'),(22,27,719221,'Menuda basura','2024-07-14 04:29:09'),(24,26,573435,'Estuve esperando esta peli por mucho tiempo','2024-07-14 19:33:44'),(25,31,315162,'Me gusto mucho la pelicula','2024-07-16 01:23:52'),(26,32,315162,'HOLA MUNDO','2024-07-16 13:29:21');
/*!40000 ALTER TABLE `comentarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funciones`
--

DROP TABLE IF EXISTS `funciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pelicula_id` int DEFAULT NULL,
  `sala_id` int DEFAULT NULL,
  `hora` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pelicula_id` (`pelicula_id`),
  KEY `funciones_ibfk_2` (`sala_id`),
  CONSTRAINT `funciones_ibfk_1` FOREIGN KEY (`pelicula_id`) REFERENCES `peliculas` (`id`) ON DELETE CASCADE,
  CONSTRAINT `funciones_ibfk_2` FOREIGN KEY (`sala_id`) REFERENCES `salas` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funciones`
--

LOCK TABLES `funciones` WRITE;
/*!40000 ALTER TABLE `funciones` DISABLE KEYS */;
INSERT INTO `funciones` VALUES (13,614933,16,'14:30:00'),(14,614933,17,'17:30:00'),(15,614933,18,'20:00:00'),(16,639720,19,'14:00:00'),(17,639720,20,'17:00:00'),(18,639720,21,'20:00:00'),(19,653346,22,'14:00:00'),(20,653346,23,'17:00:00'),(21,653346,24,'20:00:00'),(22,704673,25,'14:00:00'),(23,704673,26,'17:00:00'),(24,704673,1,'20:00:00'),(25,719221,2,'14:00:00'),(26,719221,3,'17:00:00'),(27,719221,4,'20:00:00'),(28,748783,5,'14:00:00'),(29,748783,7,'17:00:00'),(30,748783,8,'20:00:00'),(31,762441,11,'14:00:00'),(32,762441,12,'17:00:00'),(33,762441,13,'20:00:00'),(34,786892,14,'14:00:00'),(35,786892,15,'17:00:00'),(36,786892,16,'20:00:00'),(37,829402,17,'14:00:00'),(38,829402,18,'17:00:00'),(39,829402,19,'20:00:00'),(43,1001311,23,'14:00:00'),(44,1001311,24,'17:00:00'),(45,1001311,25,'20:00:00'),(46,1012201,26,'14:00:00'),(47,1012201,1,'17:00:00'),(48,1012201,2,'20:00:00'),(49,1022789,3,'14:00:00'),(50,1022789,4,'17:00:00'),(51,1022789,5,'20:00:00'),(52,1025463,7,'14:00:00'),(53,1025463,8,'17:00:00'),(54,1025463,11,'20:00:00'),(55,1026999,12,'14:00:00'),(56,1026999,13,'17:00:00'),(57,1026999,14,'20:00:00'),(58,1061474,15,'14:00:00'),(59,1061474,16,'17:00:00'),(60,1061474,17,'20:00:00'),(61,1086747,18,'14:00:00'),(62,1086747,19,'17:00:00'),(63,1086747,20,'20:00:00'),(64,1143019,21,'14:00:00'),(65,1143019,22,'17:00:00'),(66,1143019,23,'20:00:00'),(75,1012201,12,'19:00:00'),(76,1012201,12,'21:00:00'),(77,1012201,12,'23:00:00'),(78,829402,17,'16:00:00'),(79,829402,17,'18:00:00'),(80,829402,17,'20:00:00'),(81,829402,17,'22:00:00'),(83,653346,23,'18:00:00'),(85,614933,17,'18:30:00'),(87,1020896,1,'23:30:00'),(88,1020896,1,'18:00:00'),(89,639720,19,'15:00:00'),(90,1020896,1,'23:00:00'),(91,1020896,3,'23:00:00'),(92,929590,16,'23:45:00'),(93,929590,16,'18:45:00'),(94,929590,25,'16:45:00'),(95,762441,12,'20:00:00'),(97,573435,8,'01:00:00'),(98,315162,1,'10:00:00'),(103,280180,16,'18:30:00');
/*!40000 ALTER TABLE `funciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peliculas`
--

DROP TABLE IF EXISTS `peliculas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `peliculas` (
  `id` int NOT NULL,
  `ruta_imagen` varchar(200) NOT NULL,
  `titulo` varchar(150) NOT NULL,
  `sinopsis` text,
  `genero` varchar(255) DEFAULT NULL,
  `duracion` varchar(20) DEFAULT NULL,
  `estreno` date DEFAULT NULL,
  `promedio_votos` decimal(3,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peliculas`
--

LOCK TABLES `peliculas` WRITE;
/*!40000 ALTER TABLE `peliculas` DISABLE KEYS */;
INSERT INTO `peliculas` VALUES (280180,'https://image.tmdb.org/t/p/original//kmIaT03NZ58gmc0pQZkFUCqMcf1.jpg','Superdetective en Hollywood: Axel F.','Cuatro décadas después de su inolvidable primer caso en Beverly Hills, el detective de Detroit Axel Foley vuelve a lo que mejor se le da: resolver crímenes y sembrar el caos.','Acción, Comedia, Crimen','1h 58m','2024-06-20',6.92),(315162,'https://image.tmdb.org/t/p/original//b5Jb7GoQaqIXy4VEdnQa0UrQZI.jpg','El Gato con Botas: El último deseo','El Gato con Botas se embarca en un viaje épico para encontrar al mítico Último Deseo y recuperar sus nueve vidas','Animación, Aventura, Fantasía, Comedia, Familia','1h 43m','2022-12-07',8.24),(573435,'https://m.media-amazon.com/images/M/MV5BY2U5YmQ3YjgtM2I2OC00YmM5LTkyM2MtN2I5Zjg2MDE0ODkwXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_.jpg','Bad Boys: Ride or Die','Tras escuchar falsas acusaciones sobre su excapitán y mentor Mike y Marcus deciden investigar el asunto incluso volverse los más buscados de ser necesarios','Acción, Crimen, Suspense, Comedia','1h 55m','2024-06-05',7.00),(614933,'https://hips.hearstapps.com/hmg-prod/images/poster-peliculas-terror-2019-annabelle-3-1578395572.jpg','Atlassss','Una brillante analista antiterrorista recela de la IA hasta que descubre que podría ser su única esperanza cuando se tuerce una misión para atrapar a un robot rebelde.','Ciencia ficción, Acción, HOLA','2h 0m','2024-05-23',6.84),(639720,'https://image.tmdb.org/t/p/original//8RgGuC7w8JxhykauzTC4bwha1J8.jpg','Amigos imaginarios','Una niña pasa por una experiencia difícil y entonces empieza a ver a los amigos imaginarios de todo el mundo que se han ido quedando atrás a medida que sus amigos de la vida real han ido creciendo.','Comedia, Fantasía, Familia','1h 44m','2024-05-08',7.50),(653346,'https://image.tmdb.org/t/p/original//kkFn3KM47Qq4Wjhd8GuFfe3LX27.jpg','El reino del planeta de los simios','Ambientada varias generaciones en el futuro tras el reinado de César, en la que los simios son la especie dominante que vive en armonía y los humanos se han visto reducidos a vivir en la sombra. Mientras un nuevo y tiránico líder simio construye su imperio, un joven simio emprende un angustioso viaje que le llevará a cuestionarse todo lo que sabe sobre el pasado y a tomar decisiones que definirán el futuro de simios y humanos por igual.','Ciencia ficción, Aventura, Acción','2h 25m','2024-05-08',6.87),(704673,'https://image.tmdb.org/t/p/original//ejlwgCS2SJDFvlTlO8tZYPtCci4.jpg','Detonantes','Una soldado de las fuerzas especiales descubre una peligrosa conspiración cuando regresa a casa en busca de respuestas sobre la muerte de su padre.','Acción, Crimen, Suspense','1h 47m','2024-06-20',5.70),(719221,'https://es.web.img3.acsta.net/pictures/24/01/30/17/04/1436327.jpg','Tarot','Un grupo de amigos de la universidad comienzan a morir de maneras relacionadas con su fortuna después de que les lean los horóscopos.','Terror','1h 32m','2024-05-01',6.67),(748783,'https://image.tmdb.org/t/p/original//6QR2FOCQr41gSduN70WulRIhJb7.jpg','Garfield: la película','El mundialmente famoso Garfield, el gato casero que odia los lunes y que adora la lasaña, está a punto de vivir una aventura ¡en el salvaje mundo exterior! Tras una inesperada reunión con su largamente perdido padre – el desaliñado gato callejero Vic – Garfield y su amigo canino Odie se ven forzados a abandonar sus perfectas y consentidas vidas al unirse a Vic en un hilarante y muy arriesgado atraco.','Animación, Comedia, Familia, Aventura','1h 41m','2024-04-30',6.80),(762441,'https://image.tmdb.org/t/p/original//jGOi939xU8BDRfAAhN6eiTSf3H8.jpg','Un lugar tranquilo: Día uno','Una mujer llamada Sam trata de sobrevivir a una invasión en la ciudad de Nueva York por criaturas alienígenas sedientas de sangre con oídos ultrasónicos. Tercera entrega de la saga.','Terror, Ciencia ficción, Suspense','1h 39m','2024-06-26',7.09),(786892,'https://image.tmdb.org/t/p/original//tGHUlykWn9V2IIQ4ZaATIAq9VLB.jpg','Furiosa: De la saga Mad Max','En un mundo postapocalíptico donde todo ha perdido su valor, los pocos supervivientes se guían por la ley del más fuerte. Sin aprecio por la vida, lo único que despierta un brutal interés es la gasolina, sinónimo de poder y objetivo de bandas armadas hasta los dientes y sin escrúpulos. En este contexto conoceremos la  historia de la arrebatadoramente despiadada, salvaje y joven Furiosa, quien cae en manos de una horda de motoristas y debe sobrevivir a muchas pruebas mientras reúne los medios para encontrar el camino de vuelta a casa. Precuela de \'Mad Max: Furia en la carretera\' (2015).','Acción, Aventura, Ciencia ficción','2h 28m','2024-05-22',7.72),(829402,'https://image.tmdb.org/t/p/original//2D7SsqU8VZOl838KR7q9pzljaLe.jpg','Ultraman: El Ascenso','La historia sigue al exitoso jugador de béisbol llamado Ken Sato, quien regresa a Japón para asumir la identidad de Ultraman. Sin embargo, sus planes se trastocan cuando se enucnetra a un kaiju recién nacido a quien decide criar como su propio hijo. Sumado a este imprevisto, Sato deberá retomar la relación con su distanciado padre y lidiar con la Fuerza de Defensa Kaiju.','Animación, Ciencia ficción, Familia, Acción','1h 56m','2024-06-14',8.43),(929590,'https://image.tmdb.org/t/p/original//iCOQUVVaPqRuR3JqF71akguf6Mj.jpg','Civil War','En un futuro cercano, donde América está sumida en una cruenta guerra civil, un equipo de periodistas y fotógrafos de guerra emprenderá un viaje por carretera en dirección a Washington DC. Su misión: llegar antes de que las fuerzas rebeldes asalten la Casa Blanca y arrebaten el control al presidente de Estados Unidos.','Bélica, Acción, Drama','1h 49m','2024-04-10',7.00),(987686,'lsll','Un asunto familiar','¿Puede haber algo peor que trabajar como asistente para una caprichosa estrella del cine que no te toma en serio? Descubrir que está enamorado de tu madre.','Romance','1h 54m','2024-06-27',6.25),(1001311,'https://image.tmdb.org/t/p/original//ww9s0QSZ06WIxyZAKAdg6nqfE5v.jpg','En las profundidades del Sena','La científica Sophie se ve obligada a enfrentarse a su trágico pasado para salvar París de un baño de sangre cuando un tiburón gigante aparece en el Sena.','Suspense, Terror, Acción, Misterio','1h 44m','2024-06-05',6.05),(1012201,'https://image.tmdb.org/t/p/original//gFmY2GY2X71ErIlLbO1j9MqGn4J.jpg','Haikyu!! La batalla del basurero','El encuentro entre los equipos rivales de Karasuno y Nekoma hará que la tensión aumente, ya que ambos equipos están decididos a salir victoriosos en el campeonato nacional de voleibol. Primera película del proyecto en dos partes para el final de \"Haikyu!\".','Animación, Drama','1h 25m','2024-02-16',7.42),(1020896,'https://image.tmdb.org/t/p/original//kCCew66u1HdFTOUUJmwFjQaXHkH.jpg','Descansa en paz','En un caluroso día de verano en Oslo, los muertos despiertan misteriosamente, y tres familias se ven sumidas en el caos cuando sus seres queridos fallecidos vuelven a ellos. ¿Quiénes son y qué quieren?','Terror, Drama, Misterio','1h 38m','2024-02-09',6.64),(1022789,'https://image.tmdb.org/t/p/original//2PuAY3xSvbchQWqpSiXw08Yt0NP.jpg','Del revés 2 (Inside Out 2)','Vuelve a la mente de Riley, quien acaba de convertirse en adolescente, en el momento en que la Central se enfrenta a una reforma para hacer sitio a algo completamente inesperado: ¡nuevas Emociones! Alegría, Tristeza, Ira, Miedo y Asco, que llevan muchos años al mando de una operación exitosa, no saben muy bien qué sentir cuando aparece Ansiedad, que además no ha llegado sola. Se ha traído a Vergüenza, Envidia y Ennui.','Animación, Familia, Aventura, Comedia','1h 37m','2024-06-11',7.74),(1025463,'https://image.tmdb.org/t/p/original//ns9Tr9fda1YuPK2k6BqwqmEOkgl.jpg','Biónicos','Dos hermanas compiten en salto de longitud en un futuro distópico en el que las prótesis robóticas han redefinido el deporte. Su rivalidad las lleva por un siniestro camino.','Ciencia ficción, Acción, Aventura','1h 50m','2024-05-28',5.55),(1026999,'https://image.tmdb.org/t/p/original//3HoBhPg6T5st6K09QfZh4lGB0hz.jpg','La academia del Sr. Kleks','En busca de su padre, que ha desaparecido, una adolescente aparentemente normal acepta asistir a una universidad mágica dirigida por un profesor excéntrico, el Sr. Kleks.','Fantasía, Aventura, Familia','2h 10m','2024-01-05',6.07),(1061474,'https://image.tmdb.org/t/p/original//cce5dHNQfETwnQaply3qsyD1ZqM.jpg','Superman','Superman aprende a equilibrar su herencia kryptoniana con su educación humana.','Ciencia ficción, Acción, Aventura','0m','2025-07-09',0.70),(1086747,'https://image.tmdb.org/t/p/original//13G0wKhucGWiERNloOicAuzQIyd.jpg','Los vigilantess','Sigue a Mina, una artista de 28 años que queda varada en un bosque en el oeste de Irlanda. Cuando Mina encuentra refugio, sin saberlo, queda atrapada junto a tres extraños que son observados y acechados por misteriosas criaturas cada noche.','Terror, Misterio, Fantasía','1h 42m','2024-06-06',6.20),(1143019,'https://image.tmdb.org/t/p/original//nDrUZE24mSB54cuHEjslMLvfFRQ.jpg','Los infalibles','Mientras una banda de ladrones lleva meses sembrando el caos en París y humillando a la policía, el Ministro del Interior quiere sangre nueva para encabezar la investigación: Alia, explosiva e ingobernable, Hugo, mejor estudiante y meticuloso.','Comedia, Acción','1h 39m','2024-06-20',5.27),(1214509,'https://image.tmdb.org/t/p/original//prSfoAdwrOBMA9kJVwMVBdi0Gxg.jpg','De naturaleza violenta','Una voraz criatura zombi se abre paso a través de un bosque aislado.','Terror, Suspense','1h 34m','2024-05-31',5.79),(1305928,'..','The Cult','Cuando una joven se muda a un pequeño pueblo de Europa, se da cuenta de que el lugar tiene algo extraño. Con el paso del tiempo, empieza a temer por su vida. Basada en hechos reales y en el libro El día que se volvió plástica.','Terror','1h 30m','2024-06-01',0.00);
/*!40000 ALTER TABLE `peliculas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salas`
--

DROP TABLE IF EXISTS `salas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `filas` int DEFAULT NULL,
  `columnas` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salas`
--

LOCK TABLES `salas` WRITE;
/*!40000 ALTER TABLE `salas` DISABLE KEYS */;
INSERT INTO `salas` VALUES (1,'Sala 1',9,10),(2,'Sala 2',5,4),(3,'Sala 3 (VIP)',5,5),(4,'Sala 4 (Premium)',10,10),(5,'Sala 5',5,4),(7,'Sala 7',3,3),(8,'Sala 8 (Premium)',10,10),(11,'Sala 11',10,10),(12,'Sala 12 (VIP)',5,5),(13,'Sala 13 (Premium)',10,10),(14,'Sala 14',8,8),(15,'Sala 15 (VIP)',6,6),(16,'Sala 16 (Premium)',10,10),(17,'Sala 17',8,8),(18,'Sala 18 (VIP)',5,5),(19,'Sala 19 (Premium)',10,10),(20,'Sala 20',8,8),(21,'Sala 21 (VIP)',6,6),(22,'Sala 22 (Premium)',10,10),(23,'Sala 23',10,10),(24,'Sala 24 (VIP)',5,5),(25,'Sala 25 (Premium)',4,4),(26,'Sala 28',8,8),(36,'Sala 27',8,8),(37,'Sala 29',8,8),(38,'Sala 45 (Premium)',10,10);
/*!40000 ALTER TABLE `salas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `contrasena` varchar(100) NOT NULL,
  `tipo_usuario` enum('admin','cliente') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario` (`usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Bryan','Menoscal','SteveSant','bryan123','admin'),(26,'Naomi','Parraga','Saori','sao123','cliente'),(27,'Luis','Velez','Luis16','lui123','cliente'),(28,'Naomi','Parraga','Naomi','nao123','cliente'),(31,'Bryan','Menoscal','Bryan26','bryan123','cliente'),(32,'Bryan','Menoscal','steven123','11','cliente');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'cinema'
--

--
-- Dumping routines for database 'cinema'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-18 11:29:37
