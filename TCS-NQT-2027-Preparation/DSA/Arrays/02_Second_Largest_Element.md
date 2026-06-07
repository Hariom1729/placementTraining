# Problem 2: Find the Second Largest Element in an Array

## Problem Statement
Find the second largest element in an array without sorting the array. If no second largest element exists, return `-1`.

## Input Format
- An array of integers `arr`.

## Output Format
- An integer representing the second largest element.

## Constraints
- `2 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`

---

## Approach

Instead of a two-pass approach (finding largest first, then finding second largest), we can do this efficiently in a single pass.
1. Maintain two variables: `largest` and `secondLargest`, initialized to a very small number (`INT_MIN`).
2. Iterate through the array.
3. If the current element `arr[i]` is strictly greater than `largest`:
   - Update `secondLargest` to be `largest`.
   - Update `largest` to be `arr[i]`.
4. Else, if `arr[i]` is greater than `secondLargest` AND `arr[i]` is not equal to `largest` (to handle duplicates):
   - Update `secondLargest` to be `arr[i]`.
5. Finally, check if `secondLargest` is still `INT_MIN`. If so, it means there is no second largest element. Return `-1` in that case, else return `secondLargest`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int findSecondLargest(vector<int>& arr) {
        int largest = INT_MIN;
        int secondLargest = INT_MIN;
        
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] > largest) {
                secondLargest = largest;
                largest = arr[i];
            } else if (arr[i] > secondLargest && arr[i] != largest) {
                secondLargest = arr[i];
            }
        }
        
        if (secondLargest == INT_MIN) {
            return -1; // Handle case where all elements are the same
        }
        
        return secondLargest;
    }
};

int main() {
    Solution sol;
    vector<int> arr1 = {12, 35, 1, 10, 34, 1};
    cout << "Second Largest: " << sol.findSecondLargest(arr1) << endl; // Expected: 34
    
    vector<int> arr2 = {10, 10, 10};
    cout << "Second Largest: " << sol.findSecondLargest(arr2) << endl; // Expected: -1
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the number of elements in the array. We traverse the array exactly once.
- **Space Complexity:** `O(1)`. We only use two variables for tracking.
