#include <iostream> 
using namespace std; 
int main(){  
    int size = 7; 
    int temp = 0 ;
    int arr[size] ={1,2,3,4,5,6,7}; 
    for(int i = 0; i<(size/2);i++){   
       temp = arr[i]; 
       arr[i] = arr[size-1-i]; 
       arr[size-1-i] = temp;  
    } 
    for(int j = 0;j<size;j++){ 
        cout<<arr[j]; 
    } 
}