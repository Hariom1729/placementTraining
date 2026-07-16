# Word Search

## Difficulty
Medium-Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Related Companies: Amazon, Microsoft, Intuit

## Topic
Arrays (Matrix)

## Pattern
Backtracking (DFS)

## Problem Statement
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Constraints
- $m == board.length$
- $n = board[i].length$
- $1 \le m, n \le 6$
- $1 \le word.length \le 15$
- `board` and `word` consist of only lowercase and uppercase English letters.

## Input Format
- First line: `M N`
- Next `M` lines: Strings representing the board.
- Last line: `word`

## Output Format
- Return boolean `true` or `false`.

## Sample Input
```
3 4
A B C E
S F C S
A D E E
ABCCED
```

## Sample Output
```
true
```

## Edge Cases
- Word length is larger than the total number of characters in the board.
- The board contains only one character.

## Approach 1
Optimal Approach (DFS + Backtracking)
**Explanation:** 
We must find the word by exploring all possible paths starting from any cell that matches the first letter of the word.
1. Iterate over every cell `(i, j)` in the grid.
2. If `board[i][j] == word[0]`, start a DFS search from there.
3. In the DFS function:
   - If the index of the character we are looking for equals `word.length`, we found the whole word! Return `true`.
   - Check boundaries: If `i` or `j` are out of bounds, or if `board[i][j] != word[index]`, return `false`.
   - Mark the current cell as visited. Since we can't use extra space, temporarily modify the board cell (e.g., `board[i][j] = '*'`).
   - Recursively call DFS in all 4 directions (up, down, left, right) for `index + 1`.
   - If any of the recursive calls return `true`, return `true`.
   - **Backtrack:** Restore the original character to `board[i][j]`.
4. If the nested loops finish without finding the word, return `false`.

**Time Complexity:** $O(M \times N \times 4^L)$, where $L$ is the length of the word.
**Space Complexity:** $O(L)$ for the recursion stack.

## Java Solution
```java
class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word.charAt(0) && dfs(board, i, j, 0, word)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    private boolean dfs(char[][] board, int i, int j, int index, String word) {
        if (index == word.length()) return true;
        
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != word.charAt(index)) {
            return false;
        }
        
        char temp = board[i][j];
        board[i][j] = '*'; // Mark as visited
        
        boolean found = dfs(board, i + 1, j, index + 1, word) ||
                        dfs(board, i - 1, j, index + 1, word) ||
                        dfs(board, i, j + 1, index + 1, word) ||
                        dfs(board, i, j - 1, index + 1, word);
                        
        board[i][j] = temp; // Backtrack
        
        return found;
    }
}
```

## Python Solution
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False
                
            temp = board[i][j]
            board[i][j] = '*'
            
            res = (dfs(i+1, j, index+1) or
                   dfs(i-1, j, index+1) or
                   dfs(i, j+1, index+1) or
                   dfs(i, j-1, index+1))
                   
            board[i][j] = temp
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
                    
        return False
```

## C++ Solution
```cpp
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (board[i][j] == word[0] && dfs(board, i, j, 0, word)) {
                    return true;
                }
            }
        }
        return false;
    }
    
private:
    bool dfs(vector<vector<char>>& board, int i, int j, int index, string& word) {
        if (index == word.length()) return true;
        
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != word[index]) {
            return false;
        }
        
        char temp = board[i][j];
        board[i][j] = '*';
        
        bool found = dfs(board, i + 1, j, index + 1, word) ||
                     dfs(board, i - 1, j, index + 1, word) ||
                     dfs(board, i, j + 1, index + 1, word) ||
                     dfs(board, i, j - 1, index + 1, word);
                     
        board[i][j] = temp;
        
        return found;
    }
};
```

## Common Mistakes
- **Forgetting to Backtrack:** If you just mark `board[i][j] = '*'`, and the DFS path fails, you must restore it before the function returns. Otherwise, other paths starting from different cells won't be able to use that character.
- **Using a separate `visited` array:** While technically correct, allocating a $O(M \times N)$ boolean array is unnecessary space overhead. In-place modification is the expected optimal solution.

## Similar Questions
- Word Search II (Requires Trie)
