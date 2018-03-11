#!/bin/bash
Is_Lower()
{
       echo "Before converting : "$input
       input=$1
       input=`echo $input | tr "[A-Z]" "[a-z]"`
       echo "After converting : " $input
}


is_Root()
{
	name=`whoami`
	test $name = root
        if [ $? = 0 ]
	then
		return 0
	else
		return 1
	fi
}

is_user_exist()
{
	username=$1
	myname=`grep "$username" "/etc/passwd"` 
	if [ $? = 0 ]
        then
                IFS=":"
                set $myname
                if [ $1 = $username ]
                then
			return 0 
                else
                	return 1
                fi
	else
		return 1
        fi

}

PS3="Choose an option ! "

select choice in ConvertString CheckRoot CheckUser
do
	if [ $choice = "" ]
	then
		echo "Invalid Option.Choose again"
		continue
	elif [ $choice = ConvertString ]
	then
                read -p "Enter string to convert  " input
		Is_Lower $input
                break     
	elif [ $choice = CheckRoot ]
        then
                is_Root 
		if [ $? = 0 ]
                then
                echo "Yes the root is running this script"
                else
                echo "No the root is not running this script"
                fi
                break
	elif [ $choice = CheckUser ]
        then
                read -p "Enter username  " input
		is_user_exist $input
		if [ $? = 0 ]
                then
                echo "Yes the username : $input exists"
                else
                echo "No the username : $input does not exit"
                fi
                break
	
        else
              echo "Invalid Option.Choose again"
              continue
                
                
	fi

done

