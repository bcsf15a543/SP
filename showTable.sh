#!/bin/bash

Mul()
{
	num=$#
	if [ $# = 0  ]
	then
		echo "No arguments are passed"
		return

	elif [ $num -gt 6 ]
		then
		echo "More than 6 arguments are passed"
	elif [ $num -eq 1 ]
		then
		if [ $1 -eq $1 ]
		then
			start=1
			while [ $start -le 10 ]
			do
			echo "$1 * $start = `expr $1 \* $start`"
			start=`expr $start + 1`
			done
		else
			echo "Invalid input !"
		fi
	elif [ $num -eq 3 -a $2=-s ] 
	then
		if [ $1 -eq $1 -a $3 -eq $3 ]
		then
			start=$3
			while [ $start -le 10 ]
			do
			echo "$1 * $start = `expr $1 \* $start`"
			start=`expr $start + 1`
			done
		else
			echo "Invalid first or third argument!"
		fi
	elif [ $num -eq 3 -a $2=-e ] 
	then
		if [ $1 -eq $1 -a $3 -eq $3 ]
		then
			start=1
			while [ $start -le $3 ]
			do
			echo "$1 * $start = `expr $1 \* $start`"
			start=`expr $start + 1`
			done
		else
			echo "Invalid first or third argument!"
		fi
	elif [ $num -eq 5 -a $2=-s -a $4=-e ] 

	then
		if [ $1 -eq $1 -a $3 -eq $3 -a $5 -eq $5 ]
		then
			if [ $3 -lt $5 ]
                        then
		                start=$3
				while [ $start -le $5 ]
				do
				echo "$1 * $start = `expr $1 \* $start`"
				start=`expr $start + 1`
				done
                        else
                        echo "start is greater than the end"
                        fi
		else
			echo "Invalid first third or fifth argument!"
		fi
	elif [ $num -eq 6 -a $2=-s -a $4=-e -a $6=-r ]
	then
		if [ $1 -eq $1 -a $3 -eq $3 -a $5 -eq $5 ]
		then
                        if [ $3 -lt $5 ]
                        then
				start=$5
				while [ $start -ge $3 ]
				do
				echo "$1 * $start = `expr $1 \* $start`"
				start=`expr $start - 1`
				done
                        else
                        echo "start is greater than the end"
                        fi
		else
			echo "Invalid first third or fifth argument!"
		fi
	else
		echo "No valid operation found for the argument list"
	fi
}
 
Mul $@
 
