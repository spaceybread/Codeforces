#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
    
    int n;
    cin >> n;
    
    map<string, int> regi;
    string s;
    
    while (n > 0) {
        cin >> s;
        
        if (regi.count(s) == 0) {
            cout << "OK" << "\n";
            regi[s] = 1;
        } else {
            cout << s << regi[s] << "\n";
            regi[s] = regi[s] + 1;
        }
        
        n = n - 1;
        
    }
}

