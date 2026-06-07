# Problem 9: Find the Union of Two Sorted Arrays

## Problem Statement
Given two sorted arrays, `arr1` and `arr2`, return a new array containing the union of the two arrays. The union of two arrays can be defined as the common and distinct elements in the two arrays. The resulting array should also be sorted and should not contain duplicates.

## Input Format
- Two sorted arrays of integers `arr1` and `arr2`.

## Output Format
- A sorted array of integers representing the union.

## Constraints
- `1 <= arr1.length, arr2.length <= 10^5`

---

## Approach

Since both arrays are sorted, we can use a **Two Pointers** approach similar to the merge step in Merge Sort, while handling duplicates.
1. Use pointer `i` for `arr1` and pointer `j` for `arr2`. Initialize both to 0.
2. Create an empty `vector<int> Union`.
3. While `i < arr1.size()` and `j < arr2.size()`:
   - If `arr1[i] <= arr2[j]`: Insert `arr1[i]` into `Union` *only if* `Union` is empty or the last element in `Union` is not equal to `arr1[i]` (to prevent duplicates). Then `i++`.
   - Else: Insert `arr2[j]` into `Union` *only if* it's not a duplicate. Then `j++`.
4. Once one of the arrays is exhausted, loop through the remaining elements of the other array and add them to `Union` (again, avoiding duplicates).
5. Return `Union`.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findUnion(vector<int>& arr1, vector<int>& arr2) {
        int i = 0, j = 0;
        vector<int> Union;
        
        while (i < arr1.size() && j < arr2.size()) {
            if (arr1[i] <= arr2[j]) {
                if (Union.empty() || Union.back() != arr1[i])
                    Union.push_back(arr1[i]);
                i++;
            } else {
                if (Union.empty() || Union.back() != arr2[j])
                    Union.push_back(arr2[j]);
                j++;
            }
        }
        
        while (i < arr1.size()) {
            if (Union.empty() || Union.back() != arr1[i]) 
                Union.push_back(arr1[i]);
            i++;
        }
        
        while (j < arr2.size()) {
            if (Union.empty() || Union.back() != arr2[j]) 
                Union.push_back(arr2[j]);
            j++;
        }
        
        return Union;
    }
};

int main() {
    Solution sol;
    vector<int> arr1 = {1, 2, 3, 4, 5};
    vector<int> arr2 = {1, 2, 3, 6, 7};
    
    vector<int> res = sol.findUnion(arr1, arr2);
    for (int x : res) cout << x << " "; // Expected: 1 2 3 4 5 6 7
    cout << endl;
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N + M)` where `N` and `M` are the sizes of the two arrays. We process each element at most once.
- **Space Complexity:** `O(N + M)` to store the resulting union array.
