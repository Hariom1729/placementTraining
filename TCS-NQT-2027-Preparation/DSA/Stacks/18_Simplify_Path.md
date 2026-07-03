# Simplify Path

## Problem Statement
Given a string `path`, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system:
- A single period `.` refers to the current directory.
- A double period `..` refers to the directory up a level.
- Multiple consecutive slashes (e.g., `//`) are treated as a single slash `/`.

**Example:**
- **Input:** path = "/a/./b/../../c/"
- **Output:** "/c"
- **Explanation:** `/a` -> stay in `/a` -> go into `b` (`/a/b`) -> go up to `a` -> go up to root `/` -> go into `c`.

## Optimal Approach (Using Stack)
Split the path by slashes. Ignore empty strings and `.`. If you encounter `..`, pop from the stack (if not empty). Otherwise, push the directory name to the stack. Finally, reconstruct the path from the stack.

### C++ Code
```cpp
#include <iostream>
#include <string>
#include <stack>
#include <sstream>
#include <vector>
using namespace std;

string simplifyPath(string path) {
    stack<string> st;
    stringstream ss(path);
    string token;
    
    // Split string by '/'
    while (getline(ss, token, '/')) {
        if (token == "" || token == ".") continue;
        if (token == "..") {
            if (!st.empty()) st.pop();
        } else {
            st.push(token);
        }
    }
    
    string result = "";
    if (st.empty()) return "/";
    
    while (!st.empty()) {
        result = "/" + st.top() + result;
        st.pop();
    }
    
    return result;
}

int main() {
    cout << simplifyPath("/a/./b/../../c/") << endl; // Output: /c
    return 0;
}
```

### Complexity
- **Time Complexity:** $O(N)$, to traverse and parse the path.
- **Space Complexity:** $O(N)$, for storing directory names in the stack.
