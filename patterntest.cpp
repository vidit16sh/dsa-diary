#include <iostream> 
using namespace std; 
int main(){ 
    int n = 5;
    int s = n;
    for (int i = 1; i <= n;i++){
        for (int k = s ; k > 0;k--){
            cout << " ";
        }
        for (int j = 0; j < i;j++){
             cout << "*";   
       }
       for (int l = 1; l < i;l++){
           cout << "*";
       }
       {
       }
        for (int m = s ; m > 0;m--){
             cout << " ";
            
        }
        cout <<"\n";
        s--;
    } 

}