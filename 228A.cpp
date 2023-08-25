#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    int h1, h2, h3, h4;
    
    cin >> h1 >> h2 >> h3 >> h4;
    
    int colors = 4;
    
    if (h1 == h2 || h1 == h3 || h1 == h4) {
        colors--;
    }
    
    if (h2 == h3 || h2 == h4) {
        colors--;
    }
    
    if (h3 == h4) {
        colors--;
    }
    
    cout << 4 - colors << "\n";
    
}
