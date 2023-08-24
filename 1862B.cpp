#include <iostream>
#include <math.h>
#include <string>
#include <cmath>
 
using namespace std;

int main() {
    
    long long int t;
    long long int tint = 0;
    
    cin >> t;
    
    while (tint < t) {
        
        long long int n;
        
        cin >> n;
        
        long long int list[n];
        
        long long int i = 0;
        
        while (i < n) {
            cin >> list[i];
            i = i + 1;
        }
        
        i = 1;
        long long int j = 1;
        long long int newList[2*n];
        
        newList[0] = list[0];
        
        while (i < n) {
            if (list[i] >= list[i - 1]) {
                newList[j] = list[i];
            } else {
                newList[j] = list[i];
                j = j + 1;
                newList[j] = list[i];
            }
            i = i + 1;
            j = j + 1;
            
        }
        
        long long int newJ = 0;
        
        cout << j << "\n";
        
        while (newJ < j) {
            cout << newList[newJ] << " ";
            newJ = newJ + 1;
        }
        cout << "\n";
    
        tint = tint + 1;
    }
    
}
