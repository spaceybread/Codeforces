#include <iostream>
#include <math.h>
#include <string>
#include <cmath>
 
using namespace std;
 
int main() {
    string inLine;
    
    cin >> inLine;
    
    int i = 0;
    
    while (i < inLine.size()) {
        
        if (inLine[i] == '.') {
            cout << 0;
            i = i + 1;
            
        } else if (inLine[i] == '-') {
            i = i + 1;
            if (inLine[i] == '-') {
                cout << 2;
            } else {
                cout << 1;
            }
            i = i + 1;
        }
        
        
        
    }
}
    
