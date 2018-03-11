#!/bin/bash
My_Sort_Func()
{
	for name in `ls`
	do
	IFS="."
	set $name
        if [ -d "./$2" ]
	then
                
                if  [ -f "./$2/$name" ] 
                then
			echo "File with the same name already exists in $2 ! Can not move $name ."
                	
			
                else
                	mv "./$name" "./$2/$name"
                        
                fi
	else
		
                	mkdir "./$2"
			mv "./$name" "./$2/$name"
              
	fi
	done

}

if [ $# -gt 0 ]
then
	echo -en "No arguments should be passed.\nFiles in your current directory are meant to be sorted"
	exit 0
fi
My_Sort_Func 
echo "Done moving..."
