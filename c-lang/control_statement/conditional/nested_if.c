//nested if 
#include<stdio.h>
int main(){
	int a=10,b=20,c=30,d=40;
	if(a<b){
		printf("b is greaterthan a");
	}
	if(b>c){
		printf("b is greater than c");
	}
	else if(c>d){
		printf("c is greaterthan d");
	}
	else{
		printf("d is greater than all");
	}
	return 0;
}
