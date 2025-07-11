#include<stdio.h>
struct Employee
        {
                int id;
                char name[30];
                float salary;
                char address[50];
        };
struct Employee e[100];
void display(int a)
        {
                printf("id : %d ,name : %s ,salary : %f ,address : %s ",e[a].id,e[a].name,e[a].salary,e[a].address);
                printf("\n");
        }

int main()
{
        int i,j,n;
        printf("Enter no of employees : ");
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
                printf("Employee e[%d] id : ",i);
                scanf("%d",&e[i].id);
                printf("Employee e[%d] name : ",i);
                scanf("%s",&e[i].name);
                printf("Employee e[%d] salary : ",i);
                scanf("%f",&e[i].salary);
                printf("Employee e[%d] address : ",i);
                scanf("%s",&e[i].address);
        }
        for(j=0;j<n;j++)
        {
                display(j);
        }
return 0;
}
