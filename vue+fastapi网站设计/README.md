# 中国家庭追踪调查数据分析及可视化平台


## 简介

	中国家庭追踪调查数据分析及可视化平台是山东大学（威海）2020级数据科学与人工智能实验班大作业的一项内容。
	
	在之前的工作中，我们利用中国家庭追踪调查（CFPS）数据，设计了数据库架构和关系。并且进行了从南北、东中西进行数据分析，撰写了一篇关于中国城乡差异和如何乡村振兴的分析报告。在这一部分工作中，我们开发了一个可视化平台，该平台具有连接显示数据库、数据操作、数据可视化等功能。


## 网站功能

>1. 登陆注册系统，可供多用户同时登陆，为每个用户对应一份数据库
>2. 可连接显示 拆分清洗好的CFPS2010-2018年数据库，页面上可以列出数据库的所有表格，选择一个表格，可以列出所有数据
>3. 可在输入框中输入任意 SQL 语句，进行各种数据库操作（从不同表格抽取数据产生新表、数据合并、删除、添加及运算等等）
>4. 对抽取出来的数据进行可视化，支持基础折线图、面积图、柱状图、极坐标柱状图、条形图、堆叠折线图、堆叠面积图、堆叠柱状图、饼图、环形图、玫瑰图、嵌套环形图、散点图、气泡图、漏斗图、堆积条形图、堆积柱状图、极坐标堆积柱状图、堆积百分比柱状图、三维柱状图、象形柱状图等21种可视化方法


## 项目结构

* demo: 前端工程文件
  * src：存储vue文件
    * router：路由文件
    * views：三个vue页面
      * function.vue:功能界面
      * introduction.vue:介绍页面
      * login.vue:登录页面
    * App.vue:配置vue文件
    * main.js:导入需要的包
    * registerServiceWorker.js：vue配置文件
  * 其余文件均为创建工程时自动生成文件
* fastapi0215: 后端工程文件
	* app: fastapi实例，相当于python包
		* models: 定义前后端交互中的请求体，python子包
			* auth.py: 定义token验证中的请求体
			* database.py: 定义数据库操作中的请求体
			* settings.py: 设置
			* token.py: 定义token验证中的请求体
			* user.py: 定义用户系统的请求体
			* visualize.py: 定义可视化数据运算的请求体
		* routers: 处理前端请求，python子包
			* auth.py: 处理token验证的请求
			* database.py: 处理数据库操作的请求
			* user.py: 处理用户系统的请求
			* visitor.py: 处理访客记录的请求
			* visualize.py: 处理可视化运算的请求
	* data: json数据文件
		* col_names.json: 记录所有年份、所有表格所有字段的中英文名称
		* visitor.json: 记录访客人数
	* utils: 各个模块的功能函数
		* database.py: 数据库操作功能函数
		* hashing.py: 哈希加密功能函数
		* validate.py: 有效性验证功能函数
		* visualize.py: 可视化数据运算功能函数
	* main.py: 主函数，用于运行fastapi
	* requirements.txt: 记录后端需要的python包
* 图表说明.xlsx: 可视化图表有关信息


## 讲解视频

> 三阶段成果及原理讲解的B站视频链接：
> 
> [【数据库设计】中国家庭追踪调查数据库设计-山大威海大二上作业A](https://www.bilibili.com/video/BV1YF411h758/)
> [【网站开发】城乡差距与乡村振兴的碰撞—山大威海大二上作业B](https://www.bilibili.com/video/BV1Qi4y1R7WF/)
> [数据可视化网站—山大威海大二上作业C](https://www.bilibili.com/video/BV1tq4y187n6/)


> 作者：范传进、许家路、赵依洋
> 
> 联系方式：2538574548@qq.com