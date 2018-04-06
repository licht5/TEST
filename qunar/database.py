#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "0801", "RUNOOB")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT sname FROM STUDENT WHERE ssex='FE'")
cursor.execute("CREATE TABLE COURSE (CNO CHAR (4) PRIMARY  KEY ,CNAME CHAR(40) NOT NULL ,CPNO CHAR (4),CEDIT SMALLINT ,FOREIGN KEY (CPNO) REFERENCES COURSE(CPNO) )")
cursor.execute("CREATE TABLE SC (SNO CHAR(9),CNO CHAR (4)  ,GRADE SMALLINT ,PRIMARY KEY(SNO,CNO),FOREIGN KEY (CPNO) REFERENCES COURSE(CPNO),FOREIGN KEY (SNO) REFERENCES STUDENT(sno))")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("seslect : %s " % data)

# 关闭数据库连接
db.close()
