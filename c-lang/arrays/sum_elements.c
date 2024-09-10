// sum of elements in the array 
#include<stdio.h>
int main(){
    int arr[5],sum=0;
    for(int i=0;i<5;i++){
        printf("enter the elements %d : ",i);
        scanf("%d",&arr[i]);
        sum=sum+arr[i];
    }
    printf("%d",sum);
    return 0;
}

