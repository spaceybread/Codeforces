#include<iostream>
#include<math.h>
#include <string>

using namespace std;

int main() {
    
    long long int n;
    
    cin >> n;
    
    long long int i = 0;
    long long int numbers[2*n];
    
    while (i < 2*n) {
        cin >> numbers[i] >> numbers[i + 1];
        i = i + 2;
    }
    
    i = 0;
    
    while (i < 2*n) {
        long long int a = numbers[i];
        long long int b = numbers[i + 1];
        long long int k;
        long long int hig;
        long long int rem;
        
        if (a % b == 0) {
            cout << 0 << "\n";
        }
        
        else {
            k = a/b;
            hig = (k+1)*b;
            rem = hig - a;
            cout << rem << "\n";
        }
        
        i = i + 2;
    }
    
}

