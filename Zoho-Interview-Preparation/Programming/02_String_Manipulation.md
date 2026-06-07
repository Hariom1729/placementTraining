# Programming: String Manipulation

Zoho prohibits using built-in methods like `find()`, or `reverse()`. You must manipulate the underlying character arrays/strings.

## 1. Substring Search without `find`
**Problem:** Find the index of the first occurrence of a substring in a string.
**C++ Solution:**
```cpp
#include <iostream>
#include <string>

using namespace std;

int strStr(string haystack, string needle) {
    if(needle.length() == 0) return 0;
    
    for(int i = 0; i <= (int)(haystack.length() - needle.length()); i++) {
        int j = 0;
        while(j < needle.length() && haystack[i + j] == needle[j]) {
            j++;
        }
        if(j == needle.length()) return i;
    }
    return -1;
}

int main() {
    cout << strStr("hello world", "world") << "\n"; // 6
    return 0;
}
```

## 2. Reverse Words in a String without `split`
**Problem:** Reverse the order of words in a sentence.
**C++ Solution:**
```cpp
#include <iostream>
#include <string>

using namespace std;

void reverseStr(string& s, int left, int right) {
    while (left < right) {
        swap(s[left], s[right]);
        left++; right--;
    }
}

int main() {
    string s = "I love programming";
    
    // Step 1: Reverse entire string
    reverseStr(s, 0, s.length() - 1);
    
    // Step 2: Reverse each word
    int start = 0;
    for (int end = 0; end <= s.length(); end++) {
        if (end == s.length() || s[end] == ' ') {
            reverseStr(s, start, end - 1);
            start = end + 1;
        }
    }
    cout << s << "\n"; // "programming love I"
    return 0;
}
```

## 3. Run Length Encoding
**Problem:** Compress a string. "aabcccccaaa" -> "a2b1c5a3".
**C++ Solution:**
```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
    string str = "aabcccccaaa";
    string compressed = "";
    int countConsecutive = 0;
    
    for (int i = 0; i < str.length(); i++) {
        countConsecutive++;
        if (i + 1 >= str.length() || str[i] != str[i + 1]) {
            compressed += str[i];
            compressed += to_string(countConsecutive);
            countConsecutive = 0;
        }
    }
    cout << compressed << "\n";
    return 0;
}
```

## 4. Expand String
**Problem:** Given "a1b10", expand it to "abbbbbbbbbb".
**C++ Solution:**
```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
    string s = "a1b10c3";
    for (int i = 0; i < s.length(); i++) {
        if (isalpha(s[i])) {
            char c = s[i];
            int count = 0;
            i++;
            while (i < s.length() && isdigit(s[i])) {
                count = count * 10 + (s[i] - '0');
                i++;
            }
            i--; // Step back
            for (int k = 0; k < count; k++) {
                cout << c;
            }
        }
    }
    cout << "\n";
    return 0;
}
```
