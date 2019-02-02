#!/bin/bash

HOSTNAME="192.168.108.140"                                             #数据库信息
PORT="3306"
USERNAME="root"
PASSWORD="passwd"

DBNAME="tutengfei"                                                      #数据库名称

clean_sql="insert into terrorist_information2 (select * from terrorist_information where sex='1' and birthday>'2000-01-01');"		
delete_sql="delete from terrorist_information2;"	
mysql -h${HOSTNAME} -P${PORT} -u${USERNAME} -p${PASSWORD} -D ${DBNAME} -e  "${delete_sql}"								 
mysql -h${HOSTNAME} -P${PORT} -u${USERNAME} -p${PASSWORD} -D ${DBNAME} -e  "${clean_sql}"	
