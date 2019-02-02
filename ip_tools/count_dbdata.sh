#!/bin/bash


HOSTNAME="192.168.108.140"                                             #数据库信息
PORT="3306"
USERNAME="root"
PASSWORD="passwd"

DBNAME="tutengfei"                                                      #数据库名称

count_sql="insert into terrorist_provincenum 
(select substring(birth_place,1,3) as province,count(*) as num 
from terrorist_information2
where substring(birth_place,1,3)!='NUL'
group by substring(birth_place,1,3));"	
delete_sql="delete from terrorist_provincenum;"	
mysql -h${HOSTNAME} -P${PORT} -u${USERNAME} -p${PASSWORD} -D ${DBNAME} -e  "${delete_sql}"								 
mysql -h${HOSTNAME} -P${PORT} -u${USERNAME} -p${PASSWORD} -D ${DBNAME} -e  "${count_sql}"	
