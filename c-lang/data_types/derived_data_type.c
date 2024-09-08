//array
#include<stdio.h>
int main(){
 int numbers[5] = {1, 2, 3, 4, 5};
printf("First number: %d\n", numbers[0]); 
 
}



//pointers
#include<stdio.h>
int main(){
 
 int age = 25;
int *ptr = &age;
printf("Address of age: %p\n",ptr);  

}


//struct
#include<stdio.h>
int main(){
 struct Person {
    char name[50];
    int age;
    float height;
};

struct Person person1 = {"John", 30, 5.9};
printf("Name: %s, Age: %d, Height: %.1f\n", person1.name, person1.age, person1.height); 

}


//union
#include<stdio.h>
#include<string.h>
int main(){
 union Data {
    int i;
    float f;
    char str[20];
};

union Data data;
data.i = 10;
printf("Integer: %d\n", data.i);  
data.f = 220.5;
printf("Float: %.1f\n", data.f);
strcpy(data.str, "Hello");
printf("String: %s\n", data.str);  

}



//enumeration enum
#include<stdio.h>
#include<string.h>
int main(){
enum Weekday { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };
enum Weekday today = Wednesday;
printf("Today is day number: %d\n", today);  

}

