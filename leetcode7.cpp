// find the single unique number which count is 1 and others count is 2 in array of size n and m number comes twice
// eg : [1,2,2,3,3,4,4] 
#include <iostream> 
using namespace std; 
int main(){ 
int a = 0 ;
int arr[9] = {1,2,2,3,3,4,4,5,5}; 
for(int i = 0;i<9;i++){ 
    a = a^arr[i]; 
} 
cout<<a;
} 
