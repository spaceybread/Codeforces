#include <iostream>
#include <math.h>
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
    
    long long int a, b;
    bool looper = true;
    
    if (n % 2 == 0) {
        a = n/2;
        b = n/2;
        
        while (looper == true) {
            if (numbers[a] == 0 and numbers[b] == 0) {
                looper = false;
            } else {
                a = a - 1;
                b = b + 1;
            }
        }
        
    } else {
        a = n/2;
        b = n/2 + 1;
        
        while (looper == true) {
            if (numbers[a] == 0 and numbers[b] == 0) {
                looper = false;
            } else {
                a = a - 1;
                b = b + 1;
            }
        }
        
    }
    
    cout << a << " " << b << "\n";
    
}
