#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    string inLine = "";
    int i = 0;
    
    cin >> inLine;
    
    while (i < inLine.size()) {
        if (inLine[i] == 'W' && inLine[i + 1] == 'U' && inLine[i + 2] == 'B') {
            i = i + 2;
            cout << " ";
            
        } else {
            cout << inLine[i];
        }
        
        i = i + 1;
    }
    
}
