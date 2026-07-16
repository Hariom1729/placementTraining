# Subsets II

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Related Companies: Amazon, Microsoft, ByteDance

## Topic
Arrays / Recursion

## Pattern
Backtracking (with Deduplication)

## Problem Statement
Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in **any order**.

## Constraints
- $1 \le nums.length \le 10$
- $-10 \le nums[i] \le 10$

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.

## Output Format
- Return a 2D array representing all unique subsets.

## Sample Input
```
3
1 2 2
```

## Sample Output
```
[[],[1],[1,2],[1,2,2],[2],[2,2]]
```

## Edge Cases
- All elements are the same (e.g., `[2, 2, 2]`).

## Approach 1
Brute Force
**Explanation:** Generate all subsets exactly like the standard Subsets problem. Convert each subset to a string/tuple and insert it into a Hash Set to remove duplicates.
**Time Complexity:** $O(N \times 2^N)$
**Space Complexity:** $O(N \times 2^N)$ for the set.

## Approach 2
Optimal Approach (Sorting + Backtracking)
**Explanation:** 
To avoid generating duplicate subsets, we can sort the array first. Sorting ensures that all duplicate elements are adjacent.
During our backtracking decision tree, if we decide to **exclude** a number `nums[i]`, we must also implicitly exclude ALL subsequent occurrences of `nums[i]` at this specific depth of the decision tree. If we don't, including the *next* duplicate `nums[i]` will result in the exact same subset we just generated.

1. Sort `nums`.
2. Recursive function `backtrack(index, current)`.
3. Add `current` to `result` immediately at the start of the function call (this handles all intermediate subsets).
4. Loop `i` from `index` to `n-1`.
5. **Deduplication Check:** `if (i > index && nums[i] == nums[i - 1]) continue;`
6. Include `nums[i]`, recurse `backtrack(i + 1, current)`, and backtrack.

**Dry Run:**
`nums = [1, 2, 2]`
- `backtrack(0, [])` -> Add `[]`.
- `i=0` (1): `curr=[1]`. `backtrack(1, [1])` -> Add `[1]`.
  - `i=1` (2): `curr=[1,2]`. `backtrack(2, [1,2])` -> Add `[1,2]`.
    - `i=2` (2): `curr=[1,2,2]`. `backtrack(3, [1,2,2])` -> Add `[1,2,2]`. Backtrack.
  - Backtrack. `curr=[1]`.
  - `i=2` (2): `i(2) > index(1)` AND `nums[2] == nums[1]`. **SKIP!** (Prevents duplicate `[1,2]`).
- Backtrack. `curr=[]`.
- `i=1` (2): `curr=[2]`. `backtrack(2, [2])` -> Add `[2]`.
  - `i=2` (2): `curr=[2,2]`. `backtrack(3, [2,2])` -> Add `[2,2]`. Backtrack.
- Backtrack. `curr=[]`.
- `i=2` (2): `i(2) > index(0)` AND `nums[2] == nums[1]`. **SKIP!** (Prevents duplicate `[2]`).

**Time Complexity:** $O(N \times 2^N)$
**Space Complexity:** $O(N)$ for the recursion stack.

## Java Solution
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums); // Crucial for deduplication
        backtrack(0, nums, new ArrayList<>(), result);
        return result;
    }
    
    private void backtrack(int index, int[] nums, List<Integer> current, List<List<Integer>> result) {
        result.add(new ArrayList<>(current));
        
        for (int i = index; i < nums.length; i++) {
            // Skip duplicates at the same tree depth
            if (i > index && nums[i] == nums[i - 1]) {
                continue;
            }
            
            current.add(nums[i]);
            backtrack(i + 1, nums, current, result);
            current.remove(current.size() - 1);
        }
    }
}
```

## Python Solution
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(index, current):
            res.append(current.copy())
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                    
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
                
        backtrack(0, [])
        return res
```

## C++ Solution
```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        sort(nums.begin(), nums.end());
        backtrack(0, nums, current, result);
        return result;
    }
    
private:
    void backtrack(int index, vector<int>& nums, vector<int>& current, vector<vector<int>>& result) {
        result.push_back(current);
        
        for (int i = index; i < nums.size(); i++) {
            if (i > index && nums[i] == nums[i - 1]) {
                continue;
            }
            
            current.push_back(nums[i]);
            backtrack(i + 1, nums, current, result);
            current.pop_back();
        }
    }
};
```

## Common Mistakes
- **Forgetting to Sort:** The deduplication logic `nums[i] == nums[i-1]` completely fails if the duplicates are not adjacent. You MUST sort the array first.
- **Incorrect Deduplication Logic:** `if (i > 0 && nums[i] == nums[i-1])` is WRONG. It must be `i > index` because you are only skipping duplicates horizontally across the branches of the *current depth* of the tree, not vertically down a specific path.

## Similar Questions
- Subsets
- Combination Sum II
