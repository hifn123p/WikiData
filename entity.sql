/*
 Navicat Premium Data Transfer

 Source Server         : my
 Source Server Type    : MariaDB
 Source Server Version : 100211
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MariaDB
 Target Server Version : 100211
 File Encoding         : 65001

 Date: 17/12/2017 13:41:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for entity
-- ----------------------------
DROP TABLE IF EXISTS `entity`;
CREATE TABLE `entity` (
  `id` varchar(100) NOT NULL,
  `en` varchar(200) DEFAULT NULL,
  `cn` varchar(200) DEFAULT NULL,
  `descriptions` longtext DEFAULT NULL,
  `aliases` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
