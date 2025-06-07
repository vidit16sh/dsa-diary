// find the difference between product and sum of digits of number 
#include <iostream> 
using namespace std; 
int main(){ 
    int n; 
    cin>>n;
    int mul = 1; 
        int sum = 0; 
        int rem; 
       for(int i = 0;n>0;i++){  
           rem = n%10;   
           mul *= rem;  
           sum += rem; 
           n /= 10; 
       } 
       cout<<"the mul :" << mul <<endl; 
       cout<<"the sum : " << sum << endl;  
       cout<<" the total :" << sum+mul;
} 