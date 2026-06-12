# 30. Missing Number (Math Approach)

**Problem:** Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number missing from the array.

**Concept:** 
The expected sum of the first `N` natural numbers is `N * (N + 1) / 2`. Subtract the actual sum of the array from this to find the missing number.

**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

int missingNumber(vector<int>& nums) {
    int n = nums.size();
    int expectedSum = n * (n + 1) / 2;
    int actualSum = 0;
    for(int num : nums) {
        actualSum += num;
    }
    return expectedSum - actualSum;
}

int main() {
    vector<int> nums = {3, 0, 1};
    cout << "Missing Number: " << missingNumber(nums) << "\n"; // 2
    return 0;
}
```
