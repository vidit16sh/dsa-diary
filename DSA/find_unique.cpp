#include <iostream>
using namespace std;
int main()
 {
    int n = 4;  
    int ans = 0;
    int arr[n] ={1,2,5,8} ;
    for(int i = 0;i<n;i++){  
      ans = ans^arr[i];  
    } 
    cout<<ans;
 }