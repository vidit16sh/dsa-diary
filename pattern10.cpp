/*abc
  def
  ghi*/
#include <iostream> 
using namespace std; 
int main(){ 
    int n; 
    cin>>n; 
    int count = 1;
    int i = 1; 
    int c = 'A'; 
    while (i<=n){ 
       int j = 1; 
       while(j<=n){  
        char ch = c++;
        cout<<ch;  
        j +=1;
       }  
    cout<<endl; 
    i+=1;
    } 
}