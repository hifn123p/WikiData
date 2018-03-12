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

 Date: 17/12/2017 13:41:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for mainsnaks
-- ----------------------------
DROP TABLE IF EXISTS `mainsnaks`;
CREATE TABLE `mainsnaks` (
  `id` varchar(100) NOT NULL,
  `property` varchar(100) NOT NULL,
  `value` varchar(200) NOT NULL,
  `value_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`,`property`,`value`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
