#include <iostream> 
using namespace std; 
int main(){   
    int size = 9; 
    int arr[size] = {1,2,3,4,5,6,7,8,9}; 
    for(int i = 0;i<size;i = i + 2) 
    { 
        if( i+1 < size){ 
            int temp = arr[i+1]; 
            arr[i+1] = arr[i]; 
            arr[i] = temp;
        }
    } 
    for(int j = 0; j<size ;j++){ 
        cout<<arr[j];
    } 
}