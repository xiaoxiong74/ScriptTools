#!/bin/bash
ps -aux 2>/dev/null|grep "pingAll.sh" |grep -vi killed |grep -v "grep" |awk '{print $2}'|xargs kill -9
