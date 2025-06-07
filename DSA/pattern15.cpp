/*1234554321
  1234**4321 
  123****321 
  12******21 
  1********1 
*/
#include <iostream> 
using namespace std; 
int main(){ 
    int n; 
    cin>>n; 
    int i = 1; 
    while (i<=n){  
    int j = 1 ; 
    while(j<=(n-i+1)){ 
        cout<<j; 
        j++;
       } 
     if(i>1){  
        int l = (i-1)*2;
        int k = 1;
         while(k<=l){ 
             cout<<"*"; 
             k++;
         }
     }
    int m = n-i+1;  
    while(m){ 
        cout<<m; 
        m--;
      }  
    cout<<endl;
    i++;
    } 
}