/*1 
  23 
  456 
  78910 
  1112131415*/
#include <iostream> 
using namespace std; 
int main(){ 
    int n; 
    cin>>n; 
    int count = 1;
    int i = 1; 
    while (i<=n){ 
       int j = 1; 
       while(j<=i){ 
        cout<<count; 
        count+=1; 
        j +=1;
       }  
    cout<<endl; 
    i+=1;
    } 
}