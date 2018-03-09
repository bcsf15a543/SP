#! /bin/sh 

if [ $# -eq 2 ]

then

	num1=$1
	num2=$2

	if [ $num1 -eq $num1 2>/dev/null  ]
		then
		       if [ $num2 -eq $num2 2>/dev/null ]
		       then
			       ra=`expr $num1 + $num2`
			       echo "Result of Addition : $ra "
			       rs=`expr $num1 - $num2`
			       echo "Result of Subtraction : $rs "
			       rm=`expr $num1 \* $num2`
			       echo "Result of Multiplication : $rm "
			       if [ $num2 -eq 0 ]
				then
				   echo "The second argument is zero thus division modulus is impossible "	         
				else
				   rd=`expr $num1 / $num2`
				   echo "Result of Division : $rd "  
				   rmm=`expr $num1 % $num2`
				   echo "Result of modulus is : $rmm "    
			       
		               fi
			else
		       echo "Wrong input"
		       fi
		   
	else
	   echo "Wrong input"
	fi
else
  echo "Number of arguments are incorrect"

fi


