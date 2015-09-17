-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: maze
-- ------------------------------------------------------
-- Server version	5.5.44-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `etable`
--

DROP TABLE IF EXISTS `etable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `etable` (
  `row1` int(11) DEFAULT NULL,
  `row2` int(11) DEFAULT NULL,
  `row3` int(11) DEFAULT NULL,
  `row4` int(11) DEFAULT NULL,
  `dest` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `etable`
--

LOCK TABLES `etable` WRITE;
/*!40000 ALTER TABLE `etable` DISABLE KEYS */;
INSERT INTO `etable` VALUES (0,14,14,14,33),(0,0,14,14,33);
/*!40000 ALTER TABLE `etable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `level1`
--

DROP TABLE IF EXISTS `level1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `level1` (
  `mazeno` int(11) DEFAULT NULL,
  `row1` int(11) DEFAULT NULL,
  `row2` int(11) DEFAULT NULL,
  `row3` int(11) DEFAULT NULL,
  `row4` int(11) DEFAULT NULL,
  `dest` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `level1`
--

LOCK TABLES `level1` WRITE;
/*!40000 ALTER TABLE `level1` DISABLE KEYS */;
INSERT INTO `level1` VALUES (1,7,0,9,8,33),(2,0,9,10,9,33),(3,4,3,11,0,23);
/*!40000 ALTER TABLE `level1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `level2`
--

DROP TABLE IF EXISTS `level2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `level2` (
  `mazeno` int(11) DEFAULT NULL,
  `row1` int(11) DEFAULT NULL,
  `row2` int(11) DEFAULT NULL,
  `row3` int(11) DEFAULT NULL,
  `row4` int(11) DEFAULT NULL,
  `row5` int(11) DEFAULT NULL,
  `row6` int(11) DEFAULT NULL,
  `dest` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `level2`
--

LOCK TABLES `level2` WRITE;
/*!40000 ALTER TABLE `level2` DISABLE KEYS */;
INSERT INTO `level2` VALUES (1,8,34,40,59,59,57,55),(2,4,16,18,4,42,17,55),(3,1,49,5,25,17,17,52);
/*!40000 ALTER TABLE `level2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-17 17:08:02
