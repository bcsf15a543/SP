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
        if [ -f result ]
        then
              rm -r result
        fi
        echo "Before removing duplicates"
	cat "$filename"
	sort "$filename" | uniq -u 1>>result
	echo "After removing duplicates"
        rm -r "$filename"	
	cat result>>"$filename"  
        cat "$filename"    
        rm -r result    
fi

