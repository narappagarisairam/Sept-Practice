//2) with perameters  return
//sum of two numbers

#include<stdio.h>
int sum(int x,int y){
int r;
printf("enter the numbers x");
scanf("%d",&x);
printf("enter the numbers y");
scanf("%d",&y);
r=x+y;
return r;
}
int main(){
	int a,b;
int result=sum(a,b);
printf("%d",result);
return 0;
}

