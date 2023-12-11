-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mychatting
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add users',1,'add_users'),(2,'Can change users',1,'change_users'),(3,'Can delete users',1,'delete_users'),(4,'Can view users',1,'view_users'),(5,'Can add log entry',2,'add_logentry'),(6,'Can change log entry',2,'change_logentry'),(7,'Can delete log entry',2,'delete_logentry'),(8,'Can view log entry',2,'view_logentry'),(9,'Can add permission',3,'add_permission'),(10,'Can change permission',3,'change_permission'),(11,'Can delete permission',3,'delete_permission'),(12,'Can view permission',3,'view_permission'),(13,'Can add group',4,'add_group'),(14,'Can change group',4,'change_group'),(15,'Can delete group',4,'delete_group'),(16,'Can view group',4,'view_group'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add messages',7,'add_messages'),(26,'Can change messages',7,'change_messages'),(27,'Can delete messages',7,'delete_messages'),(28,'Can view messages',7,'view_messages'),(29,'Can add notifications',8,'add_notifications'),(30,'Can change notifications',8,'change_notifications'),(31,'Can delete notifications',8,'delete_notifications'),(32,'Can view notifications',8,'view_notifications'),(33,'Can add friends',9,'add_friends'),(34,'Can change friends',9,'change_friends'),(35,'Can delete friends',9,'delete_friends'),(36,'Can view friends',9,'view_friends'),(37,'Can add conversations',10,'add_conversations'),(38,'Can change conversations',10,'change_conversations'),(39,'Can delete conversations',10,'delete_conversations'),(40,'Can view conversations',10,'view_conversations'),(41,'Can add conversation participants',11,'add_conversationparticipants'),(42,'Can change conversation participants',11,'change_conversationparticipants'),(43,'Can delete conversation participants',11,'delete_conversationparticipants'),(44,'Can view conversation participants',11,'view_conversationparticipants'),(45,'Can add notification recivers',12,'add_notificationrecivers'),(46,'Can change notification recivers',12,'change_notificationrecivers'),(47,'Can delete notification recivers',12,'delete_notificationrecivers'),(48,'Can view notification recivers',12,'view_notificationrecivers'),(49,'Can add message recivers',13,'add_messagerecivers'),(50,'Can change message recivers',13,'change_messagerecivers'),(51,'Can delete message recivers',13,'delete_messagerecivers'),(52,'Can view message recivers',13,'view_messagerecivers'),(53,'Can add message receivers',13,'add_messagereceivers'),(54,'Can change message receivers',13,'change_messagereceivers'),(55,'Can delete message receivers',13,'delete_messagereceivers'),(56,'Can view message receivers',13,'view_messagereceivers'),(57,'Can add notification receivers',12,'add_notificationreceivers'),(58,'Can change notification receivers',12,'change_notificationreceivers'),(59,'Can delete notification receivers',12,'delete_notificationreceivers'),(60,'Can view notification receivers',12,'view_notificationreceivers');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chatting_main_page_conversationparticipants`
--

DROP TABLE IF EXISTS `chatting_main_page_conversationparticipants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chatting_main_page_conversationparticipants` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `conversation_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chatting_main_page_c_conversation_id_5781ebb2_fk_chatting_` (`conversation_id`),
  KEY `chatting_main_page_c_user_id_db2f7505_fk_login_pag` (`user_id`),
  CONSTRAINT `chatting_main_page_c_conversation_id_5781ebb2_fk_chatting_` FOREIGN KEY (`conversation_id`) REFERENCES `chatting_main_page_conversations` (`id`),
  CONSTRAINT `chatting_main_page_c_user_id_db2f7505_fk_login_pag` FOREIGN KEY (`user_id`) REFERENCES `login_page_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chatting_main_page_conversationparticipants`
--

LOCK TABLES `chatting_main_page_conversationparticipants` WRITE;
/*!40000 ALTER TABLE `chatting_main_page_conversationparticipants` DISABLE KEYS */;
INSERT INTO `chatting_main_page_conversationparticipants` VALUES (1,1,1),(2,1,2),(3,2,2),(4,2,3),(5,3,2),(6,3,5),(7,3,1),(8,4,7),(9,4,6),(10,5,5),(11,5,6),(12,6,5),(13,6,2),(14,7,2),(15,7,6),(16,8,8),(17,8,6),(21,9,2),(22,9,5),(23,9,1),(24,9,6),(25,9,2),(26,10,2),(27,10,1),(28,10,6),(29,10,2),(30,11,13),(31,11,2),(32,12,14),(33,12,3),(34,13,2),(35,13,1),(36,13,5),(37,13,6),(38,13,2),(39,14,14),(40,14,2);
/*!40000 ALTER TABLE `chatting_main_page_conversationparticipants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chatting_main_page_conversations`
--

DROP TABLE IF EXISTS `chatting_main_page_conversations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chatting_main_page_conversations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_chatbot` tinyint(1) NOT NULL,
  `last_chat_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chatting_main_page_conversations`
--

LOCK TABLES `chatting_main_page_conversations` WRITE;
/*!40000 ALTER TABLE `chatting_main_page_conversations` DISABLE KEYS */;
INSERT INTO `chatting_main_page_conversations` VALUES (1,'private',NULL,'2023-10-15 20:16:48.000000',0,'2023-11-30 15:41:29.417354'),(2,'private',NULL,'2023-11-22 15:18:08.354583',1,'2023-11-30 15:41:57.363359'),(3,'group',NULL,'2023-11-26 17:28:20.233556',0,'2023-11-29 02:31:02.950482'),(4,'private',NULL,'2023-11-26 18:29:25.527984',0,'2023-11-27 15:57:33.235023'),(5,'private',NULL,'2023-11-26 18:34:07.637735',0,'2023-11-26 19:10:41.982273'),(6,'private',NULL,'2023-11-26 18:42:34.656490',0,'2023-11-30 15:41:21.260222'),(7,'private',NULL,'2023-11-26 18:44:38.860297',0,'2023-11-26 19:13:40.024971'),(8,'private',NULL,'2023-11-26 18:54:20.372280',0,'2023-11-27 15:57:33.235023'),(9,'group',NULL,'2023-11-27 14:11:02.803081',0,'2023-11-27 15:57:33.235023'),(10,'group',NULL,'2023-11-27 14:11:48.275360',0,'2023-11-27 15:57:33.235023'),(11,'private',NULL,'2023-11-29 03:03:59.004441',0,'2023-11-29 03:06:28.489909'),(12,'private',NULL,'2023-11-30 15:37:43.467863',1,'2023-11-30 15:37:43.467863'),(13,'group',NULL,'2023-11-30 15:40:40.316855',0,'2023-11-30 15:40:40.316855'),(14,'private',NULL,'2023-11-30 15:55:46.215467',0,'2023-11-30 15:56:48.538947');
/*!40000 ALTER TABLE `chatting_main_page_conversations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chatting_main_page_friends`
--

DROP TABLE IF EXISTS `chatting_main_page_friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chatting_main_page_friends` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `friend_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chatting_main_page_f_friend_id_eaafda52_fk_login_pag` (`friend_id`),
  KEY `chatting_main_page_f_user_id_8a0a0e73_fk_login_pag` (`user_id`),
  CONSTRAINT `chatting_main_page_f_friend_id_eaafda52_fk_login_pag` FOREIGN KEY (`friend_id`) REFERENCES `login_page_users` (`id`),
  CONSTRAINT `chatting_main_page_f_user_id_8a0a0e73_fk_login_pag` FOREIGN KEY (`user_id`) REFERENCES `login_page_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chatting_main_page_friends`
--

LOCK TABLES `chatting_main_page_friends` WRITE;
/*!40000 ALTER TABLE `chatting_main_page_friends` DISABLE KEYS */;
INSERT INTO `chatting_main_page_friends` VALUES (1,2,1),(2,1,2),(3,3,1),(4,3,2),(5,3,4),(6,3,5),(7,2,5),(8,5,2),(15,3,6),(16,6,2),(17,2,6),(18,6,5),(19,5,6),(20,3,7),(21,7,6),(22,6,7),(23,3,8),(24,8,6),(25,6,8),(26,3,9),(27,3,10),(28,3,12),(29,12,2),(30,2,12),(31,3,13),(32,13,2),(33,2,13),(34,3,14),(35,2,14),(36,14,2),(37,2,14),(38,14,2);
/*!40000 ALTER TABLE `chatting_main_page_friends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chatting_main_page_messagereceivers`
--

DROP TABLE IF EXISTS `chatting_main_page_messagereceivers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chatting_main_page_messagereceivers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_read` tinyint(1) NOT NULL,
  `message_id` bigint NOT NULL,
  `receiver_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chatting_main_page_m_message_id_c0a2641d_fk_chatting_` (`message_id`),
  KEY `chatting_main_page_m_receiver_id_273f09f7_fk_login_pag` (`receiver_id`),
  CONSTRAINT `chatting_main_page_m_message_id_c0a2641d_fk_chatting_` FOREIGN KEY (`message_id`) REFERENCES `chatting_main_page_messages` (`id`),
  CONSTRAINT `chatting_main_page_m_receiver_id_273f09f7_fk_login_pag` FOREIGN KEY (`receiver_id`) REFERENCES `login_page_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chatting_main_page_messagereceivers`
--

LOCK TABLES `chatting_main_page_messagereceivers` WRITE;
/*!40000 ALTER TABLE `chatting_main_page_messagereceivers` DISABLE KEYS */;
INSERT INTO `chatting_main_page_messagereceivers` VALUES (1,1,1,2),(2,1,2,1),(3,1,3,1),(4,1,4,2),(5,1,5,1),(6,1,6,2),(7,1,7,1),(8,1,8,2),(9,1,9,2),(10,0,10,5),(11,1,10,1),(12,1,11,2),(13,1,11,1),(14,1,12,2),(15,0,13,6),(16,0,14,6),(17,0,15,5),(18,1,15,1),(19,0,16,5),(20,1,16,1),(21,0,17,5),(22,1,17,1),(23,1,18,2),(24,1,19,1),(25,1,20,1),(26,0,21,3),(27,0,23,3),(28,1,24,2),(29,0,25,3),(30,1,26,2),(31,0,27,5),(32,1,27,1),(33,1,28,2),(34,1,29,13),(35,0,30,3),(36,1,31,2),(37,1,32,1),(38,1,33,1),(39,1,34,1),(40,1,35,1),(41,1,36,1),(42,1,37,1),(43,0,38,5),(44,1,39,1),(45,0,40,3),(46,1,41,2),(47,0,42,3),(48,1,43,2),(49,0,44,3),(50,1,45,2),(51,0,46,2);
/*!40000 ALTER TABLE `chatting_main_page_messagereceivers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chatting_main_page_messages`
--

DROP TABLE IF EXISTS `chatting_main_page_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chatting_main_page_messages` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message_text` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `conversation_id` bigint NOT NULL,
  `sender_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chatting_main_page_m_conversation_id_262506ed_fk_chatting_` (`conversation_id`),
  KEY `chatting_main_page_m_sender_id_5add614e_fk_login_pag` (`sender_id`),
  CONSTRAINT `chatting_main_page_m_conversation_id_262506ed_fk_chatting_` FOREIGN KEY (`conversation_id`) REFERENCES `chatting_main_page_conversations` (`id`),
  CONSTRAINT `chatting_main_page_m_sender_id_5add614e_fk_login_pag` FOREIGN KEY (`sender_id`) REFERENCES `login_page_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chatting_main_page_messages`
--

LOCK TABLES `chatting_main_page_messages` WRITE;
/*!40000 ALTER TABLE `chatting_main_page_messages` DISABLE KEYS */;
INSERT INTO `chatting_main_page_messages` VALUES (1,'superuser가 보낸 채팅입니다.','2023-10-15 20:26:28.000000',1,1),(2,'test1user가 보낸 채팅입니다.','2023-10-15 20:27:22.000000',1,2),(3,'메시지가 DB에 잘 저장 되었는지 확인하는 중입니다.','2023-10-27 06:34:34.677751',1,2),(4,'superuser도 한 번 볼까요?','2023-10-27 06:36:13.202482',1,1),(5,'진짜 테스트 제발 가라 제발...!','2023-11-14 06:55:05.425513',1,2),(6,'나이스 양쪽에서 다 된다!!!!','2023-11-14 06:55:15.789284',1,1),(7,'새로 생성한 Table에 정상 저장되는지를 확인해봅시다!','2023-11-18 12:49:01.823701',1,2),(8,'이것도 한 번 확인해봐야죠','2023-11-18 12:52:14.623224',1,1),(9,'당신의 챗팅 친구 TED입니다. 무엇이 궁금하세요?','2023-11-22 21:48:04.434965',2,3),(10,'그룹 채팅 테스트입니다.','2023-11-26 19:03:32.929635',3,2),(11,'test1 user가 보내고 있습니다.','2023-11-26 19:07:35.701798',3,5),(12,'1대1 채팅입니다.','2023-11-26 19:08:24.289202',6,5),(13,'테스트가 많네요','2023-11-26 19:10:41.982273',5,5),(14,'마지막 테스트였으면 좋겠다','2023-11-26 19:13:40.024971',7,2),(15,'new표시 확인 중입니다.','2023-11-26 19:24:37.548536',3,2),(16,'new 표시 확인 다시 해볼게요','2023-11-26 19:25:48.654846',3,2),(17,'마지막 확인입니다.','2023-11-26 19:27:10.161328',3,2),(18,'메세지 전송합니다.','2023-11-27 09:24:46.074794',6,5),(19,'메시지 시간 테스트 중입니다.','2023-11-29 01:34:54.212100',1,2),(20,'채팅 리스트의 메시지 시간을 확인 중입니다.','2023-11-29 01:42:23.273583',1,2),(21,'김병지','2023-11-29 02:16:05.363691',2,2),(22,'1990 상무(상주 상무) 입단테스트에 합격해 2년 군생활 뒤, 1992년 울산 현대에서 데뷔하여, 1996년 K-리그 우승, 1998년 K-리그 준우승 등에 큰 공헌을 하였다. 특히, 1998년 10월 24일 포항 스틸러스와의 플레이오프 2차전에서 1:1로 맞선 후반 추가시간 프리킥 찬스에서 헤딩슛을 성공시키면서 골키퍼 최초의 필드골을 성공시키기도 했는데, 당시 실점의 책임에 대해서 포항 스틸러스 포백이 대인마크에 소홀한 탓인지, 골키퍼 김이섭의 방심이 원인이었는가에 대해서 이견이 많았다고 한다. 1998년 FIFA 월드컵 이후, 월드컵에서 김병지의 활약을 지켜본 잉글랜드 프리미어리그의 블랙번 로버스 FC, 에버턴 FC, 사우샘프턴 FC 등 여러 팀들이 김병지에게 러브콜을 보냈으나 김병지는 당시 소속팀이었던 울산 현대의 반대로 K-리그에 남게 되었다. 2001년 당시 국내 선수 중에서는 최고 이적료로 포항 스틸러스로 이적하여, 2004년 K-리그 준우승 등에 큰 공헌을 하였다. 특히, 2004년 12월 12일 수원 삼성 블루윙즈와의 챔피언 결정전 2차전에서 승부차기까지 간 끝에 3:4로 패하였는데, 당시 김병지는 5번째 키커로 나섰지만 그의 슈팅이 \'영원한 라이벌\'인 이운재에게 막히며 우승을 내주기도 하였다.','2023-11-29 02:16:06.243721',2,3),(23,'김병지','2023-11-29 02:26:06.703399',2,2),(24,'1990 상무(상주 상무) 입단테스트에 합격해 2년 군생활 뒤, 1992년 울산 현대에서 데뷔하여, 1996년 K-리그 우승, 1998년 K-리그 준우승 등에 큰 공헌을 하였다. 특히, 1998년 10월 24일 포항 스틸러스와의 플레이오프 2차전에서 1:1로 맞선 후반 추가시간 프리킥 찬스에서 헤딩슛을 성공시키면서 골키퍼 최초의 필드골을 성공시키기도 했는데, 당시 실점의 책임에 대해서 포항 스틸러스 포백이 대인마크에 소홀한 탓인지, 골키퍼 김이섭의 방심이 원인이었는가에 대해서 이견이 많았다고 한다. 1998년 FIFA 월드컵 이후, 월드컵에서 김병지의 활약을 지켜본 잉글랜드 프리미어리그의 블랙번 로버스 FC, 에버턴 FC, 사우샘프턴 FC 등 여러 팀들이 김병지에게 러브콜을 보냈으나 김병지는 당시 소속팀이었던 울산 현대의 반대로 K-리그에 남게 되었다. 2001년 당시 국내 선수 중에서는 최고 이적료로 포항 스틸러스로 이적하여, 2004년 K-리그 준우승 등에 큰 공헌을 하였다. 특히, 2004년 12월 12일 수원 삼성 블루윙즈와의 챔피언 결정전 2차전에서 승부차기까지 간 끝에 3:4로 패하였는데, 당시 김병지는 5번째 키커로 나섰지만 그의 슈팅이 \'영원한 라이벌\'인 이운재에게 막히며 우승을 내주기도 하였다.','2023-11-29 02:26:07.387342',2,3),(25,'김병지','2023-11-29 02:27:00.219021',2,2),(26,'1990 상무(상주 상무) 입단테스트에 합격해 2년 군생활 뒤, 1992년 울산 현대에서 데뷔하여, 1996년 K-리그 우승, 1998년 K-리그 준우승 등에 큰 공헌을 하였다. 특히, 1998년 10월 24일 포항 스틸러스와의 플레이오프 2차전에서 1:1로 맞선 후반 추가시간 프리킥 찬스에서 헤딩슛을 성공시키면서 골키퍼 최초의 필드골을 성공시키기도 했는데, 당시 실점의 책임에 대해서 포항 스틸러스 포백이 대인마크에 소홀한 탓인지, 골키퍼 김이섭의 방심이 원인이었는가에 대해서 이견이 많았다고 한다. 1998년 FIFA 월드컵 이후, 월드컵에서 김병지의 활약을 지켜본 잉글랜드 프리미어리그의 블랙번 로버스 FC, 에버턴 FC, 사우샘프턴 FC 등 여러 팀들이 김병지에게 러브콜을 보냈으나 김병지는 당시 소속팀이었던 울산 현대의 반대로 K-리그에 남게 되었다. 2001년 당시 국내 선수 중에서는 최고 이적료로 포항 스틸러스로 이적하여, 2004년 K-리그 준우승 등에 큰 공헌을 하였다. 특히, 2004년 12월 12일 수원 삼성 블루윙즈와의 챔피언 결정전 2차전에서 승부차기까지 간 끝에 3:4로 패하였는데, 당시 김병지는 5번째 키커로 나섰지만 그의 슈팅이 \'영원한 라이벌\'인 이운재에게 막히며 우승을 내주기도 하였다.','2023-11-29 02:27:00.991342',2,3),(27,'오늘로 마지막 테스트가 완료되었습니다.','2023-11-29 02:31:02.950482',3,2),(28,'안녕하세요? 반갑습니다!','2023-11-29 03:05:33.823663',11,13),(29,'저도 반가워요! 재밌게 놀아봐요 우리!!','2023-11-29 03:06:28.489909',11,2),(30,'김병지','2023-11-30 13:05:46.364203',2,2),(31,'1990 상무(상주 상무) 입단테스트에 합격해 2년 군생활 뒤, 1992년 울산 현대에서 데뷔하여, 1996년 K-리그 우승, 1998년 K-리그 준우승 등에 큰 공헌을 하였다. 특히, 1998년 10월 24일 포항 스틸러스와의 플레이오프 2차전에서 1:1로 맞선 후반 추가시간 프리킥 찬스에서 헤딩슛을 성공시키면서 골키퍼 최초의 필드골을 성공시키기도 했는데, 당시 실점의 책임에 대해서 포항 스틸러스 포백이 대인마크에 소홀한 탓인지, 골키퍼 김이섭의 방심이 원인이었는가에 대해서 이견이 많았다고 한다. 1998년 FIFA 월드컵 이후, 월드컵에서 김병지의 활약을 지켜본 잉글랜드 프리미어리그의 블랙번 로버스 FC, 에버턴 FC, 사우샘프턴 FC 등 여러 팀들이 김병지에게 러브콜을 보냈으나 김병지는 당시 소속팀이었던 울산 현대의 반대로 K-리그에 남게 되었다. 2001년 당시 국내 선수 중에서는 최고 이적료로 포항 스틸러스로 이적하여, 2004년 K-리그 준우승 등에 큰 공헌을 하였다. 특히, 2004년 12월 12일 수원 삼성 블루윙즈와의 챔피언 결정전 2차전에서 승부차기까지 간 끝에 3:4로 패하였는데, 당시 김병지는 5번째 키커로 나섰지만 그의 슈팅이 \'영원한 라이벌\'인 이운재에게 막히며 우승을 내주기도 하였다.','2023-11-30 13:05:47.308922',2,3),(32,'테스트 메시지를 보냅니다.','2023-11-30 14:06:48.154310',1,2),(33,'메시지가 잘 도착하나요?','2023-11-30 14:07:18.852367',1,2),(34,'진짜 마지막 테스트입니다','2023-11-30 14:11:24.818650',1,2),(35,'마지막!','2023-11-30 14:11:32.174758',1,2),(36,'안녕하세요!','2023-11-30 15:40:03.410901',1,2),(37,'안녕하세요! 어디 가셨나요?','2023-11-30 15:40:16.610222',1,2),(38,'ㅇㅇㅇㅇ','2023-11-30 15:41:21.260222',6,2),(39,'ㅇㅁㄴㅇㅁㄴㅇ','2023-11-30 15:41:29.417354',1,2),(40,'금나라','2023-11-30 15:41:40.880339',2,2),(41,'지방은 전국을 19개 로(路)로 나누고, 그 아래에 부(府)나 주(州)를 두고, 다시 그 아래에 현(縣)을 두었다. 로에는 도총관(都總管), 부에는 윤(尹), 주에는 절도사(節度使)·방어사(防禦使)·자사(刺史), 현에는 지현(知縣)을 임명해 다스렸다. 금나라는 초기에는 여진족의 관습법에 따르다가 화베이를 점령한 후 1145년에 역대 중국법을 참고해  Anchun Gurun, )은 여진족이 중국 동북지방, 몽골, 화베이 일대에 세운 왕조. 태조 아구다가 회령부에서 1115년에 건국했으며, 1153년에 해릉왕이 연경(燕京, 지금의 베이징)으로 수도를 옮겼다. 그 뒤 몽골 제국이 압박하자 1214년에 변경(汴京, 지금의 카이펑)으로 수도를 옮겼다. 이후 몽골 제국과 남송 연합군에 멸망당했다. 태조부터 말제까지 10명의 황제가 재위했다.','2023-11-30 15:41:42.565389',2,3),(42,'김병지','2023-11-30 15:41:48.089726',2,2),(43,'1990 상무(상주 상무) 입단테스트에 합격해 2년 군생활 뒤, 1992년 울산 현대에서 데뷔하여, 1996년 K-리그 우승, 1998년 K-리그 준우승 등에 큰 공헌을 하였다. 특히, 1998년 10월 24일 포항 스틸러스와의 플레이오프 2차전에서 1:1로 맞선 후반 추가시간 프리킥 찬스에서 헤딩슛을 성공시키면서 골키퍼 최초의 필드골을 성공시키기도 했는데, 당시 실점의 책임에 대해서 포항 스틸러스 포백이 대인마크에 소홀한 탓인지, 골키퍼 김이섭의 방심이 원인이었는가에 대해서 이견이 많았다고 한다. 1998년 FIFA 월드컵 이후, 월드컵에서 김병지의 활약을 지켜본 잉글랜드 프리미어리그의 블랙번 로버스 FC, 에버턴 FC, 사우샘프턴 FC 등 여러 팀들이 김병지에게 러브콜을 보냈으나 김병지는 당시 소속팀이었던 울산 현대의 반대로 K-리그에 남게 되었다. 2001년 당시 국내 선수 중에서는 최고 이적료로 포항 스틸러스로 이적하여, 2004년 K-리그 준우승 등에 큰 공헌을 하였다. 특히, 2004년 12월 12일 수원 삼성 블루윙즈와의 챔피언 결정전 2차전에서 승부차기까지 간 끝에 3:4로 패하였는데, 당시 김병지는 5번째 키커로 나섰지만 그의 슈팅이 \'영원한 라이벌\'인 이운재에게 막히며 우승을 내주기도 하였다.','2023-11-30 15:41:48.288882',2,3),(44,'독도','2023-11-30 15:41:57.363359',2,2),(45,'김영삼은 취임 직후부터 문민 정부는 광주 민중 항쟁을 계승한 정부임을 천명하고 12.12 사건과 5.17 사건에 대한 재수사를 지시했다. 1996년부터 12.12와 5.17에 대한 수사가 이루어져, 1997년 4월 17일 12·12사태와 5·18사건 및 대통령 비자금 사건 관련 대법원 선고공판에서 법원으로부터 징역 17년형, 추징금 2천 688억원의 형을 선고받았다. 1997년 12월 사면되었다. 1997년 당시 2629억원을 추징금을 선고받고 6월말까지 2286억원을 납부하였다. 2008년 당시 남은 추징금은 387억여 원이다.','2023-11-30 15:41:57.566701',2,3),(46,'안녕하세요','2023-11-30 15:56:48.538947',14,14);
/*!40000 ALTER TABLE `chatting_main_page_messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chatting_main_page_notificationreceivers`
--

DROP TABLE IF EXISTS `chatting_main_page_notificationreceivers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chatting_main_page_notificationreceivers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_conform` tinyint(1) NOT NULL,
  `notification_id` bigint NOT NULL,
  `receiver_id` bigint NOT NULL,
  `received_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chatting_main_page_n_notification_id_fc406e14_fk_chatting_` (`notification_id`),
  KEY `chatting_main_page_n_receiver_id_1fbfa615_fk_login_pag` (`receiver_id`),
  CONSTRAINT `chatting_main_page_n_notification_id_fc406e14_fk_chatting_` FOREIGN KEY (`notification_id`) REFERENCES `chatting_main_page_notifications` (`id`),
  CONSTRAINT `chatting_main_page_n_receiver_id_1fbfa615_fk_login_pag` FOREIGN KEY (`receiver_id`) REFERENCES `login_page_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chatting_main_page_notificationreceivers`
--

LOCK TABLES `chatting_main_page_notificationreceivers` WRITE;
/*!40000 ALTER TABLE `chatting_main_page_notificationreceivers` DISABLE KEYS */;
INSERT INTO `chatting_main_page_notificationreceivers` VALUES (1,1,1,2,'2023-11-28 13:50:04.281229'),(2,1,2,2,'2023-11-28 13:50:04.281229'),(3,1,3,2,'2023-11-28 13:50:04.281229'),(4,1,4,2,'2023-11-28 13:50:04.281229'),(5,1,5,2,'2023-11-28 13:50:04.281229'),(6,1,6,2,'2023-11-28 13:50:04.281229'),(7,1,7,2,'2023-11-28 13:50:04.281229'),(8,0,8,5,'2023-11-28 13:50:04.281229'),(9,1,9,2,'2023-11-28 13:50:04.281229'),(10,0,10,5,'2023-11-28 13:50:04.281229'),(11,0,11,6,'2023-11-28 13:50:04.281229'),(12,0,12,6,'2023-11-28 13:50:04.281229'),(13,0,2,12,'2023-11-28 14:51:44.916734'),(14,1,13,2,'2023-11-28 14:52:21.853990'),(15,0,2,13,'2023-11-29 02:58:51.429208'),(16,1,14,2,'2023-11-29 03:03:09.838221'),(17,1,2,14,'2023-11-30 15:36:23.500436'),(18,1,15,14,'2023-11-30 15:38:32.784982'),(19,1,16,14,'2023-11-30 15:38:54.398906');
/*!40000 ALTER TABLE `chatting_main_page_notificationreceivers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chatting_main_page_notifications`
--

DROP TABLE IF EXISTS `chatting_main_page_notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chatting_main_page_notifications` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `content` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `sender_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `chatting_main_page_n_sender_id_669ba206_fk_login_pag` (`sender_id`),
  CONSTRAINT `chatting_main_page_n_sender_id_669ba206_fk_login_pag` FOREIGN KEY (`sender_id`) REFERENCES `login_page_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chatting_main_page_notifications`
--

LOCK TABLES `chatting_main_page_notifications` WRITE;
/*!40000 ALTER TABLE `chatting_main_page_notifications` DISABLE KEYS */;
INSERT INTO `chatting_main_page_notifications` VALUES (1,'normal','MESSAGE','2023-11-07 21:56:51.000000',1),(2,'system','&#127881;가입을 축하합니다. 이제부터 채팅을 즐겨보세요!&#127881;','2023-11-07 21:57:31.000000',NULL),(3,'danger','오전 2시부터 4시까지 일시적으로 서비스가 중단됩니다.','2023-11-07 21:57:52.000000',NULL),(4,'friends','','2023-11-07 21:58:11.000000',1),(5,'group','프로젝트 A에 새로운 파일이 추가되었습니다. 이 파일은 모든 팀원이 확인해야 합니다. 각자 업무에 맞게 작업해주세요.프로젝트 A에 새로운 파일이 추가되었습니다. 이 파일은 모든 팀원이 확인해야 합니다. 각자 업무에 맞게 작업해주세요.','2023-11-07 21:58:24.000000',1),(6,'friends','','2023-11-26 17:06:31.172093',5),(7,'friends','','2023-11-26 17:09:23.668251',5),(8,'friends','','2023-11-26 17:14:21.954612',2),(9,'friends','','2023-11-26 18:23:37.960451',6),(10,'friends','','2023-11-26 18:27:30.852963',6),(11,'friends','','2023-11-26 18:29:10.483337',7),(12,'friends','','2023-11-26 18:54:06.325629',8),(13,'friends','','2023-11-28 14:52:21.844597',12),(14,'friends','','2023-11-29 03:03:09.828173',13),(15,'friends','','2023-11-30 15:38:32.782924',2),(16,'friends','','2023-11-30 15:38:54.393335',2);
/*!40000 ALTER TABLE `chatting_main_page_notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_general_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_login_page_users_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_login_page_users_id` FOREIGN KEY (`user_id`) REFERENCES `login_page_users` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'admin','logentry'),(4,'auth','group'),(3,'auth','permission'),(11,'chatting_main_page','conversationparticipants'),(10,'chatting_main_page','conversations'),(9,'chatting_main_page','friends'),(13,'chatting_main_page','messagereceivers'),(7,'chatting_main_page','messages'),(12,'chatting_main_page','notificationreceivers'),(8,'chatting_main_page','notifications'),(5,'contenttypes','contenttype'),(1,'login_page','users'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-10-13 02:05:20.542606'),(2,'contenttypes','0002_remove_content_type_name','2023-10-13 02:05:20.591606'),(3,'auth','0001_initial','2023-10-13 02:05:20.740681'),(4,'auth','0002_alter_permission_name_max_length','2023-10-13 02:05:20.775676'),(5,'auth','0003_alter_user_email_max_length','2023-10-13 02:05:20.781679'),(6,'auth','0004_alter_user_username_opts','2023-10-13 02:05:20.786676'),(7,'auth','0005_alter_user_last_login_null','2023-10-13 02:05:20.792677'),(8,'auth','0006_require_contenttypes_0002','2023-10-13 02:05:20.795676'),(9,'auth','0007_alter_validators_add_error_messages','2023-10-13 02:05:20.800675'),(10,'auth','0008_alter_user_username_max_length','2023-10-13 02:05:20.805716'),(11,'auth','0009_alter_user_last_name_max_length','2023-10-13 02:05:20.811677'),(12,'auth','0010_alter_group_name_max_length','2023-10-13 02:05:20.824677'),(13,'auth','0011_update_proxy_permissions','2023-10-13 02:05:20.830680'),(14,'auth','0012_alter_user_first_name_max_length','2023-10-13 02:05:20.837680'),(15,'login_page','0001_initial','2023-10-13 02:05:21.012676'),(16,'admin','0001_initial','2023-10-13 02:05:21.092675'),(17,'admin','0002_logentry_remove_auto_add','2023-10-13 02:05:21.099711'),(18,'admin','0003_logentry_add_action_flag_choices','2023-10-13 02:05:21.106676'),(19,'sessions','0001_initial','2023-10-13 02:05:21.132678'),(20,'login_page','0002_remove_users_username_users_name_and_more','2023-10-15 09:04:05.936129'),(21,'login_page','0003_remove_users_last_login','2023-10-15 09:08:11.237239'),(22,'login_page','0004_remove_users_is_active','2023-10-15 09:09:47.690910'),(23,'login_page','0005_alter_users_profile_picture','2023-10-15 09:14:50.313306'),(24,'login_page','0006_users_is_active','2023-10-15 10:25:00.992754'),(25,'chatting_main_page','0001_initial','2023-10-15 10:51:11.171094'),(26,'login_page','0007_users_status_message','2023-10-15 12:23:32.882319'),(27,'chatting_main_page','0002_conversations_is_chatbot','2023-10-28 08:48:43.364982'),(28,'chatting_main_page','0003_alter_notifications_type','2023-11-07 12:32:45.247581'),(29,'login_page','0008_users_is_online_alter_users_status','2023-11-08 00:03:17.935834'),(30,'login_page','0009_alter_users_name','2023-11-13 01:27:35.800770'),(31,'login_page','0010_alter_users_status','2023-11-14 02:52:03.010605'),(32,'chatting_main_page','0004_remove_notifications_user_notificationrecivers_and_more','2023-11-18 11:39:22.461170'),(33,'chatting_main_page','0005_rename_messagerecivers_messagereceivers_and_more','2023-11-18 11:43:54.511154'),(34,'chatting_main_page','0006_conversations_last_chat_at','2023-11-27 15:57:33.304025'),(35,'chatting_main_page','0007_notificationreceivers_received_at','2023-11-28 13:50:04.350229');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('06o8jv53yp5tvx7t510ejx6nvaszo1pk','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4wIe:CQg-cUbNsEjhhhSdM8d8n0-n4n-f7SiTh3bjpJ7I3N4','2023-12-04 04:54:20.827678'),('18ntmna9wswl0wcx4wkyfdu8b3twyi91','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r0cTc:2x2uOvnuP2VLdb1KfU_q8uFISmdx_c_J0fw5KTjvpwA','2023-11-22 06:55:48.670016'),('1itlgafaazgc2fpln85t6c44112fxfb7','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5euI:f10mvg-83HhHLr7zuwSVK8oZUe6QcG84eVLWMsaqjU0','2023-12-06 13:32:10.522669'),('1ysv6ojy60d5dxtch2v0utcgi0l8qdxv','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r61ZO:ELT1KqasdjCkNqMBxBGlMLtydJXZao91Id1f17wgufY','2023-12-07 13:44:06.118178'),('21z61xkbztii9f07zwi6pd41bzs3tq16','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qwfCe:o9tUP2iWQdqKkcdcnngJ-byeaxqc5YWTkr94oT2I0Ms','2023-11-11 09:01:56.460990'),('241d06zaieatscycsmox4p0lz4rfzcma','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2jny:AHfknw-FLobMEwy4Yk_2RObAaKKsiQXBTZY2vHdkeV4','2023-11-28 03:09:34.629485'),('25m678k6zhxqkx56qg34tlxtjpkmcjt0','.eJxVjDtuwzAQRO-ytSFI1CeUqsBFupyBWHJ3JSYSCZBUYRi5e0TAjasB5s28JzhO3iTO515ggS_0O9yAj5oL2N3nwmmN9vG51q5x8bj4dSpevMPiYzDhPCwnWMa-1d3HDQyeZTNn5mQ8XRYFb51F98uhAvrBsMbLGUrytqmT5kVz8x2J9_tr-ybYMG9Vq7TVSgSlYxGhyTlqhQY90NTyOPesaeyU9P3Q4awmnFvHetIkitSoGP7-AfHQVS0:1r7r1R:Sjnm6JVfxwHHLx2ov_pE8YAve8NSyJND-SFxTMmB6wM','2023-12-12 14:52:37.915526'),('2b8kwifq1pz4oa2554ye3268g5tlfnjr','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qtIEW:qtmDLM8xpkROEM9h5jfcCdcDjLzmuFrir4Jrh9uqOso','2023-11-02 01:53:56.824423'),('2ek422p1dt02ey3sm2rmpr8j6fu6s96g','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qwA0E:TmxF3oPjqnXxm1g44wzsSJVVDSm7ut0jVqpU2r1U4ds','2023-11-09 23:43:02.936810'),('2iybf77dk5bbqv4d416pnhrnu14wvb36','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3sp6:azL_NADnOmHhW0bXX-slcTLTy-TEt_c0xdXUYuNKOW0','2023-12-01 06:59:28.394876'),('2pf0iy3pbwunuab3uqkcf13oazh1nk8i','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4eAo:y95Qs_fZSpQe1Y5aFsFUB_hYoMUBpwzlZrVWOqkrjJw','2023-12-03 09:33:02.818176'),('3ik6i5vk2rw8lhtr7evjsyza6lm5r5p4','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5GFc:gQVFTt-S9VE5fX3gxLKr5Z5P2ErOFtFAlh7M4Nt7sIw','2023-12-05 11:12:32.861758'),('3u1ki6npsjwb2kpfo5i8zimhalnud2ot','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1qtgqM:k-mZxwJTsMWHixqlPele6xTZ9z1B7gd3Dw38DE_BrGI','2023-11-03 04:10:38.727548'),('3u3qpnkvl40x3hqfpfhbq3gih1r41n9w','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3m17:L1TuAVXsbX6gM2fnki1ZnHd8DjL5A2FM955j3r6_7hU','2023-11-30 23:43:25.850378'),('3ux8vnrd66ygzka7zo4aia11r7egrisp','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r2n3N:w5T_4kagvwXS_ZDxqeMjHAG1MYNphPm9njqIxvhvJxE','2023-11-28 06:37:41.897952'),('3y1ko8xyigw5t188nnd4hmfmxgpnv25e','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r28AE:hjajKZckVgdvoFfAVZt17Ny-el9Q_R3SW3Mu9mUfnNY','2023-11-26 10:58:02.926346'),('42gmsxw8o07s3v3q7upf5ujruszo5kru','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4eAP:7WJwjfc4KjG4xzFf9tPrOGWD4ryNtjAjqqNWVXRSiR0','2023-12-03 09:32:37.194128'),('4m5q8ek9wxk1nnw1bwv3u2dgxgo1q4gi','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r5HJj:SJkl44qN9wPuPXuZAbNWCUWJ5MZ8lRivvN8zUhme9c8','2023-12-05 12:20:51.280668'),('4tzv34m172k5teeacvhv3ie0u6k0gsrs','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5FZI:HRfa61DAAsWsXuqDGZk-MY_lBBgwsF2hqY71_UykbH0','2023-12-05 10:28:48.655996'),('55d1yp66o79luegee7g0uz54mx99l7hv','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r36AM:3VY6nDRsL0v_9ClAR9msIGUUfYPLvzQztQaDD14AxRM','2023-11-29 03:02:10.756217'),('5cgisybhdast01lecvznsht7s7cm25vs','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r503A:XzqIMWinfXFGxwrClhkU5Jtu6S7B961d2hRM7e85ANA','2023-12-04 08:54:36.520105'),('5fm9u4cbr0sip5g9c3dxgogyw3aw6z12','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r5bFq:MOlE1HJo25xNlmUhsnWQ8aRW5340FBTm8nhj8IR_jtM','2023-12-06 09:38:10.059798'),('5xyc5ogyc3um1vsjew18o1dcn379l8k4','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r2mQo:YlgZeh2UiOeip_01IY6ihE7kwKoju1e0uM7PA5Cj6zA','2023-11-28 05:57:50.502478'),('61s3pvt13rf0o5xf6z10x33n1pp3ezgp','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qxcNv:1eIfY2t77NqS69IKEdG3j8fUV0U3oqEMyIlfdiqPoW8','2023-11-14 00:13:31.224210'),('6as262n95o0rv18ojiu9623c9awn92no','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3nXw:fhPM3JdT1lAueHVZm7cmlbs3kAUaNfuJT7hrXa1nT7c','2023-12-01 01:21:24.882561'),('6bod5buwflo7ztq1ogbhz1066k4ggmmu','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qwel4:IsPFvd2Is92TUshKmUpE-JaWw2gz9FrkJqjrcYNrSEE','2023-11-11 08:33:26.180696'),('6no164u0coc0ptu7i7cj2gdpvib2cqk9','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r5apq:WoY9JjWxSM6E8IEX1ToOVfhXmKOsWA4yegCyXnWaM3Y','2023-12-06 09:11:18.707308'),('6vy6c2obm2w7old89fmqsm00fa49u4lz','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qu8IU:5olPDAkGPd926pQ5pPtug5kvpotD3FBWaT-quwV_fPY','2023-11-04 09:29:30.285664'),('6yx86a7ylbh8z88f0f2cz4t9iotdshzg','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5HA6:tQPL6mP3HydPbOSkvPwrJ1a6fFq1U2QTf2aMcinT6xs','2023-12-05 12:10:54.922779'),('764hsyc0ga43m4dzgq1s5xett41upvrh','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r1mM6:0Ylw8vEFf_c7sE4oR-7eRsHTeJqSZ79Cuyos08B_9nE','2023-11-25 11:40:50.845808'),('7dabp0aga9tzawglt8iaa0rtc9lp1olw','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qv5Cp:9Kr4hACGdrivllLt1Pj_KdiHOhHOcLTpmWaf8V2-eTU','2023-11-07 00:23:35.827254'),('7ia44l9sifd1pjr89qm7j0i4tdqlqkma','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qztGw:sroWZL0lqhgtMQyop56extkXp7MFe8WXy0qnwAp0Kx4','2023-11-20 06:39:42.973080'),('7j5t5twqmgae15oj18x0e6nmri2b7o07','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1qwG7U:Xcie6WJGMftpSj_B4C9YkNvgclQUCcOZsuHTTVGJ_Ic','2023-11-10 06:14:56.915816'),('7kvgsnirdslq27bzbwl21hdshbab1o4j','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r5GJ0:j8Js0_EBLO01nPCInmJNAdkOMLnk3DJPxL8QLOJZeNk','2023-12-05 11:16:02.748518'),('7nlvwjzblklqtikmq6f5op0jsq6galkt','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qtclT:qGX9MB2eriupyKDljePvi0kHV_cHrftwN8C_T-CMmK4','2023-11-02 23:49:19.913929'),('7r2s77pl91eqefk78cz9bw6xztd0mz47','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qv6tC:M7m0SjJxYj3-E6NQmsoV4GYsmBG3Q2yjIKEkQdjRVFw','2023-11-07 02:11:26.378086'),('7uxyurpq1gdjdyjkadguhqsrlkrkwkzn','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r3spI:FeZflYsMrhYdYdZyt-7wN2Q2mTXHR71GHndcb8jNEt4','2023-12-01 06:59:40.615717'),('8ea8wocto4qpb3r6uwz070f6pd2rt751','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2idA:57kKILzP-oce7k5giq_vKTz9GT1nVX17Sjy22CzM7gg','2023-11-28 01:54:20.775193'),('8iby5p1uh7ko1f0v3u01pfwcdn84s30v','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1qwGRO:qTq1OJy6epv3Fr2AsBXtnMZMOXv55Hp8U-Wjk3E_Uj0','2023-11-10 06:35:30.090439'),('8pz441n9hr7rsup933gee9ffa7tr1og7','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4Kgb:6_aV2keU3fY6aAwQs6YdYegOkDUZzwqUW9U2ex9Fx0Y','2023-12-02 12:44:33.860073'),('8rxcdugu8qrosyam2vsot1jpu3jqaq8r','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3S4m:E5-vV__4GSHRc0nJXl3k1UnzDDPI8-fl3qlsOX9daBc','2023-11-30 02:25:52.387736'),('8s4rv54cdcy9ilb1gcralvyx0bvh9mo9','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r4I9j:EFsZiWy_TAegE7tcO7rnKwNmgK3_nNuH8nE2zTL9fgk','2023-12-02 10:02:27.779398'),('8ssfh5ohhzxp5oeu4bkvn68mwsvpe6i6','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5GIj:jBXVPMP_ilkG4Lubbk5PePIg8K8Lhd-me2xEp4ttWLw','2023-12-05 11:15:45.268820'),('8t9nabypde8sf2sev3pbdjro8hlx03ca','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r32W5:qqCpEfWC1GeJFuFliI9CQVtvRbqqOffDiK61HGFssIg','2023-11-28 23:08:21.501486'),('97yctvjmdq0np0d5bifd716grd6rnjny','.eJxVjDFuhTAQRO-y9ReCBSxDFaVIlzNYtncXnIAt2aaIotw9WPrNr0aaN_N-wXMOJnO5jgorfNhwwAP4bLmCO0KpnLfkft621nU-nTe_TzVI8LaGFE28TscZVlT9oMYHGHvV3VyFswl0WxBeOmf9N8cG6MvGLd3OWHNwXZt0T1q6z0R8vD-3L4Ldlr1pUTuNIlYGFhFS3lMvNOmJVM_zMrKmeUAZx2mwCyq79J610iRIOCPD3z_tvFUn:1r0bqS:SHfusg9A4Kd_B7XHHCvzplKQnNLQiclQA9S0UUjfWxE','2023-11-22 06:15:20.739231'),('9dwjxljelssa2fr0hbaawbt1ygtuvooq','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4vol:SvR40HYbpnvDPAVhos509--Oy0LesrCVWvpyTfaCbM4','2023-12-04 04:23:27.370223'),('9ezltm9y85zcb9s1p82bboyjhix4yew8','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4KMR:8dbIK6FXtYK8-8SasOcIcx3-7v0Zta2_RGRk8ZKLx8w','2023-12-02 12:23:43.350503'),('9vniknvz5n0h9sezqwtyvil7q450eqv8','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r33TC:xxTdYoJMemJxi48RP1NjnFML0Y2gbtfihlk6-s5ljQc','2023-11-29 00:09:26.828603'),('a7hxbrqkw2o07dqtp6wl8ll4m5537942','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3sjc:YXDEgs1GQ9YndErw1t-tVqttxmG9-YUwYjRWXoM1AGM','2023-12-01 06:53:48.077387'),('ai7gzfwngx2vdl5igl7q80k4x9s2yf3h','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r5PJO:s9S7Uhi9IUeBJQeA9jd8eUmdHQK_HPB6yElsom3ZezQ','2023-12-05 20:53:02.375800'),('aiqpjrjdxk3syjnv5787gr0c93v0t816','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3tKE:J5wubCjO_14Mo59kD8LMY4XXt01VNphL6gmDvbybPbE','2023-12-01 07:31:38.418842'),('alci3pjfyvopr8gy3tzvgm9gbky14c6d','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qtI7L:LcAOCf4EOCX77tNBf0g7D9RyIJmq02D46qae-4nmejU','2023-11-02 01:46:31.115523'),('aus6i9jltqrvhtzkuoruchx6vz4kdhhf','.eJxVjDkOwjAUBe_iGllOvo0dSnrOEP3NJIBsKUuFuDuJlALaNzPvbXpcl6FfZ536UczFNN6cfkdCfmrZiTyw3KvlWpZpJLsr9qCzvVXR1_Vw_w4GnIetxiAeIrSBnGMmF4mzixlAUxZM1HntEiFAitI2gR2ryjk0ynFTMJvPFxtTOPE:1r8awz:6pKxFENKIB4Rz36WLOYvSEV-WZXAxDt8_4LPBsxNdPU','2023-12-14 15:55:05.179016'),('b38muh0gf8y4rt3oj15k5kmmn7b67t9x','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2mQw:UP51dCIfGjcttcFwx5746EWSKUcxGaBrcMfoeDyPAZk','2023-11-28 05:57:58.525185'),('bm862ad554mg3li47uydq4eahxlea2lx','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1quAk0:vp02sk8xqtHq7MFBsnwuBQ4JFaUG1cvgExmahhEgUXg','2023-11-04 12:06:04.647990'),('bmrhs4eadyl4wrnkng2ykqearpz49yto','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r2QzK:GKResVF8qSvIQXgsNOl5K6op27UUD2P2kxCIeArhRIQ','2023-11-27 07:04:02.395187'),('bola8fgdwoksan3nmr57wlnnc1nedqd5','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4IZC:iEwWNuoUtuS6UoMtYtWvxLRnv2ppCtqyVKT7LQWeA44','2023-12-02 10:28:46.788998'),('buc496t0qx6d19nlay7f9k6u3xn1sxh0','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1quBrv:RJ4O9Cvf_AT7a7nBY3_dmuQDy_uT_ibNVaTwKjJMwM0','2023-11-04 13:18:19.648908'),('bwxzoinzh2y31j0ckaphke7vcl2v50by','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5wg1:VaJO9fiizTNzLL8oYlLOCJRpP3Bqrwp5x3s0W5-X-eA','2023-12-07 08:30:37.797059'),('c08c3g13kucah9qxeuq92t48uq62hlen','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r1kmn:05RLGQNUIHjo6G_WDRdN_iV0LhJtrCL7qdgYOJGU2Gg','2023-11-25 10:00:17.336164'),('caett1moxn71lrq6o6nzjy288qwb2k69','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4zmP:TtwzRjoBbb1WN7QK6uKyLy_dB8tcKHpSfTanpuFzdp4','2023-12-04 08:37:17.965617'),('cbl10xphxgm7ga9nvee4iua91xyxamck','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r0caF:vFaYVSKE_GCdBbVRkh8YprYiwdK3gH-r1IYYmHue8y4','2023-11-22 07:02:39.597424'),('chgdmq0hrwix82kfxf42u6lnk6i6035f','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2s5P:Xl0A6BFjthZ4tnlZe75Z0tisoCd_sFfV2TchCe8oofI','2023-11-28 12:00:07.985342'),('coujkvj48ou0hb4j17lnhown70blnu2j','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r1nqw:njE_pxgc-CaenMi403sNo9Q86zLMhSpMougSB4VMsa8','2023-11-25 13:16:46.051915'),('dgdg79isb2o9bq1y0qtc9fbxmt9ppd4y','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qxFKY:_GQyTY5lY4SWuVJFgmWtUR-6V3-kCsgP1lX0sWuG3BM','2023-11-12 23:36:30.562946'),('dgdqsqc163x6xdhiw7zr3n941pkjb5rq','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2mw9:atZi_XRhy_i7rRoyaz69PzGPitQIkfCb8Hs6HI7Ybvc','2023-11-28 06:30:13.556515'),('dq3vmjljejtmxbmztin11smijnlwx7z3','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qv6mf:MucOUXSkyoi8R6kt-Cy-LHJ77raZA7y0O36uULqcE0Y','2023-11-07 02:04:41.530719'),('dtfn80e8tawerbzjwmv2dt7ng5t0ryrk','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qwDpq:GoUhBTcouDclLwvoey35CoWp7ZLq1Si4fTJFMq8po34','2023-11-10 03:48:34.887270'),('dz52cnli8ca86s6pohcrvivs6lv5xsyt','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5GUL:pKAA3XHUebG-Lpvow_8drkul-GKmcm9722eHXg3HQEs','2023-12-05 11:27:45.020723'),('eugnq728e2rq4ofuoutrxnfgawbwguvv','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5alx:KjM9Go6iPP0ieOQUFq99J3w5i_2rRcAUynGi6Wy_V-Q','2023-12-06 09:07:17.307598'),('evx5nrscz8p271oj3tnu8w7rbu0yx2xc','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r0Xxq:4B001R-xC0xtNh84qhT72ZMi468pW6KYs3m33m6lr5I','2023-11-22 02:06:42.760150'),('exwijd4vs4oh525pvz86zwd47yqzajfu','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5oE5:0xBJNjtbktHga0sm4SioBAjZ9Hzq3zAo1nRRT_p1vbM','2023-12-06 23:29:13.088318'),('ezkt165yi4z640p16k0h8rko3aga030a','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1qv6YL:6mFn2XZpPDKqw6meOfBq1niT6CMjBkfyJemnatDKd8o','2023-11-07 01:49:53.470842'),('f1phpkow97r3qgzjddzhnu825fe1oy40','.eJxVjUFuwyAQRe_COrIMNhb2quoim6pnQAMz2DQ2VIAbRVXvXpCyyWqk__5_88ssJa8T5XMvbGFX8Du7MDraXZjZfS6U1mgeb2vLOhuPyuuoeOctFB-DDudhKLGFCyW5urBvyPkeE1YB50Le6McH_VFnGs6y6TNT0r5R8ZoZsDcKDeAXhDXWZ6Ekb7pW6Z40d58RaX9_dl8EG-StaYUySjgHjpNzDidrsXc4qhGnnuQ8kELJhRuGkcMsJph7S2pS6AQKKYj9_QN65F0f:1qvXh5:yqobACJKAmbsjzOdSCB-JrvkGjHDYbYjWxEZ3ZnWpQ8','2023-11-08 06:48:43.792649'),('f1xxqezeis9s48zuc1mlfgaj5x9aq5af','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5d3M:LoNq6Czq12kDvrk5ovOlZcnOuxBMdP9gbaqufjt0fU8','2023-12-06 11:33:24.084332'),('f5b9jy4auk6fm514af9vuis16lql1z9j','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5OQS:Ls4jBt1n9j0M_24L4Il22wVAIC4XRN6scYtYbqkvIpg','2023-12-05 19:56:16.684772'),('f9s0aibh4ou33l8n8yu12rbw1skhkmuc','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r1oFq:aAVsKad6fCGpv68f0LNe6BmDr4BWeHqz-LTb8ipwWeg','2023-11-25 13:42:30.621331'),('g28iljcpowlm4t353yk1h8a5861yqvg2','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r3sjT:5NWHU_lfnmFB0ob3EuEXOiQhIBa_CjFxzhpTf5pgh64','2023-12-01 06:53:39.246646'),('g6ejc2n3ihtf0oq2sxzdj4u0494ckhxc','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2Q89:6Nr3WFiLoOdCF76N6XOvV1oKL-2Wl3px0S9svxhJf68','2023-11-27 06:09:05.930631'),('g8glm0yzvejbe20b7716mee7iika72w6','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r4IY6:WzIX-gx3kcFxgBst6MMcQEPindndS8aP_4gB-53C630','2023-12-02 10:27:38.461438'),('g9ifykl2axnkpao5fhllb5u6kfv9sl6f','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qwjDE:uxXC5vXCY9ym0mOtqsXGFeIpcWLXFXledgN5Tu8q3-k','2023-11-11 13:18:48.639447'),('ge2vdg2hoe4wkxwnutnsgohovleqkfcv','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4I9q:0UCe1V1Ix1gJVA-mQMCn71FVrZyqh0ZegqB3QT4UttQ','2023-12-02 10:02:34.897881'),('gwj711g6u50ra1mbnhhy9lfgy6p4kvuf','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r5GUR:-Vmq6iUGlTGMeGbKbwjunPUuxj30jxKm3XSj9Qul-GQ','2023-12-05 11:27:51.100815'),('gwsg8m8cd02qozolbk2l5psa902m21tk','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r0cV6:T9luZNBwUaGDJKMO6UcU3RoL4yotZsQtZwLlkU-Gtrs','2023-11-22 06:57:20.596906'),('h8iw2ajsvpl21zctkvll3kuf5l0sf106','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5GGr:tLJk4w2EO1BqTcrIInQ8Mlso5Ku72WZuiZkOxTmi-_E','2023-12-05 11:13:49.086923'),('haux7j3hkthrnrlkszbwhky0htyu5y0l','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3S1l:ZeEWQr_4TYOIqDablggHY000YS66vIpheHaX9mnRo9M','2023-11-30 02:22:45.752811'),('hultmpfpj274e8ra7m80ge5ge8qlkic4','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1qtiJ4:nCVALEZmDIfgyP3p2VevbIlGuBWwCqJnAzEsSQjHGBc','2023-11-03 05:44:22.821549'),('hvzdnh9wnh5kf1uv7doinxwaw75a8hdh','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4dIi:b-VWtoIRnpqBs4OTFqgLwpluc9J8bLlPkkGZiZYo6pw','2023-12-03 08:37:08.610939'),('hywsazjdjhm4qyv272gu9kdute2ikmp2','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3tnd:Tmk2nL4NUhDf4CF9mXdVQR3dl-GaLMKOxPSMXANyGvI','2023-12-01 08:02:01.360438'),('ie65jp6840s8wzp6sjlp9gvjb4lsdlcj','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r0ckq:zERAVAvXl3klrZZjp51NILLxPM4XdtdYEw7ehcHn81k','2023-11-22 07:13:36.036751'),('ilgmryjjainn45t9rrrrej0422xd0ts9','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r5akY:3R_jawFjTnNRWMWzqP92nJR3fswTCD1HWAoSuFJVD7o','2023-12-06 09:05:50.996736'),('imcnjhjx8fldxtv69gele10dmhlitc0h','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qv6ww:66t2s9WBehQtUoXaV_MPqkLxujz1jBdmil4MoTLqseM','2023-11-07 02:15:18.870033'),('ixf46ovc8m53cd9s2u8vasojh37oaphu','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r4J0j:yoDFBhw92cR0aqGgAu3ca2jF4dXhDOs1oqG9yI2X13M','2023-12-02 10:57:13.041081'),('j69m4qc9m9zuvvt0patfumg59e39nw7r','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qyKtR:WMg8W9wTFU9js9GFIgCPXjgCsIYqUKzjHpC6SeNAQnM','2023-11-15 23:45:01.080986'),('jb56g4892lj6neq560lig3xuvnt16rpp','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r1F1w:agVnDSQ-5BtmwPJFaId5laJPZj96cZoy8MFHP28vIdY','2023-11-24 00:05:48.460022'),('jbtxp7mka1xo7p5jxewg5umbv5w9ym7s','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1quUEa:V0oTY_za9UKhYifoRFG14U3T7LdWSApLvuOCZLtmrzk','2023-11-05 08:54:56.121524'),('jctuuwovoq3htkrp4xov7vc5kkd7xswb','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r0cGb:mtDZHQ8BYeYh5mx5XDwENpALVpFxtn2qEfisaq6mE3Y','2023-11-22 06:42:21.990507'),('jncwxgclyrtf26tilffu4qbu0p96wab1','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r5GCa:m13ZUs9vf9KCBfkfXDYbamnpL2mK4AHRSjC2tCZ_kFs','2023-12-05 11:09:24.370229'),('joo51ibqgvrhb6i9v4cxd9nam6qu45p5','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qtcgp:_aU3xC1uN4Lf9y7Sxr1IufG8UG0_bEoEVgV_lfZqy5I','2023-11-02 23:44:31.314272'),('jxxg7g2e8489j26ntfj1m7mjxvvtanqp','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2jlZ:Vx35liG0T69uL6j1p4s1W3LmfgcOuYwjVGfBTIvCtD0','2023-11-28 03:07:05.226288'),('k0ck60ecwgdnk3wu5m15ixn8ovhu8ce1','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qvY9E:B5lGctLs_i4Zy-MgkO3lkqKp0rmiNnJSY_IP3mtmc3Y','2023-11-08 07:17:48.830628'),('k3vww77l0o74mdy36gma4l438nqeb91x','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4eDh:dqplWNAXIVEjtiqhr6_aLOp0gI1WxbohgGkkng2s8-0','2023-12-03 09:36:01.204680'),('k774fu9ym6c3n9vo3cppg8guhc2fq49y','.eJxVjDEOwyAMAP_CXCHiBAQdO3TrG5DBdkMbJRIkU9W_t5GyZL073UdlriVWbtu0qqu6Y5nURUXc1jFujWss9MdwZgnzm-dd0Avn56LzMq-1JL0n-rBNPxbi6Xa0p8GIbdy34JMHEZSORYRczmSEBj-QM2xDz55sB9L3Q4cBHAaT2TtPAgQWWH1_Gfo_rA:1r8ay3:TUlEBtd9TvmawRXZg5LXZusUlFwpHeAssjV0zbKVbWE','2023-12-14 15:56:11.280234'),('k9jjyzfcfhy6vgu46grbst1l6rr46f2y','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r4IZl:crOU6GFhIbPziNnu5-QQwuuCka4q4A07pwTcqUelM8o','2023-12-02 10:29:21.529345'),('ke8swwekfh4g4wstmsfdfedki98dfsbd','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r0XvS:J_tzYg1HolaDGEHJoq8pXOP3VhsPKOi9jtdgE7nGDco','2023-11-22 02:04:14.111335'),('ko2718fgs39mcur5w2kwmyw961zww1lr','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2KfN:jWk9cD23KpWtN68r_JcOSUCJ2zRe5GRYOr20DeYDDYY','2023-11-27 00:19:01.831796'),('kwn22z14t66ap0ukhobwxmf849zydzut','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1qwepA:o3iSHJ_ywQTxBSAqJZMWUjo_pp7TzDkTysdJjmGp3Q0','2023-11-11 08:37:40.771042'),('l3it5o9z3ohrudj415xadlgmgoopg8zd','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4L0B:TDdVSnutzKVMHcBRvIXvfsrqAp9fDvPjRYqH8aRvXik','2023-12-02 13:04:47.010229'),('l8i9rnomyc3qmtcwf5i8x6v30tz8p0ps','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2hIr:le3Mn3idmY3bNpJ1Q04AYIqz9Lh_xDM9ASrv6NxEVmI','2023-11-28 00:29:17.307303'),('lmfop0wvarczl2c28v88r60scr4sohxp','.eJxVjDEOwyAUQ-_CXCF-Egh07JCtZ0Dw-Wloo0SCMFW9e0HKksWy_Gx_GVKKNlEu68HubHJxZTdmXTkWWzIlG0ON4Zp5hx_aGghvt712jvt2pOh5q_CTZv7cA62Ps3s5WFxe2lpA6IwUSsI49h6VJNHNszZyNmowWFUjDQKhms550HocwPdCQR80Avv9AcisPdE:1qtjfj:LbAZvcsS5PfHCxu50Uuin6xpfgj4iJ3DX6SQYaiKLz0','2023-11-03 07:11:51.986144'),('m04837tsujmxm6npsg2xudwfksu3qxp0','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5oGD:AZP3fSqnf_VAFb8eSBFGJLWV-ayinYj8DVSr20qz0ew','2023-12-06 23:31:25.092409'),('m5l1ihqq7hhpgtrrn5ajzzwugegjtk3s','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5ERk:UlwAxPBQEXoq-6eLtcOoZQPlN1lZQvRCvzq03H344nw','2023-12-05 00:16:56.987634'),('meu1vufad59mjp94n7mrojwlh9bymb80','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5FTw:gGhftj8RB7Ji29vgmkG91VYv1gpTKdZDvwgr9DNgLWk','2023-12-05 10:23:16.508935'),('moq4249r42v4saiaq1z8fn61o6dy3nrl','.eJxVjDEOgzAMRe_iuUIQIE2Yqg7deobIxHZJC0FKwlT17gWpSydLfu-_N3hOwSXO21xggBuGGU7Ay3EHKJyLtRciqvy67GC3S5DgsYQ1urgtIycYztrWRp_A4VYmt2VOLtA-V_D3G9G_OB6Anhgf696MJYWxOpTqR3N1X4nn68_9C0yYpyOrzGiUCErDIkLae6qFOtORrrm3LRvqGyVt2zVolUZbezbakChSvWL4fAHcHVHn:1r82O7:m1hANb8XOC9I-rOqhzyNDuiug06UazXYYGAH1z7n8Vo','2023-12-13 03:00:47.236046'),('mtemfxdrsk1o9niydf9g2kbx2x81kjs6','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r4Kjt:o1qSslo5v8jOlUbnqRArbusFurLrALbxIUoONw3SOaI','2023-12-02 12:47:57.802306'),('mtzouxi3zzsmrxiopvbqvz84heif3cd1','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qvq23:llCzHSGOcaFMXbokyhvW0gNpZpvNAJuCPVQZvuc90PU','2023-11-09 02:23:35.683786'),('n7kaqwgjovm40c8i860zhnvh3crez3hm','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qwDP6:k5BkIT8Q8PUP22UWhcA4rlKlxuIliXG4TzeDnmKKoU0','2023-11-10 03:20:56.894545'),('n7yv3go6kjjz9dt98ycccbc0szyaj3lw','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r2iLf:CUdLIbKuBs-IYJYAAO4CIOxePlx223MFnNioAZRXndk','2023-11-28 01:36:15.636848'),('ni78v3gwktpoq1s45p2tuwxjjmvt4c6w','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3VJ5:PyLElX_deP5TrTGkq-UMptAFHuWA_dKW22u8u7MBPzA','2023-11-30 05:52:51.767737'),('o2m950a89b4e7annvdxpkp6bh8cqplhx','eyJjZXJpX3Jlc3VsdCI6IkZhaWwiLCJlbWFpbCI6ImJsaXN0ZXJnb2J5QGdtYWlsLmNvbSIsImNlcnRpZmljYXRpb25fbnVtYmVyIjo0OTM5OTJ9:1r0biV:8eC7yovxk5mtmeI638Iy9SiasqEdH104sMaM5WOWUs4','2023-11-22 06:07:07.447468'),('o7gif9oip7dlnz2t1uetgkrxg2krvd1x','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r37qU:ef2fC4HVNCp7f2x1p67CNSQJSvfw_NikIYMKs6xbsC8','2023-11-29 04:49:46.158914'),('ojhsh8r15m3d0qmbcbusrsej4a63dg4q','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r28Cm:By427kUizdNZqlmMlm0rd2GHY9dEU6d53DCUJVa6_kc','2023-11-26 11:00:40.447832'),('oqcfg7f7snan0se95t9tuctowgwoh0p3','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5OQu:mjUyZTz3nC1vbXR_5qfNpQREvXPkE5tvObkPWsSfeLM','2023-12-05 19:56:44.204366'),('oswpe3y48hr7j9aopj4mrrmgi81bc1om','.eJxVjLuugzAQRP9l6wjB8oihilLc7n6DtXh3gxMwkm2aRPn3gJQm1UhzZs4LnERvo6RtzjDAH_kZTiDLkQNo4ofe0_MSKDEVbl12uD-yV-8o-zXYsC2jRBia6nwu8QSWtjzZLUm0nncFwk83kntIOADfKdzW3Rly9GNxTIovTcX_yjJfv9sfwURpOrRoRoOqpJWoKnfOcancmIa7Utq-FsNthVrXTUU9dtSXTkxnWJGxRYH3B7hkU-Y:1r2hFy:G6ybAFesiph7LzmWTH1m3o_NjEqCCrS5XgsuCIhQlro','2023-11-28 00:26:18.446022'),('p8ed9c4sbt08w6si0f469z8gplea6g6h','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qwf64:HDlubvRryBiwptLU-3QrjIhgKn1rElBU7CIBRB1LG_g','2023-11-11 08:55:08.062141'),('pd5qklvnt6lzb2maedm6inzeck69y5o9','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qvSCS:I6PCL_A1WxHvk5zAkzV9DAkGK-jjHh7BKb7kVo8pHBM','2023-11-08 00:56:44.922944'),('pfjzbyhtrt8wgr64nn9ytj3mbtw8ngj9','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2kxh:8gt0e_QvaXwVWZqT_42WdbFdMnNdlBd6LU5llOdqeDw','2023-11-28 04:23:41.617504'),('pgrsj8f91jn90rbh8551y3i9zbfsvujh','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r8ADM:k5R1I6KL50IOyDVXKeI_CFCVkiWRFsxRpkUejjEZDck','2023-12-13 11:22:12.424776'),('phs8x7onjah1a1vtqs4kx2wlqxczot5z','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4vvy:AP8pIIcJQLALO-4EMiEVXPRe0s46ypyw2yywStd9IGA','2023-12-04 04:30:54.902846'),('pih3dh5oh3mpm2zf6no5ho1hxshwp90d','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3VL8:8SqUBQ4BLu9Z_P2vJucYa_kI-RsGjt6Yp5gW2FXSj3g','2023-11-30 05:54:58.785947'),('pkn5pojf2exe4phj3a5z0he10vg2sr20','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3WHO:qW9gjJMMhvyUfGj1xb7mT6aNdDyTkSKG4SfMMhuVRUY','2023-11-30 06:55:10.683739'),('po5w8fx822bm4zqlcfxgdjmv1wsk1ys1','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4dkK:ezYhTduZf62WxyDZhMdiqM-EmPJH-4AOXlQErhne248','2023-12-03 09:05:40.293145'),('ppzk8t67cwoxdsne6q8p7p9fcrh1k7ua','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qv6jj:dTKw3q6w8fqKVeYmibAT4KgksBt1Mn8tcZfE1AhvXWA','2023-11-07 02:01:39.685371'),('qxkvlwh8es4mrcd78c8jn54k5kh7p39d','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qrzbw:G5kaiaVrXaPhfOPkWSKcmFrCKDoxn60Qw2Oh98dRo7w','2023-10-29 11:48:44.581666'),('r3gosnh3zpd5j4ivxp39fm4oc9kh4wdb','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qvYRq:_FVbVePEL5Yh1HKX_JxJ6S8Prnom7K-inmfZHdhVKIA','2023-11-08 07:37:02.453158'),('rfhxggyrvhwsdpuh6gpqg2pd1t52chn5','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r0whZ:Hf5MeTw_O2rK6k_M1QBlU-NCSA_c3KTejzic0xJzUHg','2023-11-23 04:31:33.093107'),('rjpefzzw9j3u4ocu1m1hf444pb0iaout','.eJxVjLGOwyAQRP9l68iysUHY1emKdPkGBOyuTWKDBLg4ne7fz0hpUo00b-b9gqccTKZy7hUWuNuwww3oaLmA20OplNfkfr7W1nU-HRe_TjVw8LaGFE08D0cZlnGSUvU3MPasmzkLZRPwsgj46Jz1L4oN4NPGNV3OWHNwXZt0b1q6R0Lav9_bD8Fmy9a0QjstmC0PxMyovMeecdITqp7kPJJGOQgex2mws1B27j1ppZEFCikI_v4B8SxVLA:1r0L2g:3lI0gLO2k2zgnGVaNCvr9HgoVi4YI5oUdcNEgSP0CFE','2023-11-21 12:18:50.591853'),('rp0joud6l8trtzento5rxetccs0gu81c','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r2Qf5:Euq_8OGgJ-Dl8VvDy-apBrsqVUWEkuc9iA75fEpSZSs','2023-11-27 06:43:07.261975'),('rppopv1v0e449ueehozk8t90x8h5xsdw','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r358S:bP9GmW1mv8bSOX5HDc7h_caf3gAKb992gP6B9g35CPA','2023-11-29 01:56:08.034188'),('rts53751sz69ulct4vrqhpj1081crts9','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2kxI:KN21c_en6AOBLJcKLsyhcG-WCoh97E7Z8zxRAr5nEx0','2023-11-28 04:23:16.257476'),('rviyx3wsunyaac7f5d7qjhfl1uu3px8i','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qtNB2:Vryr0VtBJDDxuk1-yn19X5F2-a5FPSOKCMUl0t-ssHE','2023-11-02 07:10:40.486658'),('rwrv1tt61ybbudppiquyman4ckk04gjc','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r3qyQ:k1rVCa4CTbe-FhjubLwjWirUnSInO6xxY154F1hxMM4','2023-12-01 05:00:58.810873'),('rwzsvm6nm2fcsu3ndkmupzqjekn0et5j','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5PJz:MC8ZxyMe1uYO9UwUu6nYKmj_ziL0mGuuLOOfuFnSsGY','2023-12-05 20:53:39.555302'),('s0f5qtvx6awcfmt1r9xvgsobi15h8ioh','.eJxVjDEOwyAMAP_CXCHiBAQdO3TrG5DBdkMbJRIkU9W_t5GyZL073UdlriVWbtu0qqu6Y5nURUXc1jFujWss9MdwZgnzm-dd0Avn56LzMq-1JL0n-rBNPxbi6Xa0p8GIbdy34JMHEZSORYRczmSEBj-QM2xDz55sB9L3Q4cBHAaT2TtPAgQWWH1_Gfo_rA:1qvuUr:42vjvUbAzObCGlJVLUPtx013Ftg9_aBNyGsEeJTDn_k','2023-11-09 07:09:37.783015'),('sa195ggow6aictw57sg9r1ii6q2ab2gy','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qtcaZ:XIJW-bYpdLsP7NHa85Sp6BcIRt8k7xxiXhKSfupPk_s','2023-11-02 23:38:03.246485'),('sf20wg7wo6bwh2r9igh8m9repncbudc4','eyJjZXJpX3Jlc3VsdCI6IlN1Y2Nlc3MiLCJlbWFpbCI6ImthbmdtaW5qaV9AbmF2ZXIuY29tIiwiY2VydGlmaWNhdGlvbl9udW1iZXIiOjg3NjY5N30:1r8ZWK:ayM9YiIuwHpOno8EkCZPhsSO7V-LHH10YeyZiRUy_iM','2023-12-14 14:23:28.303354'),('sk1zchfnr2yg4pzvvse6zd5wzd40dhf6','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r2mwi:ywyJbDy9MO6FT8O-Zwy-dKY0CKXw2Uq53j96-sK6fMM','2023-11-28 06:30:48.549339'),('skhzwx69y503mod7r8ugh3fgahqhy9h8','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4IWt:3kP7KbUluxKUevifJLH0p5fKu-yvPjAeeZZPXnhNxPc','2023-12-02 10:26:23.456141'),('swkaio28daskzpjd5vtowgrl8n83510i','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qwAIi:5-dxzfCwrkE-t-RSbgYJ1iLu8g704fWcRzNR5jLs9gw','2023-11-10 00:02:08.736454'),('ti45zk9y5tq3dl19p9j5f9pm4vaevbig','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2Og2:WbWi1tyKSXMce4tIBzpMhdxsDaNZzhCDWY5pwxWFZo8','2023-11-27 04:35:58.709885'),('tkd5xew2yv9g7xbq08nvvhsmtl4zefke','.eJxVjLFuxCAQRP9l65NlsE2wq-iKdPkGBOyuTWKDBLg4nfLvMdI1V400b-Y9wVMOJlM59woLfNmwww3oaLmA20OplNfkHp9r6zqfjotfpxo4eFtDiiaeh6MMy6zEh1A3MPasmzkLZRPwskh465z1vxQbwB8b13Q5Y83BdW3SvWjpvhPSfn9t3wSbLVvTSu20ZLYsiJlReY8946hHVD1N80AaJyF5GEZhZ6ns3HvSSiNLlJMk-PsH9flVMw:1r0MmY:H-pynBuzuw_JPZoydV6GWQH2rXz4krpYOnfvzIOkvbs','2023-11-21 14:10:18.101714'),('tsmuwhrc4n2xi4p4lakbfi7iisny7v1t','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r1oBz:7Dj9Fa0gkbWcTs8OIrdwmwfNPINAVgq8zSPx0VUsOx0','2023-11-25 13:38:31.905530'),('tzixmi0try5agg5vki95rwtr3vs19afh','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3Qu5:xlg3yKStqPGdUL3oZOpkBGe_6KtvBhrLFoZZY0rTOiU','2023-11-30 01:10:45.679472'),('u20nitt810lyn28z7m39jnki8184t5rf','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qtIIk:Z_FmxwT5ItJORzxytnLHu3trclGx8DOHwp7SNxQJGOw','2023-11-02 01:58:18.230761'),('u3lipk0nvar6nmca9sm297o5d0s4x1ho','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qv61n:qMNJaQrDUG3M9d1S5ECKPQnWLZShu4TeLZ7PniFWBlk','2023-11-07 01:16:15.239334'),('uavg2bih9s18kurcux3boph8p5q0fqcc','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4J0U:4l2sihy4R31JAhLRIfdVAPRj60IhsK_MBNjV4WL5KjY','2023-12-02 10:56:58.744046'),('ufrpf9fqkc86liintl3d8emba7u749t3','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1qv5xA:QgMOMmG53kYc3ZGn1XG1xSH69mGFJWbkvk9fXlw2dTA','2023-11-07 01:11:28.022231'),('ujs7llrif6p4jlsg0l3whqfbh38ifx2j','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r0VV0:kExUwJjh6LTHCYSNSzariuD077N0_SURrKQVmCDB_Xs','2023-11-21 23:28:46.176532'),('uyqfuv51khpizq0ifhziky9ademoz3j0','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2n3Z:e8ozMmfXr3-mlqWJKM1iR4-KyczBKnIkDPJPQ1W90Xs','2023-11-28 06:37:53.906626'),('v24tivqmet9fxh8f19v4zv6nuqdlxdoe','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qwEKV:SapKWrWy_sZ0ejlqFPfgBrKAN0KB0McRYo-gINEZkVU','2023-11-10 04:20:15.752397'),('v71r4e20z74cj684pf64kv1ebm3jezvu','.eJxVjL0OgzAMBt_Fc4Ug_MgwVR269RkiE9slLQQpCVPVdy9ILJ0s-e67DziJ3kZJ25xhgDv5GS4gy3EHyJIyIl6ZuXDrspNdz169o-zXYMO2jBJhKC9gacuT3ZJE63mfGvj7jeTeEg7ALwrPdc-FHP1YHEpx0lQ8Vpb5drp_gYnSdGQNjmhUSStRVe6c41K5wYa7Utq-FuS2MlrXTUW96agvnWCHrIZNawS-P92oUQk:1r882t:BRRt3Q9OPETrf69j0GOdq6PXqbTAYDoPDScpnyg65Dc','2023-12-13 09:03:15.042516'),('vt1avwwa6lvwunt6a4ouc2n7lu13aqtx','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5PHI:T5f6qvFQsourY7uQXjJZBmjoIbisGWUxCoLU8TjO71o','2023-12-05 20:50:52.773913'),('w4pveas26rvdfflmnwikbumswqva417o','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r0cgl:8AEhwCGQtwszx4iHa6rxKpcv2A8Hz4PvcJTP_7dgHik','2023-11-22 07:09:23.027682'),('w5rkm2v1jpx4fm5ixmeojxrzr54l3n8s','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r35az:PSxdEGU4_Uy6tJn0ofx24osTXf06J07nZCsqmqnqRA8','2023-11-29 02:25:37.104768'),('w6mgikj8vvbsaffg5rcjl47i1ea1pe03','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r0wgJ:SrGsATNpYVtYBF2mlGhMQXGApeu5r8Nwtw4NFq4BYzc','2023-11-23 04:30:15.515622'),('w6x88nsxo1edx35agphaldke74nt07ya','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2QAa:tUlHNxjfrcuT1G6BCmfCR-w4iCO0-1L9XvWVcKG9eFE','2023-11-27 06:11:36.736253'),('wem0tgt2yiu71gna92b64edoekpeamno','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5G4J:LnOBFI8OpAHBPU90xZqMrws3D833mOqVOu4cwTCfU2U','2023-12-05 11:00:51.567566'),('wvcdgamaqypq02tplzzuf10r0mrgt5jn','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r3VDy:mNy4B0LgWyWIIlGRIKVjPhXGO6UXQclhWOWA6V2KfJA','2023-11-30 05:47:34.350243'),('xaty1ad5q4nn3q8gvmzoyyhlst0q60jk','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qznuL:RDdd9ngqXFS4kX-91h12BULFb9u1jOzdX3fyIoaLUio','2023-11-20 00:56:01.069912'),('xh72qxj7xj8nk6gghz12rrwzijxjs9hy','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1qwGRh:Rii1tmFGNi6zRIbFIjB8rsOumFek2nHneHoRK2plg8g','2023-11-10 06:35:49.417604'),('xiejy7wppf7loch2jnjinpamg7mubng6','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r3tK5:UfjCwi0qfW-qB2jAYDIoD3fs8Wo_fJAUV5eMDOQ-KQA','2023-12-01 07:31:29.898056'),('xraou5hu9ue7fnwbqlt8sq4v2lqemmjl','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1qtcjU:exTbFu56TaNxVrxQB5Nyohpo84EeirCgdM1or-XT604','2023-11-02 23:47:16.628169'),('xtsi86y7lnhtp27sj5kep5sluj0oyp8j','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2hIr:le3Mn3idmY3bNpJ1Q04AYIqz9Lh_xDM9ASrv6NxEVmI','2023-11-28 00:29:17.261299'),('y02w0jc9mqebjo29d32jcex3xe52dhwz','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r7THZ:bbgOTiXjsEY6X2PmOiewTXqwP06E5Q8Nzze_o_E7PwY','2023-12-11 13:31:41.776100'),('y1x3k2mfbiulli6bjnbocyfulzoz3mc3','.eJxVjD0OwyAUg-_CXCEe4bdj95wBwQNK2gqkkExV794gZWgXy_Jn-02c37fi9p5Wt0RyJUAuv1nw-Ex1gPjw9d4otrqtS6CjQk_a6dxiet3O7t9B8b2MNYPIrWRKgtZTQCUT4zkbK7NVwuKhBpNgCIfhPoAxWkCYmIIpGgTy-QK-cTbG:1r3tnX:wFBRDcjohY3dhVr8T8jwsfDEkzbbNh1cohyCOSPyN-g','2023-12-01 08:01:55.273927'),('y9i6vzj2gnojyv2aygve0jkupap3hk6n','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r4LeN:tLFvgoHWtDK--_IYGFQKnT9qpECRBWBye4uVmFzTezY','2023-12-02 13:46:19.916300'),('ya18mrzjk2skcabce1uu11ip2wa2gydo','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2hLf:z9arH_zVzlDDsmJ0ENlJHmIZ1AFZJ0uAFoiokgNf0lI','2023-11-28 00:32:11.131404'),('yad174fg6csjhtxqzs0fxvpd0s9w9l9j','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1quCJQ:PTovEKewuLIUT43nhbcZNQNwQn1CYQkbkpUSJIUfVVM','2023-11-04 13:46:44.496005'),('yaynk38nfbdbf7otmztbyah2v13jtdpi','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r0cm4:2FmP24NefDahPkOEq5Q2MdVoXbRp7A9eAQAjlJmRS3M','2023-11-22 07:14:52.311607'),('yjnalaanrq41pormpckwupbykj8mdmvl','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r8YHt:eg3zlnAlLgEsbuWuUDyxMGLTqQxB4UIV3gvzOtRvWOY','2023-12-14 13:04:29.213658'),('ykrmyyasmrsdkf52crw3xgpf6a3ptf17','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5H3b:72AmfLbCoROrX2jjglRyZYUCxZd8E2EiN5mxCxsTQpA','2023-12-05 12:04:11.393175'),('ywiav7rye752cu9xcqtpu93rqoc05b1o','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5NjJ:6mOSlLEStWJjjsqJlHUOQKqbFuraFqagUuGTaVCNMA4','2023-12-05 19:11:41.946203'),('z11jagw5j4m1f8r9oa6tpwa77r52q4o9','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r7xxb:79aKD-3gG52DklsfHDYgPZWhdEMvIFJcjmLG6d0ZXp4','2023-12-12 22:17:07.898668'),('z4voj693msmxihtxqvcldfq77g3axvre','.eJxVjbtuxCAURP-FemXxCGBvFaVLkSrp0eVyWZO1IQKsKIry72GlbbadM2fmlyHV5Cq1Y-vszN4PRGqNnRjtkLaRdGrd2mfK4QI7dYJ9wrKPwhB7igmhp5JdPnZPlZ0V58uiTuwLWvsuNYyFjxLg57VJJYTiQ3Rw9NUdjapLNy7UY-gBr-NukPAJ-VLGX-41-elWme60TW8l0PZy7z4MrNDWYSNawfmTj7PlMPvohVJaRm1AG2mBrNFoFy6ksYuwi45eSwMBZ7RkDFfs7x-M_F10:1r82N9:t0zGO6YiudM__GbrJ7Q_FZxxnpKHzUxTnIKywcn1Kfs','2023-12-13 02:59:47.735484'),('zaa5k3md030uh3mbkpjkxftfnx7mtqht','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r0sNV:XYAc7syGeU0A48M-UdmOr8usKHkXSkX2Vy5lu64nOIw','2023-11-22 23:54:33.623652'),('zj2vtbx09zf6f5ig6taz2cfsyogbkda9','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r5Nqo:TBIHFUS0lLORIT7eeY0AO_Jg2rSL6GVFmKwDrRtCMpI','2023-12-05 19:19:26.483365'),('zjqpqu1o1zvz7mhm2d5goqppmzheghrs','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r2Q5m:YYI6n-BQS_J0J5lXZG_8W9-YopQ22B_wfpvKBuM3TA8','2023-11-27 06:06:38.058102'),('znhii7xkbl5gr0925fr00jzur4ml5xg3','.eJxVjMsKwyAQAP_FcxHdGNEee-83yMbdrWmLQh6n0H8vQg7tdWaYQyXct5L2lZc0k7oqUJdfNmF-ce2CnlgfTedWt2WedE_0aVd9b8Tv29n-DQqupW8hTAFEUCyLCPmcyQi54MgbHuPAgUYLMgzOYgSP0WQOPpAAwQisPl8Pvzih:1r0cXY:Wlrt5CfHenvNdN_b3U5c8meuwBhv2EB64U-5pgB-ZlA','2023-11-22 06:59:52.285841');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_page_users`
--

DROP TABLE IF EXISTS `login_page_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_page_users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `profile_picture` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `status` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `status_message` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `is_online` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `login_page_users_name_f1df7cbb_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_page_users`
--

LOCK TABLES `login_page_users` WRITE;
/*!40000 ALTER TABLE `login_page_users` DISABLE KEYS */;
INSERT INTO `login_page_users` VALUES (1,'pbkdf2_sha256$600000$XCSIoCf8zpqQIgQZFyOzfU$SRWgITJEwaR4AXtZOb6IlOoIEW6fMUBtcdUeC7xn40s=',1,'endgameteam@gmail.com',1,'endgameteam','user/user_1.jpeg','offline',1,'superUser 입니다.',0),(2,'pbkdf2_sha256$600000$w4LBil9NJ4xoqo2z4EOVoJ$+2Lu7FrTKa3bG72reEdmc3154iyxpuilCJOZzylKUxg=',0,'test1@ddd.com',0,'오늘의날짜는30일','user/user_2.jpeg','online',1,'상태메시지 변경 됩니다.',1),(3,'pbkdf2_sha256$600000$wcVgTDYvEjJwji4mclx5OJ$HD+1j4HgqJxUwaSXmOiZk41hRqGRZKdkuW/ru75tcK0=',0,'ted@endgameteam.com',1,'TED','profile_ted.png','online',0,'안녕하세요. 당신의 채팅 친구 TED 입니다.',1),(4,'pbkdf2_sha256$600000$JUIi8GDwaWLHPw96I4WS8t$CqtvC6J2o035mk0KJA/iAPuG089wP8NWVf5o3Xa2FiE=',0,'m7427858@gmail.com',0,'USER_6030','profile_basic.png','online',1,NULL,0),(5,'pbkdf2_sha256$600000$EAml4uKtIm8ClKinE46MOc$HVjTA6zMSw7zA8ItU5oG6QQi4zRYL6VRlzmjCTrQqpk=',0,'test2@ddd.com',0,'USER_7652','profile_basic.png','online',1,NULL,0),(6,'pbkdf2_sha256$600000$K1IvaOZHy4nSQBkv6c1Yws$LfgWPy7xVD+780DL/P4byo+N7yAOTffT7jCE2w3I+oA=',0,'test3@ddd.com',0,'USER_5747','profile_basic.png','online',1,NULL,0),(7,'pbkdf2_sha256$600000$jBYZCGnjCrSlM2zsRJFuTY$qll+5WEHg8YW23t7rNbzcBV8QKzdENhidfBussBnjeY=',0,'test4@ddd.com',0,'USER_7359','profile_basic.png','online',1,NULL,0),(8,'pbkdf2_sha256$600000$9wCmY9Vcnf7mnvqBiVroZ6$LHuO0CGSd280dNj1pupBXfUOEFzszVsx8vZSxPcnFbY=',0,'test5@ddd.com',0,'USER_8746','profile_basic.png','online',1,NULL,0),(9,'pbkdf2_sha256$600000$SFaTgHqEnTk8pCHBecjT67$HN25U+RAwApXFcxdmgffJq/gJy91Q4e7d2gpQyiGsEE=',0,'chatgpt@endgameteam.com',1,'ChatGPT','profile_ted.png','online',0,'안녕하세요. ChatGPT입니다.',1),(10,'pbkdf2_sha256$600000$RjKWUMrALiRDrS3VON8Mhy$rYVps9/oUbBNgrEPTLa7fb5ikapyZjsufIb/emRbp78=',0,'test6@ddd.com',0,'USER_8063','profile_basic.png','online',1,NULL,0),(12,'pbkdf2_sha256$600000$ePhk16ljgu5sNGnKpAeFdp$/pPNAKxRGiJ4RSvj/H9xAxJYMtPD79KoxggESkIbypc=',0,'test7@ddd.com',0,'USER_6621','profile_basic.png','online',1,NULL,0),(13,'pbkdf2_sha256$600000$s5TMp3jcQcaZlkDkNuJL0a$5v3LOWC6TpJqNs4tC/mQWAF5N616Ngb/T9JI+/572hE=',0,'test77@endgameteam.com',0,'USER_579','profile_basic.png','online',1,NULL,0),(14,'pbkdf2_sha256$600000$yOWaPjuYazqIWj3VxBvCrE$bwsCFFHQuFJDZ2d3nUt5IbzrfJOdn+sjP+HB41azMZM=',0,'kangminji_@naver.com',0,'USER_1170','profile_basic.png','online',1,'',1);
/*!40000 ALTER TABLE `login_page_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_page_users_groups`
--

DROP TABLE IF EXISTS `login_page_users_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_page_users_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `users_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login_page_users_groups_users_id_group_id_97cfadb2_uniq` (`users_id`,`group_id`),
  KEY `login_page_users_groups_group_id_7d5b0c47_fk_auth_group_id` (`group_id`),
  CONSTRAINT `login_page_users_groups_group_id_7d5b0c47_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `login_page_users_groups_users_id_fb7feb91_fk_login_page_users_id` FOREIGN KEY (`users_id`) REFERENCES `login_page_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_page_users_groups`
--

LOCK TABLES `login_page_users_groups` WRITE;
/*!40000 ALTER TABLE `login_page_users_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `login_page_users_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_page_users_user_permissions`
--

DROP TABLE IF EXISTS `login_page_users_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_page_users_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `users_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login_page_users_user_pe_users_id_permission_id_ae53bda1_uniq` (`users_id`,`permission_id`),
  KEY `login_page_users_use_permission_id_0d2c82bd_fk_auth_perm` (`permission_id`),
  CONSTRAINT `login_page_users_use_permission_id_0d2c82bd_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `login_page_users_use_users_id_92e83f88_fk_login_pag` FOREIGN KEY (`users_id`) REFERENCES `login_page_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_page_users_user_permissions`
--

LOCK TABLES `login_page_users_user_permissions` WRITE;
/*!40000 ALTER TABLE `login_page_users_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `login_page_users_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-12  8:58:03
