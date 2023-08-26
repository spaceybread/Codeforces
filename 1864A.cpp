#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    int t;
    cin >> t;
    
    for (int iter = 0; iter < t; iter++){
        int x, y, n;
        cin >> x >> y >> n;
        
        int num[n];
        
        num[0] = x;
        num[n - 1] = y;
        
        int j = 1;
        
        for (int i = n - 2; i > 0; i--) {
            num[i] = num[i + 1] - j;
            j = j + 1;
        }
        
        if ((num[1] - num[0]) > (num[2] - num[1])) {
            for (int i = 0; i < n; i++) {
                cout << num[i] << " ";
            }
        } else {
            cout << "-1";
        }
        cout << "\n";
        
    }
}
