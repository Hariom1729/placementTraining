# Rotate Array by K Elements

## Difficulty
Easy

## Asked In
Infosys SP
Infosys DSE
Year: 2021, 2023
Frequency: High

---

## Problem Statement
Given an array `arr` of size `N`, rotate the array to the right by `K` steps, where `K` is non-negative.

---

## Input Format
- The first line contains an integer `N`, the size of the array.
- The second line contains `N` space-separated integers representing the array elements.
- The third line contains an integer `K`, the number of steps to rotate.

---

## Output Format
- Return the modified array after rotation.

---

## Constraints
- $1 \le N \le 10^5$
- $0 \le K \le 10^5$
- $-10^9 \le arr[i] \le 10^9$

---

## Examples

### Example 1
**Input:** 
```
7
1 2 3 4 5 6 7
3
```
**Output:** 
```
5 6 7 1 2 3 4
```

### Example 2
**Input:** 
```
4
-1 -100 3 99
2
```
**Output:** 
```
3 99 -1 -100
```

---

## Brute Force Approach
Create a new temporary array. Iterate through the original array and place the element at index `i` into the new array at index `(i + K) % N`. Finally, copy the temporary array back to the original array.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$ for the temporary array.

---

## Better Approach
If rotation by one element takes $O(N)$ time, we can rotate the array one by one $K$ times.

**Complexity:** 
- **Time Complexity:** $O(N \times K)$, which will give Time Limit Exceeded (TLE) for large $N$ and $K$.
- **Space Complexity:** $O(1)$.

---

## Optimal Approach (Reversal Algorithm)
**Detailed explanation:**
We can achieve this in-place using the Reversal Algorithm:
1. Since $K$ can be greater than $N$, we take $K = K \pmod N$.
2. Reverse the entire array from `0` to `N-1`.
3. Reverse the first `K` elements from `0` to `K-1`.
4. Reverse the remaining `N-K` elements from `K` to `N-1`.

**Dry Run:**
Given array: `[1, 2, 3, 4, 5, 6, 7]`, $K = 3$
- Step 1: $K = 3 \pmod 7 = 3$.
- Step 2 (Reverse all): `[7, 6, 5, 4, 3, 2, 1]`
- Step 3 (Reverse first 3): `[5, 6, 7, 4, 3, 2, 1]`
- Step 4 (Reverse remaining): `[5, 6, 7, 1, 2, 3, 4]`

**Complexity:**
- **Time Complexity:** $O(N)$ since each element is reversed twice at most.
- **Space Complexity:** $O(1)$ in-place.

---

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void rotate(vector<int>& nums, int k) {
    int n = nums.size();
    k = k % n; // Handle cases where k > n
    
    // Reverse the entire array
    reverse(nums.begin(), nums.end());
    // Reverse the first k elements
    reverse(nums.begin(), nums.begin() + k);
    // Reverse the remaining n-k elements
    reverse(nums.begin() + k, nums.end());
}

int main() {
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    rotate(nums, 3);
    
    for(int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    // Output: 5 6 7 1 2 3 4
    return 0;
}
```

---

## Common Mistakes
- **Forgetting Modulo:** If $K > N$, the code will crash or misbehave if you don't do `k = k % n`.
- **Mixing up Right vs Left Rotation:** Right rotation requires reversing the whole array *first*. Left rotation requires reversing the segments *first*, then reversing the whole array.

---

## Similar Questions
- Rotate Array Left by K Elements
- Reverse Words in a String (Uses exact same reversal algorithm)

---

## Interview Tips
- Mention the $O(N)$ space brute-force method first. Then ask the interviewer, "Would you like me to optimize the space to $O(1)$?" before showing the Reversal Algorithm. It demonstrates deep understanding.

---

## Variations Asked
- Rotate a Linked List by $K$ nodes.
- Rotate a 2D Matrix by 90 degrees.

---

## Pattern Recognition
**Identify this when:** A problem asks to shift elements cyclically. The **Reversal Algorithm** is the golden standard for cyclic shifts in arrays or strings in $O(1)$ space.
