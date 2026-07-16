# Minimum Number of Jumps to Reach End

## Difficulty
Hard

## Asked In
Infosys SP
Year: 2022, 2023
Frequency: High

---

## Problem Statement
Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps. You can assume that you can always reach the last index.

---

## Input Format
- The first line contains an integer `N`.
- The second line contains `N` space-separated integers.

---

## Output Format
- Return the minimum number of jumps required to reach the end.

---

## Constraints
- $1 \le nums.length \le 10^4$
- $0 \le nums[i] \le 1000$

---

## Examples

### Example 1
**Input:** 
```
5
2 3 1 1 4
```
**Output:** 
```
2
```
**Explanation:** The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

### Example 2
**Input:** 
```
5
2 3 0 1 4
```
**Output:** 
```
2
```

---

## Brute Force Approach
Use Recursion. From every index, try all possible jumps from `1` to `nums[i]` and find the minimum jumps among all paths.

**Time Complexity:** $O(N^N)$ (Exponential, will strictly TLE).
**Space Complexity:** $O(N)$ for recursion stack.

---

## Better Approach (Dynamic Programming)
Use a 1D DP array where `dp[i]` stores the minimum jumps required to reach index `i` from the start.
`dp[i] = min(dp[i], dp[j] + 1)` for all `j < i` if you can jump from `j` to `i`.

**Complexity:** 
- **Time Complexity:** $O(N^2)$
- **Space Complexity:** $O(N)$ for the DP array.

---

## Optimal Approach (Greedy BFS)
**Detailed explanation:**
We can solve this in $O(N)$ time using a Greedy approach that acts like a BFS.
We maintain three variables:
1. `jumps`: The number of jumps taken so far.
2. `current_end`: The farthest index we can reach with the current number of jumps.
3. `farthest`: The farthest index we can reach from all the nodes we have traversed so far.

Iterate through the array (excluding the last element):
- Update `farthest = max(farthest, i + nums[i])`.
- If we reach the `current_end` (i.e., `i == current_end`), it means we must take a jump now. We increment `jumps`, and update `current_end = farthest`.

**Dry Run:**
`nums = [2, 3, 1, 1, 4]`
- Init: `jumps = 0`, `current_end = 0`, `farthest = 0`
- `i = 0` (val 2): `farthest = max(0, 0+2) = 2`. `i == current_end` (0 == 0), so `jumps = 1`, `current_end = 2`.
- `i = 1` (val 3): `farthest = max(2, 1+3) = 4`.
- `i = 2` (val 1): `farthest = max(4, 2+1) = 4`. `i == current_end` (2 == 2), so `jumps = 2`, `current_end = 4`.
- Loop ends (since we only go up to `N-2`).
- Return `jumps` = 2.

**Complexity:**
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$

---

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int jump(vector<int>& nums) {
    int n = nums.size();
    if (n <= 1) return 0; // Already at end
    
    int jumps = 0;
    int current_end = 0;
    int farthest = 0;
    
    // We don't need to visit the last index
    for (int i = 0; i < n - 1; i++) {
        farthest = max(farthest, i + nums[i]);
        
        // If we reach the limit of our current jump
        if (i == current_end) {
            jumps++;
            current_end = farthest;
            
            // If the current end reaches or exceeds the last index, we can stop
            if (current_end >= n - 1) {
                break;
            }
        }
    }
    
    return jumps;
}

int main() {
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << "Min Jumps: " << jump(nums) << endl; // Output: 2
    return 0;
}
```

---

## Common Mistakes
- **Looping to the very end:** The loop should only run up to `n - 2`. If you run it to `n - 1`, and `current_end` happens to land exactly on `n - 1`, the logic will trigger an unnecessary extra jump at the very last index.
- **Returning too early:** Don't return `jumps` inside the loop without fully updating.

---

## Similar Questions
- Jump Game I (Check if you can reach the end: Boolean).
- Jump Game III (Jump forward and backward).

---

## Interview Tips
- This problem is the classic transition from $O(N^2)$ DP to $O(N)$ Greedy. Interviewers love this problem for SP L2/L3 roles to test if you can recognize when Greedy outperforms DP.

---

## Pattern Recognition
**Identify this when:** You are asked to find the *minimum* number of steps/jumps in an array, and you have choices of how far to move. This is the **Greedy Reachability** pattern.
