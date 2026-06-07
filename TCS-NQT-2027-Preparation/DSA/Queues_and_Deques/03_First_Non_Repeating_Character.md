# Problem 3: First Non-Repeating Character in a Stream

## Problem Statement
Given a stream of characters (a string `s` passed character by character), find the first non-repeating character each time a character is inserted to the stream.
If no non-repeating character exists, append '#' to the answer.

## Input Format
- A string `s` representing the stream of characters.

## Output Format
- A string representing the sequence of first non-repeating characters.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

---

## Approach: Queue + Frequency Array

As characters arrive in a stream, we need to keep track of their order of arrival (FIFO) and their frequency.
1. Use an array `freq[26]` to store the frequency of each character.
2. Use a `queue<char> q` to keep track of the order of characters.
3. For each incoming character `c` in the stream:
   - Increment its frequency: `freq[c - 'a']++`.
   - Push `c` into the queue.
   - Now, check the front of the queue. If the character at the front has a frequency greater than `1` (it repeats), pop it from the queue. We keep popping until we find a character with a frequency of `1`, or until the queue is empty.
   - If the queue is empty, there is no non-repeating character, append `#`.
   - If not empty, the front of the queue is the first non-repeating character, append it.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

class Solution {
public:
    string FirstNonRepeating(string A) {
        vector<int> freq(26, 0);
        queue<char> q;
        string result = "";
        
        for (char c : A) {
            // 1. Update frequency and add to queue
            freq[c - 'a']++;
            q.push(c);
            
            // 2. Remove repeating characters from the front of the queue
            while (!q.empty() && freq[q.front() - 'a'] > 1) {
                q.pop();
            }
            
            // 3. Append the answer
            if (q.empty()) {
                result += '#';
            } else {
                result += q.front();
            }
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    string stream = "aabc";
    cout << "Stream: " << stream << "\nResult: " << sol.FirstNonRepeating(stream) << endl; 
    // a -> 'a'
    // a -> '#' (queue front 'a' repeats, popped. queue empty)
    // b -> 'b'
    // c -> 'b' (b is still the first non-repeating)
    // Expected: a#bb
    
    string stream2 = "zz";
    cout << "Stream: " << stream2 << "\nResult: " << sol.FirstNonRepeating(stream2) << endl; 
    // Expected: z#
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)`. Each character is pushed into the queue once and popped at most once.
- **Space Complexity:** `O(N)` for the queue in the worst case (all unique characters), plus `O(26)` for the frequency array which is `O(1)`.
