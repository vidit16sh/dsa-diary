/*the pattern : 1234 
                1234 
                1234 
*/ 

#include <iostream> 
using namespace std; 

int main(){ 
    for(int i = 0;i<4;i++){ 
        for(int j = 1; j<=4;j++){ 
            cout<<j;
        } 
        cout<<"\n";
    }
}