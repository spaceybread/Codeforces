#include <iostream>
#include <math.h>
#include <string>
#include <cmath>
 
using namespace std;

int main() {
    
    int test;
    cin >> test;
    
    int i = 0;
    int n;
    
    while (i < test) {
        cin >> n;
        
        if (n % 2 == 1) {
            n = n - 1;
        }
        
        cout << n/2 << "\n";
        
        i = i + 1;
    }
}
