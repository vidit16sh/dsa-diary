/* 
   1 
  121
 12321 
1234321    
*/
#include <iostream> 
using namespace std; 
int main(){ 
    int n; 
    cin>>n; 
    int i = 1; 
    while (i<n){  
    int s = n-i; 
      while(s){ 
        cout<<" "; 
        s -=1;
    }
    int j = 1; 
       while(j<i){ 
        cout<<j; 
        j++;
       } 
    while(j>0){ 
         cout<<j; 
         j--;
     }
      cout<<endl;    
    i+=1;
    } 
}