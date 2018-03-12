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

 Date: 17/12/2017 13:41:52
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for references
-- ----------------------------
DROP TABLE IF EXISTS `references`;
CREATE TABLE `references` (
  `id` varchar(100) NOT NULL,
  `property` varchar(100) NOT NULL,
  `value` varchar(200) NOT NULL,
  `value_type` varchar(100) DEFAULT NULL,
  `snaks_order` varchar(100) NOT NULL,
  `ref_value` varchar(200) NOT NULL,
  `ref_value_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`,`property`,`value`,`snaks_order`,`ref_value`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;
