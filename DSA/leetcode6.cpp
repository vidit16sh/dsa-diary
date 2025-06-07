/*swap the aletrnate elements in array eg {1,2,3,4} = {2,1,4,3}*/ 
#include <iostream> 
using namespace std; 
int main(){  
    int size = 9; 
    int arr[size] ={1,2,3,4,5,6,7,8,9}; 
    for(int i = 0 ;i<(size-1);i+=2){ 
        swap(arr[i],arr[i+1]);
    } 
    for(int j = 0;j<size;j++){ 
        cout<<arr[j];
    }
}