#!/bin/bash
if [ $# != 1 ];then
	echo -e "please input ip!\nusage:sh pingAll.sh 192.168.109"
	exit
fi
echo "==========Unreachable IP============:"
for i in `seq 1 255`
do
	ping -c 1 -w 1 ${1}.${i} |awk 'BEGIN{FS="\n";RS="@@";OFS="#"}{print $1,$2,$3,$4}'|grep -v ttl |awk '{print $2}' |grep ".*" --color=always
done
