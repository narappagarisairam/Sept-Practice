#include<stdio.h>
int main(){
	extern int x;
	printf("%d",x);
	x++;
	printf("%d",x);
}

