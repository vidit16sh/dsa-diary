#include <iostream> 
#include<vector> 
using namespace std; 
int main(){ 
    vector<int> n; // intialize an vector , vector is a dynamic array 
    n.push_back(1); // to insert an element in vector 
    n.push_back(2); 
    n.push_back(3);  
    for(int i = 0;i<n.size();i++){ 
        cout<<n[i];
    }   
    vector<int>::iterator it; //iterator
    for(it = n.begin(); it!=n.end();it++) 
    {  
        cout<<*it<<endl;
    } 
    n.pop_back(); // to pop out last element 
    for(auto element:n) // kind of for each loop ;
    { 
        cout<<element<<endl;
    }
}