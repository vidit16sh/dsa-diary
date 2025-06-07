#include <iostream> 
using namespace std; 
int main(){ 
    int total; 
    cin>>total; 
    int n100 =0,n50= 0,n10= 0,n1 = 0; 
    int count = 0;   
    switch(count){
        case 0: n100 = total/100; 
                cout<<"number of 100 notes :"<<n100<<endl;  
                total = total%100;  
        case 1: n50 = total/50; 
                cout<<"number of 50 notes :"<<n50<<endl;  
                total = total%50; 
        case 2: n10  = total/10; 
                cout<<"number of 10 notes :"<<n10<<endl;
                total = total%10; 
        case 3: n1 = total/1;  
               cout<<"number of 1 notes :"<<n1<<endl;
    }
}