#include <iostream> 
using namespace std; 
int main(){   
    int n = -15; 
    int rem = 0; 
    while(n!=0){ 
        rem = rem + n%2;  
        n = n/2;
    }  
    if(rem == 1 || rem == -1){ 
        cout<<"true"; 
    } 
    else if(rem > 1 || -1 > rem){ 
        cout<<"false"; 
    } 
    else cout<<"n is 0"; 
}