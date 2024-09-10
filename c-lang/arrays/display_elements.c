//array to display the elements
#include<stdio.h>
int main(){
    int arr[5];
    for(int i=0;i<5;i++){
        printf("enter the value of array %d ",i);
        scanf("%d",&arr[i]);
    }
    printf("enter the elements");
    for(int i=0;i<5;i++){
        printf("%d \t",arr[i]);
    }
    printf("\n");
    return 0;
}

