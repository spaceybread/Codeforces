#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    int y, w;
    cin >> y >> w;
    
    if (y > w) {
        if (y == 6) {
            cout << "1/6";
        } else if (y == 5) {
            cout << "1/3";
        } else if (y == 4) {
            cout << "1/2";
        } else if (y == 3) {
            cout << "2/3";
        } else if (y == 2) {
            cout << "5/6";
        } else if (y == 1) {
            cout << "1/1";
        }
    } else {
        if (w == 6) {
            cout << "1/6";
        } else if (w == 5) {
            cout << "1/3";
        } else if (w == 4) {
            cout << "1/2";
        } else if (w == 3) {
            cout << "2/3";
        } else if (w == 2) {
            cout << "5/6";
        } else if (w == 1) {
            cout << "1/1";
        }
        
    }
    cout << "\n";
}
