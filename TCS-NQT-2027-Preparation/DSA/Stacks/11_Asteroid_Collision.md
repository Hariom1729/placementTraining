# Problem 11: Asteroid Collision

## Problem Statement
We are given an array `asteroids` of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Input Format
- An array of integers `asteroids`.

## Output Format
- An array of integers representing the final state.

## Constraints
- `2 <= asteroids.length <= 10^4`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`

---

## Approach

We can use a stack to simulate the collisions. A collision ONLY happens when the asteroid at the top of the stack is moving RIGHT (`> 0`) and the incoming asteroid is moving LEFT (`< 0`).

1. Iterate through each `ast` in the array.
2. If `ast > 0` (moving right), simply push it to the stack (it can never collide with elements already in the stack).
3. If `ast < 0` (moving left):
   - While the stack is not empty, and the top is moving right (`st.top() > 0`), and the top is smaller than the current asteroid (`st.top() < abs(ast)`), pop the stack (top asteroid explodes).
   - If the stack becomes empty or the top is also moving left (`st.top() < 0`), push the current asteroid.
   - If the top is equal in size (`st.top() == abs(ast)`), pop the stack and DO NOT push the current asteroid (both explode).
4. Extract the elements from the stack and reverse them to get the final array.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> st;
        
        for (int ast : asteroids) {
            bool exploded = false;
            
            while (!st.empty() && ast < 0 && st.top() > 0) {
                if (st.top() < abs(ast)) {
                    st.pop(); // Top asteroid explodes, incoming might still collide
                    continue;
                } else if (st.top() == abs(ast)) {
                    st.pop(); // Both explode
                    exploded = true;
                    break;
                } else {
                    exploded = true; // Incoming asteroid explodes
                    break;
                }
            }
            
            if (!exploded) {
                st.push(ast);
            }
        }
        
        vector<int> res(st.size());
        for (int i = res.size() - 1; i >= 0; i--) {
            res[i] = st.top();
            st.pop();
        }
        
        return res;
    }
};

int main() {
    Solution sol;
    vector<int> asteroids = {5, 10, -5};
    vector<int> result = sol.asteroidCollision(asteroids);
    
    cout << "Final State: ";
    for(int x : result) cout << x << " "; 
    // Expected: 5 10 (10 destroys -5)
    cout << endl;
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Each asteroid is pushed and popped at most once.
- **Space Complexity:** `O(N)` for the stack.
