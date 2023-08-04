#include<iostream>
#include<math.h>
#include <string>

using namespace std;

string repeat(string s, int n)
{
    string s1 = s;
  
    for (int i=1; i<n;i++)
        s += s1;
  
    return s;
}


int main() {
    
    long long int n;
    long long int zero = 0;
    long long int two = 2;
    long long int one = 1;
    cin >> n;
    
    string starterOdd = "I hate it";
    string starterEven = "I hate that I love it";
    string even = "I hate that I love that ";
    
    string enderOdd = "I hate that I love that ";
    
    
    if (n == one) {
        cout << starterOdd;
    }
    
    else if (n == two) {
        cout << starterEven;
    }
    
    else if (n % two == zero && n != two) {
        n = n/two - one;
        cout << repeat (even, n);
        cout << starterEven;
    }
    
    else if (n % two == one && n != one) {
        n = (n - one)/two;
        cout << repeat (enderOdd, n);
        cout << starterOdd;
    }
    
}

