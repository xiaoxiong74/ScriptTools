#!/bin/bash
echo 'inse_sql start'
HOSTNAME="192.168.108.140"                                             #数据库信息
PORT="3306"
USERNAME="root"
PASSWORD="passwd"
DBNAME="tutengfei"                                                      #数据库名称
insert_sql="insert into terrorist_information1 select * from terrorist_information;"	
delete_sql="delete from terrorist_information1;"
mysql -h${HOSTNAME} -P${PORT} -u${USERNAME} -p${PASSWORD} -D ${DBNAME} -e "${delete_sql}"									 
mysql -h${HOSTNAME} -P${PORT} -u${USERNAME} -p${PASSWORD} -D ${DBNAME} -e "${insert_sql}"	
echo "inser_sql down"								 
										 
										 
