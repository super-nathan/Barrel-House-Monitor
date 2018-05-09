#!/bin/bash
# This script that is called by RC.local at startup. 
# It was orininally designed to notify someone of a 
# a catastrophic failure on another project, but will 
# probably be used on this project to opperate springler 
# solenoids. It is not activly used.


function main
{
Init
WatchPin
}



function Init
{
#this is just a little bit of debugging so I can see the IP of the computer
sleep 120
spreadsheet.py
whatsip=`ifconfig wlan0 | sed -n 2p`
textnathan send --text="$whatsip" --phones=18282892378
}

function WatchPin
{
Wigout=`cat /etc/tempmonitor/wigout.conf`
Temp=`cat /tmp/tempnow.txt`
echo $Wigout
echo $Temp
Wigout=${Wigout/.*}
Temp=${Temp/.*}
echo $Wigout
echo $Temp
while [ "$Temp" -le "$Wigout" ]
do
 sleep 300
done

MyTime=`date +%H%M`
file="/tmp/tempnow.txt"
TempNow=$(cat "$file")
textnathan send --text="The temp at $MyTime is $TempNow" --phones=18282892378
textnathan send --text="The temp at $MyTime is $TempNow" --phones=18473131733

sleep 3600

WatchPin
}


#run
main

