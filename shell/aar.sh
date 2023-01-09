#!/bin/sh

# shell判断进程脚本, 后台执行nohup sh ssrcron.sh
date >> aar.txt
echo "the aar is running" >> ssrcron.txt
while :
do
stillRunning=$(ps -ef |grep SCREEN |grep -v "grep")
if [ -z "$stillRunning" ]
then
date >> aar.txt
echo "the screen was closed!!!!!!!!!!!!!!!!!" >> ssrcron.txt
sh ./run.sh start
date >> aar.txt
echo "the screen was started!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" >> ssrcron.txt
fi
sleep 10
done