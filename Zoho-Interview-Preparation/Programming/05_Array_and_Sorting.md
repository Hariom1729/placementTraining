# Programming: Array and Custom Sorting

Zoho tests custom comparators and manual sorting logic extensively.

## 1. Alternate Sorting
**Problem:** Sort the array such that the first element is maximum, second is minimum, third is second max, fourth is second min, etc.
**Input:** `[1, 2, 3, 4, 5, 6, 7]`
**Output:** `[7, 1, 6, 2, 5, 3, 4]`
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7};
    sort(arr.begin(), arr.end()); // In Zoho, write your own sorting algorithm here
    
    vector<int> result(arr.size());
    int left = 0, right = arr.size() - 1;
    int index = 0;
    
    bool flag = true;
    while(left <= right) {
        if(flag) {
            result[index++] = arr[right--];
        } else {
            result[index++] = arr[left++];
        }
        flag = !flag;
    }
    
    for(int val : result) cout << val << " ";
    cout << "\n";
    return 0;
}
```

## 2. Sort by Frequency
**Problem:** Sort elements by their frequency. Elements with higher frequency come first. If frequencies are the same, sort by the element's value ascending.
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    vector<int> arr = {4, 4, 2, 2, 2, 3, 3, 1};
    unordered_map<int, int> freqMap;
    
    for (int num : arr) {
        freqMap[num]++;
    }
    
    sort(arr.begin(), arr.end(), [&](int a, int b) {
        if(freqMap[a] != freqMap[b]) {
            return freqMap[a] > freqMap[b]; // Descending frequency
        }
        return a < b; // Ascending value
    });
    
    for(int val : arr) cout << val << " ";
    cout << "\n";
    return 0;
}
```

## 3. Merge Two Sorted Arrays Without Extra Space
**Problem:** Given two sorted arrays, merge them into the first array assuming the first array has enough empty buffer at the end.
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> nums1 = {1, 2, 3, 0, 0, 0};
    int m = 3;
    vector<int> nums2 = {2, 5, 6};
    int n = 3;
    
    int p1 = m - 1;
    int p2 = n - 1;
    int p = m + n - 1;
    
    while(p1 >= 0 && p2 >= 0) {
        if(nums1[p1] > nums2[p2]) {
            nums1[p] = nums1[p1];
            p1--;
        } else {
            nums1[p] = nums2[p2];
            p2--;
        }
        p--;
    }
    
    // If elements are left in nums2
    while(p2 >= 0) {
        nums1[p] = nums2[p2];
        p2--;
        p--;
    }
    
    for(int val : nums1) cout << val << " ";
    cout << "\n";
    return 0;
}
```
