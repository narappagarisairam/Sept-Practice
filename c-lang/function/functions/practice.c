//sum of the square of the all odd numbers from 1 to 25;

#include<stdio.h>
int main(){
	int a,b;
	result=fun(a,b);
    printf("%d",result);
    return 0;
}
int fun(){
    int sum=0;
    for(int num=1;num<=25;num++){
        if(num%2!=0){
            sum=sum+(num*num);
        
        }
    }
    return sum;
}

