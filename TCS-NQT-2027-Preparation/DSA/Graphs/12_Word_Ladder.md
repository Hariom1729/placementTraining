# Problem 12: Word Ladder

## Problem Statement
A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s_1 -> s_2 -> ... -> s_k` such that:
- Every adjacent pair of words differs by a single letter.
- Every `s_i` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `s_k == endWord`
Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.

## Constraints
- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 5000`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.

---

## Approach: BFS

This is a shortest path problem in an unweighted graph where nodes are words, and an edge exists if two words differ by exactly one character.
To find the shortest path in an unweighted graph, we use **BFS**.

1. Put all words from `wordList` into an `unordered_set` for `O(1)` lookups.
2. Use a `queue<pair<string, int>> q` storing the word and the current sequence length.
3. Push `{beginWord, 1}` to `q`. Remove `beginWord` from the set.
4. While queue is not empty:
   - Pop `{word, steps}`.
   - If `word == endWord`, return `steps`.
   - Iterate through every character of `word`:
     - Change it to every letter from `'a'` to `'z'`.
     - If the new word exists in the set:
       - Push it to the queue with `steps + 1`.
       - Erase it from the set so we don't visit it again.
5. If the queue is empty and we haven't found `endWord`, return `0`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> st(wordList.begin(), wordList.end());
        
        // If endWord is not in the dictionary
        if (st.find(endWord) == st.end()) return 0;
        
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        st.erase(beginWord);
        
        while (!q.empty()) {
            string word = q.front().first;
            int steps = q.front().second;
            q.pop();
            
            if (word == endWord) return steps;
            
            // Try changing each character of the word
            for (int i = 0; i < word.length(); i++) {
                char original = word[i];
                
                for (char c = 'a'; c <= 'z'; c++) {
                    word[i] = c;
                    
                    if (st.find(word) != st.end()) {
                        q.push({word, steps + 1});
                        st.erase(word); // Mark as visited
                    }
                }
                
                // Restore original character for next iteration
                word[i] = original;
            }
        }
        
        return 0;
    }
};

int main() {
    Solution sol;
    string beginWord = "hit";
    string endWord = "cog";
    vector<string> wordList = {"hot","dot","dog","lot","log","cog"};
    
    cout << "Shortest sequence length: " << sol.ladderLength(beginWord, endWord, wordList) << endl; 
    // Expected: 5 (hit -> hot -> dot -> dog -> cog)

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N * M * 26)` where `N` is the length of `wordList` and `M` is the length of each word. We check `26 * M` variations for each popped word.
- **Space Complexity:** `O(N * M)` to store the words in the set and queue.
