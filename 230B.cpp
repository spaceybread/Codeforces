#include<iostream>
#include<math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    long long int limit = 1000000;
    long long int lower = sqrt(limit);

    int numbers[limit];
    
    long long int n = 1;
    long long int i = 2;
    long long int m = 1;
    
    while (n < limit + 1) {
        numbers[n] = n;
        n = n + 1;
    }
    
    while (i < lower) {
        if (numbers[i] != 0) {
            m = 1;
            while ((m + i) < limit) {
                if (numbers[m + i] % numbers[i] == 0) {
                    numbers[m + i] = 0;
                }
                m = m + 1;
            }
        }
        i = i + 1;
    }
    
    cin >> n;
    long long int ins[n];
    i = 0;
    
    while (i < n) {
        cin >> ins[i];
        i = i + 1;
    }
    
    i = 0;
    
    while (i < n) {
        m = ins[i];
        
   
        
        if (m == 4) {
            cout << "YES" << "\n";
        }
        else if (m % 2 == 0 and m != 0) {
            cout << "NO" << "\n";
        }
        else if (m == 1) {
            cout << "NO" << "\n";
        }
        
        else {
            long double l = sqrt(m);
            
            if (l != floor(l)) {
                cout << "NO" << "\n";
            }
            else {
                m = (int) l;
                if (numbers[m] == m) {
                    cout << "YES" << "\n";
                }
                
                else {
                    cout << "NO" << "\n";
                }
            }
            
        }
        
        i = i + 1;
    }
    
    
}


