#!/bin/bash
name=$1
path=`ps -all -A | grep "$name"`
set $path
if [ $? = 0 ]
then
	echo "PID : " $4
        echo "Name : " $name
        echo "PPID : " $5
        echo "State : Running"
      
else
	echo "No the process isnt running"
fi
