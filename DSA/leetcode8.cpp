// unique occurence problem  
#include <iostream>  
#include <algorithm> 
#include <vector>
using namespace std; 
int main(){ 
    bool a = true; 
    int arr[] = {3,2,2,3,3,1}; 
    int n = sizeof(arr)/sizeof(arr[0]);
    sort(arr,arr + n); 
    vector<int> ans;  
    int i = 0; 
    while(i<n){ 
        int count = 1;   
        for(int j = i+1;j<n;j++) 
        {  
           if(arr[i] == arr[j]){ 
            count++; 
           } 
           else{ 
            break;
           } 
        }  
        i += count;  
        ans.push_back(count);
    }   
    sort(ans.begin(),ans.end()); 
    for(int i = 0;i<ans.size();i++){ 
        if(ans[i] == ans[i+1])
        { 
            a = false; 
            break; 
        } 
    }  
    cout<<a<<endl;
}