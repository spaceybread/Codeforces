#include<iostream>
#include<math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    int n;
    cin >> n;
        
    long long int money[n];
    long long int val = 0;
    long long int sum = 0;
    
    int i = 0;
    
    while (i < n) {
        cin >> money[i];
        i = i + 1;
    }
    
    i = 0;
    
    
    while (i < n) {
        if (val < money[i]) {
            val = money[i];
        }
        i = i + 1;
    }
    
    i = 0;
    
    while (i < n) {
        sum = (val - money[i]) + sum;
        i = i + 1;
    }

    cout << sum; 
}
