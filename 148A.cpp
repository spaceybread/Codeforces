#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    int k, l, m, n, d;
    
    cin >> k;
    cin >> l;
    cin >> m;
    cin >> n;
    cin >> d;
    
    int count = d;
    
    if (k == 1 || l == 1 || m == 1 || n == 1) {
        cout << d << "\n";
    }
    else {
        for (int i = 1; i < d + 1; i++ ) {
            
            if((i%k != 0) && (i%l != 0) && (i%m != 0) && (i%n != 0)){
                count--;
            }
        }
        
        cout << count << "\n";
        
        
    }

}
