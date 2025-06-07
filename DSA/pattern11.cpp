/*A 
  BC 
  DEF 
  GHIJ 
*/
#include <iostream> 
using namespace std; 
int main(){   
    int n; 
    cin>>n; 
    int c = 'A'; 
    int i = 1;  
    while(i<=n){ 
        int j = 1; 
        while(j<=i){ 
            char ch = c++; 
            cout<<ch; 
            j+=1; 
        }  
        cout<<endl;  
        i+=1; 
    }
}