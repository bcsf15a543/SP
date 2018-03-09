#!/bin/bash

totalarguments=$#

if [ "$totalarguments" -ne 2  ] 
 
       then

       if [ "$totalarguments" -ne 2  ] 
           then
	   echo "Number of arguments are not correct"
       fi

fi

if [ $totalarguments = 2 ]

	then

		filename=$1

		studentname=$2

		set `ls -li $filename`

		echo "OWNER : " $4

		echo "GROUP : " $5

		echo "PERMISSION : " $2

		echo "FILE NAME :" $filename

		if [ $4 = $studentname ]
		  then
		   echo "CHEATING : 0 "
		else
		   echo "CHEATING : 1"
                fi

fi
if [ $totalarguments = 4 ]

	then

		filename=$1

		studentname=$2

                filename2=$3

                studentname2=$4

		set `ls -li $filename`

		echo "OWNER : " $4

		echo "GROUP : " $5

		echo "PERMISSION : " $2

		echo "FILE NAME :" $filename

		if [ $4 = $studentname ]
		  then
		   echo "CHEATING : 0 "
		else
		   echo "CHEATING : 1"
		fi

                set `ls -li $filename2`

		echo "OWNER : " $4

		echo "GROUP : " $5

		echo "PERMISSION : " $2

		echo "FILE NAME :" $filename2

		if [ $4 = $studentname2 ]
		  then
		   echo "CHEATING : 0 "
		else
		   echo "CHEATING : 1"
		fi

                echo "Difference between two files "

		diff -c "$filename" "$filename2" #COMPARING THE CONTENT

                test studentname = studentname2 && echo "Same user name" || echo "Different username"

               
fi








