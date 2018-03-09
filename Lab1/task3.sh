#!/bin/bash

UNIX=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora');

echo "Printing elements of array "${UNIX[*]} #printing all array

echo "Printing length of array " ${#UNIX[*]} # printing length of the array

echo "Length of second element " ${#UNIX[2]} # printing the length of second element

echo "Priting elements from 3rd index" ${UNIX[*]:3:2}   #printing all elements from 3

 

echo "After replacement " ${UNIX[*]/Ubuntu/SCO}  #to replace ubunto with sgo

UNIX=(${UNIX[*]} "AIX" "HP-UNIX") #to add elements in existing array

echo "After addition" ${UNIX[*]} # displaying elements

unset UNIX[2] #remove the third element

echo "After removal " ${UNIX[*]}

LINUX=("${UNIX[*]}") #copying UNIX into LINUX

echo "LINUX ARRAY"${LINUX[*]}

BASH=("${UNIX[*]}" "${LINUX[*]}") # copying UNIX and LINUX into BASH

echo "BASH ARRAY" ${BASH[*]}

unset LINUX[*]  #unset LINUX

echo "LINUX ARRAY after unset"  ${LINUX[*]}
 
unset UNIX[*]   #unset UNIX

echo "UNIX ARRAY after unset"  ${UNIX[*]}







