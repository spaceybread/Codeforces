#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    long long int t;
    cin >> t;
    
    long long int i = 0;
    int a, b, c;

    while (i < t) {
        cin >> a >> b >> c;
        if (a + b == c) {
            cout << "YES" << "\n";
        } else if (b + c == a) {
            cout << "YES" << "\n";
        } else if (a + c == b) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << "\n";
        }
        i = i + 1;
    }
    
}
