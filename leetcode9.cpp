// find duplicate int in array ; 
#include <iostream> 
#include <algorithm>  
#include <vector>
using namespace std; 
int main(){ 
    int a = 0;  
    vector <int> arr = {1,2,3,4,5,6,7,8,9,6}; 
    for(auto el:arr){ 
         a ^= el;  
    } 
    for(int i = 1;i<arr.size();i++){ 
        a ^=i;
    } 
    cout<<a;
}