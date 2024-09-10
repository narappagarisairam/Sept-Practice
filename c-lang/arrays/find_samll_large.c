//find the smallest and largest elements in the array;
#include<stdio.h>
int main(){
    int arr[10];
    for(int i=0;i<10;i++){
        printf("enter the elements");
        scanf("%d",&arr[i]);
    }
    int small,large;
    small=large=arr[0];
    for(int i=0;i<10;i++){
        if(arr[i]<small){
            small=arr[i];
        }
        if(arr[i]>large){
            large=arr[i];
        }
    }
    printf("small is %d and large is %d",small,large);
}

