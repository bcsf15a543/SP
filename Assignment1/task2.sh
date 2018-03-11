#!/bin/bash
filename=$1
if [ $# -eq 0 ]
then
	echo "No argument passed"
elif [ $# -gt 1 ]
then
	echo "More than one argument passed"
elif [ ! -f $filename ]
then
	echo "Not a regular file "
else
	count=1
        if [ -f "./evenfile" ] # Files with same name should not be created
        then
		echo "Even file already exists ! "
		exit 1
        fi
        if [ -f "./oddfile" ] # Files with same name should not be created
        then
		echo "Odd file already exists ! "
		exit 1
        fi
        touch "evenfile"
        touch "oddfile"
	while read line
	do
	status=`expr $count % 2 `
	if [ $status -eq 0 ]
	then
		echo $line 1>>evenfile
	else
		echo $line 1>>oddfile
	fi
	count=`expr $count + 1`
	done < $filename
fi

