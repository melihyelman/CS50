#include <math.h>
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float dollars;
    int counter = 0;
    do
    {
        dollars = get_float("Change : ");
    }while(dollars<=0);
    int cents = round(dollars * 100);
    while (cents >=25){
        counter++;
        cents-=25;
    } 
    while (cents >=10){
        counter++;
        cents -=10;
    } 
    while (cents >= 5){
        counter ++;
        cents -=5;
    } 
    while (cents >= 1){
        counter++;
        cents --;
    }
    printf("%i\n",counter);
}