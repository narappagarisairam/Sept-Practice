#!/bin/bash
echo "enter number1"
read num1
echo "enter the number 2"
read num2
if [ $num1 -gt $num2 ]; then
	echo "$num1 is bigger"
else
	echo "$num2 is bigger"
fi
