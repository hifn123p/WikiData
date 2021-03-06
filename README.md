# wikidata_query
wikidata query by GUI

# 项目1：关系数据库系统：Wikidata的设计，实现和查询处理 #

**任务介绍如下:**

1. 研究并了解给定的数据源并设计一些有用的查询。
2. 为数据设计关系数据库（一组模式），以便您可以将数据加载到数据库中，并提交您设计的查询以及需求中列出的查询。
3. 验证模型的设计。您应该优化您的设计（例如，通过实现索引），以便数据库可以在合理的时间内返回查询的结果。
4. 实现简单的图形用户界面来执行查询，以便我可以检查设计的性能。
5. 准备5-10分钟的演示，展示您的初步设计。
6. 撰写报告以描述您的设计和实现，并发出所有源代码（MySQL脚本以及GUI代码）。

## 数据规格 ##
Wikidata是一个免费和开放的知识库，可以由人类和机器读取和编辑。 Wikidata作为其维基媒体姐妹项目的结构化数据的中心存储，包括Wikipedia，Wikivoyage，Wikisource等。 Wikidata还为维基媒体项目之外的许多其他网站和服务提供支持！

Wikidata的内容可以在免费许可证下使用，使用标准格式导出，并且可以链接到链接的数据Web上的其他打开的数据集。

对于此项目，您将获得Wikidata最新数据的JSON转储

您可以从 http://adapt.seiee.sjtu.edu.cn/~frank/wikidata-latest-all.json.bz2 下载，并用bzip解压缩。

请仔细阅读https://www.mediawiki.org/wiki/Wikibase/DataModel/JSON 

用于转储文件格式的https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer 以及Wikidata的基本数据模型和定义。

-------------------------------------------------------------------------------------------------

您需要创建一个关系数据库来存储整个数据转储。您还应仔细设计这些表格，以满足查询和大数据量的需要。

所需查询
1. 给定一个名称，返回与该名称相匹配的所有实体。
2. 给定一个实体，返回它所属的所有先前类别（实例和子类）。
3. 给定一个实体，在一个语句中返回与该实体共同发生的所有实体。
4. 给定一个实体，返回它拥有的所有属性和语句。
5. 设计和实施基本问答（问答）系统，例如如果我问中国人口是多少，应该回答正确答案。


您需要使用ER图设计给定数据的模型，并将模型转换为真实关系数据库（MySQL）的方案

初始版本通常不能满足所有要求。为了使您的模型快速或高效地为您提出的查询，您需要修改模型的设计，并调整数据库的参数，使您的数据库运行更快。潜在优化可以包括但不限于精简表设计，建筑索引，非规范化等。然而，无论您使用什么样的优化，您都应该给出真正需要做的有说服力的理由，确实有一定的效果。换句话说，您需要设计坚实的实验来展示您的设计。

 一个有效的实验应至少包含以下部分：
1. 硬件规格
2. 数据集
3. 测试查询
4. 初始化脚本
5. 实验程序
6. 结果分析

对于您的每个优化，您应该设计一个实验来演示优势和劣势，以及是否将优化作为设计的一部分。 说，索引可能会提高查询的速度。 但是，它也需要磁盘空间来存储它们。 因此，如果一列不想被过滤，则不需要在其上构建索引。
