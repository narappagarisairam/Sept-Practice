#include<stdio.h>
#include "calculator.h"
int main(){
	int a=10,b=30,c;
	c=add(a,b);
	printf("c=%d",c);
	c=sub(a,b);
	printf("d=%d",c);
	c=mult(a,b);
	printf("e=%d",c);
	c=div(a,b);
	printf("f=%d",c);
	return 0;
}


