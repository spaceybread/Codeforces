#include <iostream>
#include <math.h>
#include <string>
#include <cmath>
 
using namespace std;
 
int main() {
    int h3[1000];
    
    int i = 0;
    int j = 1;
    
    int test;
    
    while (i < 1000) {
        if (!(j % 3 == 0 || j % 10 == 3)) {
            h3[i] = j;
            i = i + 1;
        }
        j = j + 1;
        
    }
    
    i = 0;
    
    cin >> test;
    
    int n;
    
    while (i < test) {
        cin >> n;
        cout << h3[n - 1] << "\n";
        i = i + 1;
    }
}
    
