#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    
    int r = 0;
    int g = 0;
    int b = 0;
    int sum;
    
    cin >> n;
    
    char table[n];
    
    for (int i = 0; i < n; i++) {
        cin >> table[i];
    }
    
    for (int j = 0; j < n; j++) {
        if (table[j] == 'R' || table[j] == 'G' || table[j] == 'B' ) {
            if (table[j] == 'R' && table[j + 1] == 'R') {
                r = r + 1;
            }
            if (table[j] == 'G' && table[j + 1] == 'G') {
                g = g + 1;
            }
            if (table[j] == 'B' && table[j + 1] == 'B') {
                b = b + 1;
            }
        }
    }
    
    sum = r + g + b;
    cout << sum;
    
    
}
