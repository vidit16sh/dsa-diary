// reverse of an integer 
#include <iostream> 
using namespace std; 
int main(){  
int x = 123;
long r = 0; 
int dig = 0;   
while (x != 0){ 
    dig = x % 10; 
    r = r*10 + dig; 
    x /=10;   
    }  
if (r <= INT_MAX && r >= INT_MIN) {
     cout<<r;
    } 
}  
