#include<iostream>
#include<math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    long long int n;
    long long int i = 0;
    
    cin >> n;
    
    long long int sum = 0;
    long long int in = 0;
    
    while (i < n) {
        cin >> in;
        
        sum = sum + in;
        
        i = i + 1;
    }
    
    if (sum != 0) {
        cout << "HARD";
    } else {
        cout << "EASY";
    }   
}



