#include<iostream>
#include<math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    long long int n;
    long long int i = 0;
    long long int count = 1;
    
    cin >> n;
    
    long long int table[n];
    
    while (i < n) {
        cin >> table[i];
        i = i + 1;
    }
    
    i = 0;

    while (i < (n - 1)) {
        if (table[i] != table[i + 1]) {
            count = count + 1;
        }
        i = i + 1;
    }
    
    cout << count;
}


