#include<iostream>
#include<string.h>
#include<math.h>

using namespace std;

int main() {
    
    long long int n;
    cin>>n;
    
    long long int k;
    cin>>k;
    
    if (k <= (n / 2 + n % 2)) {
        cout<<(k * 2 - 1);
    }
    else {
        
        cout << ((k - (n / 2 + n % 2)) * 2);
        
    }
    return 0;
    
}
