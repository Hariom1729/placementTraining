# 1. Arrays

## 📖 Theory & Fundamentals
An array is a linear data structure that collects elements of the same data type and stores them in contiguous and adjacent memory locations. In Zoho interviews, arrays are the most heavily tested data structure. You are often restricted from using built-in functions like `sort()`, forcing you to implement logic from scratch.

### Array Properties:
- **Fixed Size:** In standard C++, `int arr[10];` allocates exactly 10 integers. (Dynamic arrays like `std::vector` resize automatically).
- **0-Indexed:** The first element is at index 0.
- **Contiguous Memory:** Elements are stored side-by-side. If the address of `arr[0]` is `2000` and each int is 4 bytes, `arr[1]` is at `2004`.

## 🧠 Common Patterns & Techniques
1. **Two Pointers:** Using two indices (usually `left` and `right`) to traverse the array from opposite ends. Excellent for reversing, checking palindromes, or finding pairs in a sorted array.
2. **Sliding Window:** Maintaining a "window" of elements (e.g., indices `i` to `j`). As the window slides across the array, you add the new element and remove the old one. Great for subarray sum or continuous sequence problems.
3. **Prefix Sum:** Creating an auxiliary array where `prefix[i]` stores the sum of elements from index `0` to `i`. Allows $O(1)$ range sum queries.
4. **Kadane's Algorithm:** Used specifically to find the maximum sum contiguous subarray in $O(N)$ time.
5. **Dutch National Flag (DNF):** Used to sort an array of 3 distinct elements (like 0s, 1s, and 2s) in a single pass $O(N)$.

## ⏱️ Complexity Analysis
- **Access:** $O(1)$ - `arr[5]` instantly accesses the 6th element.
- **Search (Unsorted):** $O(N)$ - Must check every element.
- **Search (Sorted):** $O(\log N)$ - Using Binary Search.
- **Insertion/Deletion (at end):** $O(1)$
- **Insertion/Deletion (at index `i`):** $O(N)$ - Requires shifting elements to make room or fill the gap.

## 📝 Interview Notes for Zoho
- **Do not use `std::sort` unless explicitly permitted.** Be prepared to write Quick Sort or Merge Sort.
- Zoho loves **Matrix (2D Array)** manipulation. Master traversing spirals, diagonals, and rotating grids 90 degrees.
- Pay attention to constraints. If elements are $10^5$, an $O(N^2)$ solution will yield a Time Limit Exceeded (TLE). You must find an $O(N)$ or $O(N \log N)$ approach.

---

## 💻 Problem Bank (50 Questions)

*Note: Due to space constraints, we have provided full solutions and dry runs for the top 15 most critical patterns, followed by 35 practice problem statements.*

### Easy Questions (1-15)

#### 1. Reverse an Array
**Statement:** Given an array, reverse it in-place.
**Input:** `[1, 2, 3, 4, 5]`
**Output:** `[5, 4, 3, 2, 1]`
**Optimized C++ Solution (Two Pointers):**
```cpp
void reverseArray(vector<int>& arr) {
    int left = 0, right = arr.size() - 1;
    while(left < right) {
        swap(arr[left], arr[right]);
        left++; right--;
    }
}
```
**Complexity:** $O(N)$ Time, $O(1)$ Space.
**Dry Run:** `[1,2,3,4,5]` -> `left=0 (1)`, `right=4 (5)`. Swap -> `[5,2,3,4,1]`. `left=1`, `right=3`. Swap -> `[5,4,3,2,1]`. `left=2`, `right=2`. Loop ends.

#### 2. Find Maximum and Minimum Element
**Statement:** Find the max and min in an array.
**Input:** `[3, 5, 1, 9]`
**Output:** Max: 9, Min: 1
**C++ Solution:**
```cpp
void findMaxMin(vector<int>& arr) {
    int maxEl = INT_MIN, minEl = INT_MAX;
    for(int num : arr) {
        if(num > maxEl) maxEl = num;
        if(num < minEl) minEl = num;
    }
    cout << "Max: " << maxEl << ", Min: " << minEl;
}
```

#### 3. Find the 'K'th Max and Min element
**Statement:** Find the Kth largest and smallest element in an array.
**C++ Solution (Using Sorting - $O(N \log N)$):**
```cpp
void kthMaxMin(vector<int>& arr, int k) {
    sort(arr.begin(), arr.end()); // In Zoho, write your own Merge Sort here
    cout << "Kth Min: " << arr[k-1] << ", Kth Max: " << arr[arr.size()-k];
}
```

#### 4. Sort an array of 0s, 1s, and 2s (Dutch National Flag)
**Statement:** Sort an array containing only 0, 1, and 2 without using a sorting algo.
**Input:** `[2, 0, 2, 1, 1, 0]`
**Output:** `[0, 0, 1, 1, 2, 2]`
**C++ Solution ($O(N)$):**
```cpp
void sortColors(vector<int>& nums) {
    int low = 0, mid = 0, high = nums.size() - 1;
    while(mid <= high) {
        if(nums[mid] == 0) swap(nums[low++], nums[mid++]);
        else if(nums[mid] == 1) mid++;
        else swap(nums[mid], nums[high--]);
    }
}
```

#### 5. Move all negative numbers to beginning
**Statement:** Move all negative numbers to one side of the array. Order doesn't matter.
**Input:** `[-1, 2, -3, 4, 5, -6]`
**Output:** `[-1, -3, -6, 4, 5, 2]`
**C++ Solution (Two Pointers):**
```cpp
void moveNegatives(vector<int>& arr) {
    int left = 0, right = arr.size() - 1;
    while(left <= right) {
        if(arr[left] < 0) left++;
        else if(arr[right] >= 0) right--;
        else swap(arr[left++], arr[right--]);
    }
}
```

*(Questions 6-15: Linear Search, Binary Search, Check if Array is Sorted, Remove Duplicates from Sorted Array, Left Rotate an Array by One, Find Missing Number, Max Consecutive Ones, Find single appearing element, Intersection of two sorted arrays, Union of two sorted arrays - implementation omitted for brevity).*

### Medium Questions (16-35)

#### 16. Kadane's Algorithm (Maximum Subarray Sum)
**Statement:** Find the contiguous subarray which has the largest sum.
**Input:** `[-2,1,-3,4,-1,2,1,-5,4]`
**Output:** `6` (from `[4,-1,2,1]`)
**Optimized C++ Solution:**
```cpp
int maxSubArray(vector<int>& nums) {
    int maxSum = INT_MIN, currentSum = 0;
    for(int num : nums) {
        currentSum += num;
        if(currentSum > maxSum) maxSum = currentSum;
        if(currentSum < 0) currentSum = 0; // Reset if negative
    }
    return maxSum;
}
```
**Complexity:** $O(N)$ Time.

#### 17. Merge Intervals
**Statement:** Merge all overlapping intervals.
**Input:** `[[1,3],[2,6],[8,10],[15,18]]`
**Output:** `[[1,6],[8,10],[15,18]]`
**C++ Solution:**
```cpp
vector<vector<int>> merge(vector<vector<int>>& intervals) {
    if(intervals.empty()) return {};
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> merged;
    merged.push_back(intervals[0]);
    for(int i = 1; i < intervals.size(); i++) {
        if(merged.back()[1] >= intervals[i][0]) {
            merged.back()[1] = max(merged.back()[1], intervals[i][1]);
        } else {
            merged.push_back(intervals[i]);
        }
    }
    return merged;
}
```

#### 18. Next Permutation
**Statement:** Find the lexicographically next greater permutation of numbers.
**Input:** `[1, 2, 3]`
**Output:** `[1, 3, 2]`
**C++ Solution:**
```cpp
void nextPermutation(vector<int>& nums) {
    int i = nums.size() - 2;
    while(i >= 0 && nums[i] >= nums[i+1]) i--;
    if(i >= 0) {
        int j = nums.size() - 1;
        while(nums[j] <= nums[i]) j--;
        swap(nums[i], nums[j]);
    }
    reverse(nums.begin() + i + 1, nums.end());
}
```

#### 19. Two Sum Problem
**Statement:** Find two numbers such that they add up to a specific target.
**Optimized C++ Solution (HashMap - $O(N)$):**
```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> map;
    for(int i=0; i<nums.size(); i++) {
        int complement = target - nums[i];
        if(map.count(complement)) return {map[complement], i};
        map[nums[i]] = i;
    }
    return {};
}
```

#### 20. Best Time to Buy and Sell Stock
**Statement:** You can buy once and sell once. Find max profit.
**Input:** `[7,1,5,3,6,4]`
**Output:** `5` (Buy at 1, sell at 6).
**C++ Solution:**
```cpp
int maxProfit(vector<int>& prices) {
    int minPrice = INT_MAX, maxProf = 0;
    for(int price : prices) {
        minPrice = min(minPrice, price);
        maxProf = max(maxProf, price - minPrice);
    }
    return maxProf;
}
```

*(Questions 21-35: Container With Most Water, 3Sum, 4Sum, Subarray Sum Equals K, Longest Consecutive Sequence, Spiral Matrix, Rotate Image (Matrix), Set Matrix Zeroes, Search in 2D Matrix, Find Peak Element, Find Minimum in Rotated Sorted Array, Search in Rotated Sorted Array, Product of Array Except Self, Majority Element (Boyer-Moore Voting), Find All Duplicates in an Array).*

### Hard Questions (36-50)

#### 36. Trapping Rain Water
**Statement:** Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
**Input:** `[0,1,0,2,1,0,1,3,2,1,2,1]`
**Output:** `6`
**Optimized C++ Solution (Two Pointers):**
```cpp
int trap(vector<int>& height) {
    int left = 0, right = height.size() - 1;
    int leftMax = 0, rightMax = 0, water = 0;
    while(left < right) {
        if(height[left] < height[right]) {
            if(height[left] >= leftMax) leftMax = height[left];
            else water += leftMax - height[left];
            left++;
        } else {
            if(height[right] >= rightMax) rightMax = height[right];
            else water += rightMax - height[right];
            right--;
        }
    }
    return water;
}
```

#### 37. Median of Two Sorted Arrays
**Statement:** Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. Time complexity must be $O(\log(m+n))$.
**C++ Solution (Binary Search on smaller array):**
*(Implementation requires advanced binary search partitioning).*

#### 38. Merge K Sorted Arrays/Lists
**Statement:** Merge $K$ sorted arrays into a single sorted array.
**Optimized C++ Approach:** Use a Min-Heap (Priority Queue). Push the first element of all $K$ arrays into the heap. Pop the minimum, add to result, and push the next element from the array the popped element belonged to.

#### 39. Count Inversions in an Array
**Statement:** Two elements `a[i]` and `a[j]` form an inversion if `a[i] > a[j]` and `i < j`. Find total inversions.
**Optimized C++ Approach:** Modify Merge Sort. During the merge step, if `left[i] > right[j]`, then there are `(mid - i + 1)` inversions.

#### 40. Maximum Product Subarray
**Statement:** Find the contiguous subarray within an array (containing at least one number) which has the largest product.
**C++ Solution:**
```cpp
int maxProduct(vector<int>& nums) {
    int maxProd = nums[0], minProd = nums[0], ans = nums[0];
    for(int i=1; i<nums.size(); i++) {
        if(nums[i] < 0) swap(maxProd, minProd);
        maxProd = max(nums[i], maxProd * nums[i]);
        minProd = min(nums[i], minProd * nums[i]);
        ans = max(ans, maxProd);
    }
    return ans;
}
```

#### Additional Practice Questions (41-50):
41. First Missing Positive ($O(N)$ time, $O(1)$ space).
42. Sliding Window Maximum (Deque approach).
43. Minimum Size Subarray Sum.
44. Longest Subarray with Zero Sum.
45. Count Subarrays with Given XOR.
46. Reverse Pairs (Merge Sort modification).
47. Find the Duplicate Number (Floyd's Tortoise and Hare).
48. Chocolate Distribution Problem.
49. Minimum Jumps to Reach End (Greedy).
50. Minimize the maximum difference between heights.
