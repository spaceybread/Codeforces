#include<iostream>
#include<string.h>
#include<math.h>

using namespace std;

int main() {
    
    long long int n;
    cin>>n;
    
    long long int sum;
    
    if (n % 2 == 0) {
        sum = n/2;
    }
    else {
        sum = -((n + 1)/2);
    }
    
    cout<<sum;
    
}
