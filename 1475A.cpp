#include <iostream>

using namespace std;


int main() {

    long long int t;

    cin >> t;

    for (int i = 0; i < t; i++) {
    long long int n; 
    
    cin >> n;
    
    while (n % 2 == 0) {
      n = n / 2;
    }

    if (n != 1) {
      cout << "YES \n";
    } else {
      cout << "NO \n";
    }
  }


    return 0;
}
