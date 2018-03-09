#!/bin/bash
arrayContent=(`cat "file1"`)
echo "Array is " ${arrayContent[*]}
echo "Length is " ${#arrayContent[*]}
echo "Length of the element at third index "  ${#arrayContent[2]}
