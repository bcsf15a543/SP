#!/bin/bash
showMeOwner()
{
if [ $# = 1 ]
then
	cd ~/
        name=$1
	for x in `ls`
	do
		set `ls -li $x`
      		if [ -f $x ]
		then
			if [ $4 = $name ]
			then
			echo "Owner|" $name
                        shift
                        shift
                        echo "Name|" $8 
		fi
		fi 
	done
elif [ $# = 0 ]
then
	echo "No arguments passed"
else
	echo "More than 1 arguments passed"
fi



}
showMeOwner $@
