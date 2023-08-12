#include<iostream>
#include<math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    long long int i = 0;
    long long int n;
    cin >> n;
    
    long long int val;
    
    while (i < n) {
        cin >> val;
        
        bool isBigger = true;
        bool isPossible = false;
        
        int j = 0;
        
        while (j < 11) {
            
            if (j * 111 > val) {
                cout << "NO" << "\n";
                break;
            }
            
            if ((val - (111 * j)) % 11 == 0) {
                cout << "YES" << "\n";
                break;
            }
            j = j + 1;
            
        }
        
        i = i + 1;
    }
    

}
