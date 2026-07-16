# Sort Colors (Dutch National Flag)

## Difficulty
Medium

## Probability
★★★★★

## Asked In
Infosys SP
Infosys DSE
Related Companies: Amazon, Microsoft, Adobe

## Topic
Arrays

## Pattern
Dutch National Flag (Two Pointers)

## Problem Statement
Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

## Constraints
- $1 \le nums.length \le 300$
- $nums[i]$ is either 0, 1, or 2.

## Input Format
- First line: `N`, size of array.
- Second line: `N` space-separated integers containing only 0, 1, or 2.

## Output Format
- Return the sorted array in-place.

## Sample Input
```
6
2 0 2 1 1 0
```

## Sample Output
```
0 0 1 1 2 2
```

## Edge Cases
- All elements are the same color (e.g., `[1, 1, 1]`).
- Array size is 1.
- Missing colors (e.g., only 0s and 2s).

## Approach 1
Brute Force (Sorting)
**Explanation:** Just use a built-in sorting algorithm or merge sort.
**Time Complexity:** $O(N \log N)$
**Space Complexity:** $O(1)$ or $O(N)$ depending on the sort.
*Note: Problem explicitly forbids library sort.*

## Approach 2
Better Approach (Counting Sort)
**Explanation:** Make one pass to count the number of 0s, 1s, and 2s. Make a second pass to overwrite the array with the exact number of 0s, then 1s, then 2s.
**Complexity:** $O(2N)$ time, $O(1)$ space. (Not a single-pass solution).

## Approach 3
Optimal Approach (Dutch National Flag Algorithm)
**Explanation:** We use three pointers: `low`, `mid`, and `high`.
- `low` keeps track of where the next `0` should go.
- `high` keeps track of where the next `2` should go.
- `mid` is the iterator traversing the array.

While `mid <= high`:
- If `nums[mid] == 0`: Swap `nums[low]` and `nums[mid]`. Increment both `low` and `mid`.
- If `nums[mid] == 1`: Leave it alone. Increment `mid`.
- If `nums[mid] == 2`: Swap `nums[mid]` and `nums[high]`. Decrement `high`. (Do NOT increment `mid` yet, because the swapped element from `high` needs to be evaluated).

**Dry Run:**
`nums = [2, 0, 2, 1, 1, 0]`
- init: `low=0`, `mid=0`, `high=5`
- `mid=0` (2): swap mid(0) & high(5). `nums=[0, 0, 2, 1, 1, 2]`. `high=4`.
- `mid=0` (0): swap low(0) & mid(0). `low=1, mid=1`.
- `mid=1` (0): swap low(1) & mid(1). `low=2, mid=2`.
- `mid=2` (2): swap mid(2) & high(4). `nums=[0, 0, 1, 1, 2, 2]`. `high=3`.
- `mid=2` (1): `mid=3`.
- `mid=3` (1): `mid=4`. `mid > high`, break.

**Time Complexity:** $O(N)$ (One Pass)
**Space Complexity:** $O(1)$

## Java Solution
```java
class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        
        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums, low, mid);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                swap(nums, mid, high);
                high--;
            }
        }
    }
    
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

## Python Solution
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0;
        int mid = 0;
        int high = nums.size() - 1;
        
        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums[low], nums[mid]);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                swap(nums[mid], nums[high]);
                high--;
            }
        }
    }
};
```

## Common Mistakes
- **Incrementing `mid` when swapping with `high`:** If you swap `mid` and `high`, the new element sitting at `mid` came from the end of the array, meaning we have NO idea what it is. We must evaluate it on the next loop iteration. Therefore, do NOT `mid++` in the `nums[mid] == 2` block.

## Interview Tips
- Mention the counting sort approach first (2 passes). The interviewer will ask for a 1-pass solution. That is your cue to bring out the Dutch National Flag algorithm.

## Similar Questions
- Sort List
- Wiggle Sort
- Sort Array By Parity

## Variations Asked in Infosys
- Arrange negative numbers to the left and positive to the right.
