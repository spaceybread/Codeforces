#include <iostream>
using namespace std;

int main() {
    string s;
    char c;
    bool isCaps = true;
    
    cin >> s;
    
    for (int i = 1; i < s.length(); i++) {
        if (islower(s[i])) {
            isCaps = false;
        }
    }
    
    if (isCaps == true) {
        for (int j = 0; j < s.length(); j++) {
            if (islower(s[j])) {
                c = toupper(s[j]);
            } else {
                c = tolower(s[j]);
            }
            cout << c;
        }
    } else {
        cout << s;
    }
}
