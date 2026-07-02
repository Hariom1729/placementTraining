# 🔥 Top 50 High-Probability TCS NQT Coding Questions (Part 5: Q41 - Q50)

## 41. Find the Sum of Fractions
**Concept:** Given two fractions `num1/den1` and `num2/den2`, find their sum and output it in the simplest form.
```cpp
#include <iostream>
using namespace std;

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

void sumOfFractions(int num1, int den1, int num2, int den2) {
    int lcm = (den1 * den2) / gcd(den1, den2);
    int sum_num = (num1 * (lcm / den1)) + (num2 * (lcm / den2));
    
    int common_factor = gcd(sum_num, lcm);
    cout << sum_num / common_factor << "/" << lcm / common_factor << endl;
}

int main() {
    sumOfFractions(1, 2, 3, 4); // Output: 5/4
    return 0;
}
```

## 42. Check if Two Given Rectangles Overlap
**Concept:** A rectangle is defined by its bottom-left and top-right coordinates. They don't overlap if one is entirely to the left, right, top, or bottom of the other.
```cpp
#include <iostream>
using namespace std;

struct Point {
    int x, y;
};

bool doOverlap(Point l1, Point r1, Point l2, Point r2) {
    // If one rectangle is on left side of other
    if (l1.x > r2.x || l2.x > r1.x) return false;
    
    // If one rectangle is above other
    if (r1.y > l2.y || r2.y > l1.y) return false;
    
    return true;
}
```

## 43. Check if a Number is a Perfect Number
**Concept:** A perfect number is a positive integer that is equal to the sum of its proper divisors.
```cpp
#include <iostream>
using namespace std;

bool isPerfect(int n) {
    int sum = 1;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            sum += i;
            if (n / i != i) sum += n / i;
        }
    }
    return sum == n && n != 1;
}

int main() {
    cout << (isPerfect(28) ? "Yes" : "No") << endl; // Yes (1+2+4+7+14=28)
    return 0;
}
```

## 44. Calculate the Sum of Numbers in a String
**Concept:** A string contains alphanumeric characters. Extract contiguous digits to form numbers and sum them up.
```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int sumOfNumbersInString(string str) {
    int sum = 0;
    string temp = "";
    
    for (char c : str) {
        if (isdigit(c)) {
            temp += c;
        } else {
            if (!temp.empty()) {
                sum += stoi(temp);
                temp = "";
            }
        }
    }
    if (!temp.empty()) sum += stoi(temp); // Handle number at the end
    
    return sum;
}

int main() {
    cout << sumOfNumbersInString("12abc20xyz3") << endl; // Output: 35
    return 0;
}
```

## 45. Sort an Array According to the Order Defined by Another Array
**Concept:** Use a custom comparator or a hash map to count occurrences and place elements according to the second array.
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

void sortA1ByA2(vector<int>& A1, vector<int>& A2) {
    unordered_map<int, int> freq;
    for(int num : A1) freq[num]++;
    
    vector<int> result;
    // Add elements based on A2's order
    for(int num : A2) {
        while(freq[num] > 0) {
            result.push_back(num);
            freq[num]--;
        }
    }
    // Add remaining elements sorted
    vector<int> remaining;
    for(auto it : freq) {
        while(it.second > 0) {
            remaining.push_back(it.first);
            it.second--;
        }
    }
    sort(remaining.begin(), remaining.end());
    result.insert(result.end(), remaining.begin(), remaining.end());
    
    for(int num : result) cout << num << " ";
    cout << endl;
}
```

## 46. Maximum Product Subarray
**Concept:** Keep track of the maximum and minimum product ending at the current element, because a negative number multiplied by a minimum (negative) product becomes a maximum product.
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxProduct(vector<int>& nums) {
    int max_prod = nums[0], min_prod = nums[0], ans = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] < 0) swap(max_prod, min_prod);
        max_prod = max(nums[i], max_prod * nums[i]);
        min_prod = min(nums[i], min_prod * nums[i]);
        ans = max(ans, max_prod);
    }
    return ans;
}

int main() {
    vector<int> arr = {2, 3, -2, 4};
    cout << "Max Product: " << maxProduct(arr) << endl; // Output: 6
    return 0;
}
```

## 47. Longest Common Prefix Among an Array of Strings
**Concept:** Sort the strings lexicographically and compare only the first and the last strings.
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    if (strs.empty()) return "";
    sort(strs.begin(), strs.end());
    
    string first = strs[0], last = strs[strs.size() - 1];
    string ans = "";
    
    for (int i = 0; i < min(first.length(), last.length()); i++) {
        if (first[i] != last[i]) return ans;
        ans += first[i];
    }
    return ans;
}
```

## 48. Check if a Number is an Automorphic Number
**Concept:** An automorphic number is a number whose square ends in the same digits as the number itself (e.g., $5^2 = 25$, $76^2 = 5776$).
```cpp
#include <iostream>
using namespace std;

bool isAutomorphic(int n) {
    int square = n * n;
    while (n > 0) {
        if (n % 10 != square % 10) return false;
        n /= 10;
        square /= 10;
    }
    return true;
}

int main() {
    cout << (isAutomorphic(76) ? "Automorphic" : "Not Automorphic") << endl;
    return 0;
}
```

## 49. Reverse an Array in Groups of Given Size
**Concept:** Iterate through the array with a step of `k` and reverse the sub-array of size `k`.
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void reverseInGroups(vector<int>& arr, int k) {
    int n = arr.size();
    for (int i = 0; i < n; i += k) {
        int left = i;
        int right = min(i + k - 1, n - 1);
        while (left < right) {
            swap(arr[left++], arr[right--]);
        }
    }
}
```

## 50. Maximum Difference Between Two Elements (Larger Appears After Smaller)
**Concept:** Keep track of the minimum element seen so far and update the maximum difference.
```cpp
#include <iostream>
#include <vector>
using namespace std;

int maxDifference(vector<int>& arr) {
    if (arr.size() < 2) return -1;
    
    int min_element = arr[0];
    int max_diff = arr[1] - arr[0];
    
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] - min_element > max_diff) {
            max_diff = arr[i] - min_element;
        }
        if (arr[i] < min_element) {
            min_element = arr[i];
        }
    }
    return max_diff > 0 ? max_diff : -1;
}

int main() {
    vector<int> arr = {2, 3, 10, 6, 4, 8, 1};
    cout << "Max Difference: " << maxDifference(arr) << endl; // Output: 8 (10 - 2)
    return 0;
}
```
