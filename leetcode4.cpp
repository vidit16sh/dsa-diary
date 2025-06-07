// compliment of base 10 
#include <iostream> 
using namespace std; 
int main(){  
    int a = 5; 
    int comp = ~a; 
    int mask = 0; 
    while(a!=0){  
       mask = (mask << 1) | 1 ; 
        a = a>>1 ; 
    } 
    comp = comp&mask; 
    cout<<comp;
}