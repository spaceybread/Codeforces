#ifndef _GLIBCXX_NO_ASSERT
 #include <cassert>
 #endif
 #include <cctype>
 #include <cerrno>
 #include <cfloat>
 #include <ciso646>
 #include <climits>
 #include <clocale>
 #include <cmath>
 #include <csetjmp>
 #include <csignal>
 #include <cstdarg>
 #include <cstddef>
 #include <cstdio>
 #include <cstdlib>
 #include <cstring>
 #include <ctime>
 
 #if __cplusplus >= 201103L
 #include <ccomplex>
 #include <cfenv>
 #include <cinttypes>
 #include <cstdbool>
 #include <cstdint>
 #include <ctgmath>
 #include <cwchar>
 #include <cwctype>
 #endif
 
 // C++
 #include <algorithm>
 #include <bitset>
 #include <complex>
 #include <deque>
 #include <exception>
 #include <fstream>
 #include <functional>
 #include <iomanip>
 #include <ios>
 #include <iosfwd>
 #include <iostream>
 #include <istream>
 #include <iterator>
 #include <limits>
 #include <list>
 #include <locale>
 #include <map>
 #include <memory>
 #include <new>
 #include <numeric>
 #include <ostream>
 #include <queue>
 #include <set>
 #include <sstream>
 #include <stack>
 #include <stdexcept>
 #include <streambuf>
 #include <string>
 #include <typeinfo>
 #include <utility>
 #include <valarray>
 #include <vector>
 
 #if __cplusplus >= 201103L
 #include <array>
 #include <atomic>
 #include <chrono>
 #include <condition_variable>
 #include <forward_list>
 #include <future>
 #include <initializer_list>
 #include <mutex>
 #include <random>
 #include <ratio>
 #include <regex>
 #include <scoped_allocator>
 #include <system_error>
 #include <thread>
 #include <tuple>
 #include <typeindex>
 #include <type_traits>
 #include <unordered_map>
 #include <unordered_set>
 #endif

using namespace std;

int main() {
    
    int t;
    cin >> t;
    
    for (int iter = 0; iter < t; iter++) {
        
        int score = 0;
        
        for (int i = 0; i < 10; i++) {
            string s;
            cin >> s;
            
            for (int j = 0; j < 10; j++) {
                if (s[j] == 'X') {
                    
                    if (i == 0 || i == 9) {
                        score = score + 1;
                    } else if (i == 1 || i == 8) {
                        if (j == 0 || j == 9) {
                            score = score + 1;
                        } else {
                            score = score + 2;
                        }
                    } else if (i == 2 || i == 7) {
                        if (j == 0 || j == 9) {
                            score = score + 1;
                        } else if (j == 1 || j == 8) {
                            score = score + 2;
                        } else  {
                            score = score + 3;
                        }
                    } else if (i == 3 || i == 6) {
                        if (j == 0 || j == 9) {
                            score = score + 1;
                        } else if (j == 1 || j == 8) {
                            score = score + 2;
                        } else if (j == 2 || j == 7) {
                            score = score + 3;
                        } else  {
                            score = score + 4;
                        }
                    } else if (i == 4 || i == 5) {
                        if (j == 0 || j == 9) {
                            score = score + 1;
                        } else if (j == 1 || j == 8) {
                            score = score + 2;
                        } else if (j == 2 || j == 7) {
                            score = score + 3;
                        } else if (j == 3 || j == 6) {
                            score = score + 4;
                        } else  {
                            score = score + 5;
                        }
                    }
                    
                }
            }
            
        }
        cout << score << "\n";
    }
    

}
