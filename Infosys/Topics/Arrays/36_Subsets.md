# Subsets

## Difficulty
Medium

## Probability
★★★★☆

## Asked In
Infosys SP
Related Companies: Amazon, Meta, Microsoft

## Topic
Arrays / Recursion

## Pattern
Backtracking / Power Set

## Problem Statement
Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in **any order**.

## Constraints
- $1 \le nums.length \le 10$
- $-10 \le nums[i] \le 10$
- All the numbers of `nums` are unique.

## Input Format
- First line: `N`
- Second line: `N` space-separated integers.

## Output Format
- Return a 2D array representing all subsets.

## Sample Input
```
3
1 2 3
```

## Sample Output
```
[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

## Edge Cases
- Empty array.
- Array with a single element.

## Approach 1
Iterative Cascading
**Explanation:** Start with an empty subset `[[]]`. For every number in the array, take all existing subsets, copy them, append the new number to each copy, and add them back to the list of subsets.
**Time Complexity:** $O(N \times 2^N)$
**Space Complexity:** $O(N \times 2^N)$ to hold all subsets.

## Approach 2
Optimal Approach (Backtracking / DFS)
**Explanation:** 
Backtracking is the most elegant way to generate combinations and subsets. We explore a decision tree where at each element, we have two choices: either **include** the element in our current subset, or **exclude** it.
1. Create a `result` list of lists.
2. Define a recursive helper function `backtrack(index, current_subset)`.
3. Base Case: If `index == nums.length`, we have made a decision for every element. Add a copy of `current_subset` to `result` and return.
4. Recursive Step 1 (Include): Add `nums[index]` to `current_subset`. Call `backtrack(index + 1, current_subset)`.
5. **Backtrack:** Remove the recently added element from `current_subset`.
6. Recursive Step 2 (Exclude): Call `backtrack(index + 1, current_subset)`.

**Time Complexity:** $O(N \times 2^N)$ because there are $2^N$ subsets, and copying each subset takes $O(N)$ time.
**Space Complexity:** $O(N)$ for the recursion stack (ignoring the space to store the output).

## Java Solution
```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(0, nums, new ArrayList<>(), result);
        return result;
    }
    
    private void backtrack(int index, int[] nums, List<Integer> current, List<List<Integer>> result) {
        if (index == nums.length) {
            result.add(new ArrayList<>(current)); // Deep copy
            return;
        }
        
        // Include
        current.add(nums[index]);
        backtrack(index + 1, nums, current, result);
        
        // Backtrack
        current.remove(current.size() - 1);
        
        // Exclude
        backtrack(index + 1, nums, current, result);
    }
}
```

## Python Solution
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(index, current):
            if index == len(nums):
                res.append(current.copy())
                return
                
            # Include
            current.append(nums[index])
            backtrack(index + 1, current)
            
            # Backtrack
            current.pop()
            
            # Exclude
            backtrack(index + 1, current)
            
        backtrack(0, [])
        return res
```

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(0, nums, current, result);
        return result;
    }
    
private:
    void backtrack(int index, vector<int>& nums, vector<int>& current, vector<vector<int>>& result) {
        if (index == nums.size()) {
            result.push_back(current);
            return;
        }
        
        // Include
        current.push_back(nums[index]);
        backtrack(index + 1, nums, current, result);
        
        // Backtrack
        current.pop_back();
        
        // Exclude
        backtrack(index + 1, nums, current, result);
    }
};
```

## Common Mistakes
- **Forgetting to deep copy:** When adding `current` to `result`, you MUST create a new copy of `current` (e.g., `new ArrayList<>(current)`). If you just add `current` by reference, later backtracking modifications will mutate the list that is already inside `result`, resulting in a final list of empty lists.

## Similar Questions
- Subsets II (Contains duplicates)
- Permutations
- Combinations
