//simple calculator
#include<stdio.h>
int main(){
	int n1,n2,result;
	char opt;
	printf("enter the number 1 :");
	scanf("%d",&n1);
	printf("enter the number 2:");
	scanf("%d",&n2);
	getchar();
	printf("choose the option : a=addition\n b=subtraction\n c=multiplication\n d=division\n e=molular division \n");
	printf("enter the option : ");
	scanf("%c",&opt);
	fflush(stdout);
	if (opt=='a'){
		result=n1+n2;
	}
	else if(opt=='b'){
		result=n1-n2;
	}
	else if(opt=='c'){
		result=n1*n2;
	}
	else if(opt=='d'){
		result=n1/n2;
	}
	else if(opt=='e'){
		result=n1%n2;
	}
	else{
		printf("enter the valid option");
	}
	printf("result is : %d ",result);
		return 0;
      
}
