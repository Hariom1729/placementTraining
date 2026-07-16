# Second Largest Element

## Difficulty
Easy

## Asked In
Infosys SP
Infosys DSE
Year: 2022, 2023
Frequency: Very High

---

## Problem Statement
Given an array `arr` of size `N`, find the second largest distinct element in the array. If the second largest element does not exist, return `-1`.

---

## Input Format
- The first line contains an integer `N`, the size of the array.
- The second line contains `N` space-separated integers representing the array elements.

---

## Output Format
- Return a single integer representing the second largest distinct element.

---

## Constraints
- $2 \le N \le 10^5$
- $1 \le arr[i] \le 10^9$

---

## Examples

### Example 1
**Input:** 
```
6
12 35 1 10 34 1
```
**Output:** 
```
34
```

### Example 2
**Input:** 
```
3
10 10 10
```
**Output:** 
```
-1
```
**Explanation:** The largest element is 10. There is no second largest distinct element.

---

## Brute Force Approach
1. Sort the array in descending order.
2. Iterate through the array and find the first element that is not equal to the largest element (which is at index 0).

**Time Complexity:** $O(N \log N)$ due to sorting.
**Space Complexity:** $O(1)$ assuming in-place sorting.

---

## Better Approach
**Explanation:** 
1. Make a first pass to find the maximum element in the array.
2. Make a second pass to find the maximum element that is strictly less than the maximum element found in the first pass.

**Complexity:** 
- **Time Complexity:** $O(N) + O(N) = O(2N)$, which simplifies to $O(N)$.
- **Space Complexity:** $O(1)$.

---

## Optimal Approach
**Detailed explanation:**
We can do this in a single pass $O(N)$. We maintain two variables, `largest` and `second_largest`, both initialized to an extremely small value (or `-1` depending on constraints). 
As we iterate through the array:
- If the current element is greater than `largest`, we update `second_largest` to be `largest`, and `largest` to be the current element.
- If the current element is less than `largest` but greater than `second_largest`, we update `second_largest`.

**Dry Run:**
Given array: `[12, 35, 1, 10, 34, 1]`
- Initialize `first = -1`, `second = -1`
- `i=0` (12): `12 > first`. `second = -1`, `first = 12`.
- `i=1` (35): `35 > first`. `second = 12`, `first = 35`.
- `i=2` (1): `1 < first` and `1 < second`. No change.
- `i=3` (10): `10 < first` and `10 < second`. No change.
- `i=4` (34): `34 < first` and `34 > second`. `second = 34`.
- `i=5` (1): No change.
- Return `34`.

**Complexity:**
- **Time Complexity:** $O(N)$ for a single pass.
- **Space Complexity:** $O(1)$.

---

## C++ Solution
```cpp
#include <iostream>
#include <vector>
using namespace std;

int getSecondLargest(vector<int> &arr) {
    int n = arr.size();
    if (n < 2) return -1;
    
    int largest = -1;
    int second_largest = -1;
    
    for (int i = 0; i < n; i++) {
        if (arr[i] > largest) {
            second_largest = largest;
            largest = arr[i];
        } else if (arr[i] < largest && arr[i] > second_largest) {
            second_largest = arr[i];
        }
    }
    
    return second_largest;
}

int main() {
    vector<int> arr = {12, 35, 1, 10, 34, 1};
    cout << getSecondLargest(arr) << endl; // Output: 34
    return 0;
}
```

---

## Common Mistakes
- **Initialization:** Initializing `second_largest` to `arr[0]` or `0` can fail if all elements are negative or if constraints require returning `-1` when no such element exists. Initialize to `-1` or `INT_MIN`.
- **Handling Duplicates:** Failing to check `arr[i] < largest`. If `arr[i] == largest`, you should NOT update `second_largest`.

---

## Similar Questions
- Third Largest Element
- Kth Largest Element (Medium)

---

## Interview Tips
- Interviewers love asking you to optimize this from $O(N \log N)$ to $O(N)$ single-pass. Always explain the brute force, then jump to the single-pass approach to show problem-solving progression.

---

## Variations Asked
- Return the *index* of the second largest element instead of the value.
- Find the second *smallest* element.

---

## Pattern Recognition
**Identify this when:** The problem asks for the "top K" or "Kth extreme" element where K is very small (like 2 or 3). If $K$ is small, variables work. If $K$ is large, you need a **Min/Max Heap (Priority Queue)**.
