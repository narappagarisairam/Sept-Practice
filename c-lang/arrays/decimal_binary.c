#include<stdio.h>
int main(){
    int arr[15],num;
    int i=0;
    printf("enter the decimal number : ");
    scanf("%d",&num);
    while(num>0){
        arr[i]=num%2;
        num=num/2;
        i++;
    }
    printf("binary number : ");
    for(int j=i-1;j>=0;j--){
        printf("%d",arr[j]);
    }
    printf("\n");
    return 0;
}
