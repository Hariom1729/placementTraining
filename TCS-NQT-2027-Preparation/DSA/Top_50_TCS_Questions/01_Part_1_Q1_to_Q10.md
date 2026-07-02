# 🔥 Top 50 High-Probability TCS NQT Coding Questions (Part 1: Q1 - Q10)

## 1. Decimal to Base-N Conversion (or vice versa)
**Concept:** TCS loves number systems. A very frequent question is converting a decimal number to binary, octal, or an arbitrary base (like base 17), or converting from base-N to decimal.

**Example:**
- **Input:** N = 25
- **Output:** 11001
- **Explanation:** 25 in binary is represented as 11001.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string decimalToBinary(int n) {
    if (n == 0) return "0";
    string binary = "";
    while (n > 0) {
        binary += to_string(n % 2);
        n /= 2;
    }
    reverse(binary.begin(), binary.end());
    return binary;
}

int main() {
    cout << decimalToBinary(25) << endl; // Output: 11001
    return 0;
}
```

## 2. Counting Frequencies of Elements/Characters
**Concept:** Arrays or Strings where you need to count occurrences to find duplicates, unique elements, or the most frequent element. (Using Hash Maps).

**Example:**
- **Input:** str = "tcsnqttcs"
- **Output:** 3 (Index of 'n')
- **Explanation:** 't', 'c', and 's' repeat. The first character that does not repeat is 'n' at index 3.

```cpp
#include <iostream>
#include <unordered_map>
using namespace std;

int firstUniqChar(string s) {
    unordered_map<char, int> count;
    for (char c : s) {
        count[c]++;
    }
    for (int i = 0; i < s.length(); i++) {
        if (count[s[i]] == 1) return i;
    }
    return -1;
}

int main() {
    cout << firstUniqChar("tcsnqttcs") << endl; // Output: 3 ('n')
    return 0;
}
```

## 3. Second Largest and Second Smallest Element
**Concept:** TCS frequently asks for the second largest or second smallest element in an array *without* using the built-in sorting function, requiring a single or double pass $O(N)$ solution.

**Example:**
- **Input:** arr = [12, 35, 1, 10, 34, 1]
- **Output:** 34
- **Explanation:** The largest element is 35. The second largest is 34.

```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int secondLargest(vector<int>& arr) {
    int first = INT_MIN, second = INT_MIN;
    for (int num : arr) {
        if (num > first) {
            second = first;
            first = num;
        } else if (num > second && num != first) {
            second = num;
        }
    }
    return second == INT_MIN ? -1 : second;
}

int main() {
    vector<int> arr = {12, 35, 1, 10, 34, 1};
    cout << secondLargest(arr) << endl; // Output: 34
    return 0;
}
```

## 4. Valid Anagram
**Concept:** String manipulation is a heavy focus in TCS Ninja. Checking if two strings are anagrams of each other.

**Example:**
- **Input:** s = "listen", t = "silent"
- **Output:** Yes
- **Explanation:** Both strings contain the exact same characters with the same frequencies.

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool isAnagram(string s, string t) {
    if (s.length() != t.length()) return false;
    vector<int> count(26, 0);
    
    for (int i = 0; i < s.length(); i++) {
        count[s[i] - 'a']++;
        count[t[i] - 'a']--;
    }
    for (int c : count) {
        if (c != 0) return false;
    }
    return true;
}

int main() {
    cout << (isAnagram("listen", "silent") ? "Yes" : "No") << endl; // Yes
    return 0;
}
```

## 5. Subarray with Given Sum (Sliding Window)
**Concept:** Often asked in the Digital profile. Given an array of positive integers, find a contiguous subarray that adds up to a given number `S`.

**Example:**
- **Input:** arr = [1, 4, 20, 3, 10, 5], sum = 33
- **Output:** Found between indexes 2 and 4
- **Explanation:** Elements at index 2, 3, and 4 are 20 + 3 + 10 = 33.

```cpp
#include <iostream>
#include <vector>
using namespace std;

void subarraySum(vector<int>& arr, int sum) {
    int current_sum = arr[0], start = 0;
    
    for (int i = 1; i <= arr.size(); i++) {
        // Clean up window if sum exceeds
        while (current_sum > sum && start < i - 1) {
            current_sum -= arr[start];
            start++;
        }
        // Check if sum matches
        if (current_sum == sum) {
            cout << "Found between indexes " << start << " and " << i - 1 << endl;
            return;
        }
        // Add next element
        if (i < arr.size()) current_sum += arr[i];
    }
    cout << "No subarray found" << endl;
}

int main() {
    vector<int> arr = {1, 4, 20, 3, 10, 5};
    subarraySum(arr, 33); // Found between indexes 2 and 4
    return 0;
}
```

## 6. Rotate a Matrix by 90 Degrees
**Concept:** 2D Array manipulation is standard for Digital rounds. Instead of allocating a new matrix, do it in-place.

**Example:**
- **Input:** 
  [[1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]]
- **Output:** 
  [[7, 4, 1],
   [8, 5, 2],
   [9, 6, 3]]
- **Explanation:** The matrix is rotated 90 degrees clockwise.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void rotateMatrix(vector<vector<int>>& matrix) {
    int n = matrix.size();
    // 1. Transpose the matrix
    for(int i = 0; i < n; i++) {
        for(int j = i; j < n; j++) {
            swap(matrix[i][j], matrix[j][i]);
        }
    }
    // 2. Reverse each row
    for(int i = 0; i < n; i++) {
        reverse(matrix[i].begin(), matrix[i].end());
    }
}
```

## 7. Next Greater Element
**Concept:** Stack-based algorithms are a favorite. Find the next greater element for every element in an array.

**Example:**
- **Input:** arr = [4, 5, 2, 25]
- **Output:** [5, 25, 25, -1]
- **Explanation:** 5 is greater than 4, 25 is greater than 5 and 2, and nothing is greater than 25.

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, -1);
    stack<int> s;
    
    for(int i = 0; i < n; i++) {
        while(!s.empty() && nums[s.top()] < nums[i]) {
            result[s.top()] = nums[i];
            s.pop();
        }
        s.push(i);
    }
    return result;
}
```

## 8. Reverse Words in a String
**Concept:** A string parsing question where you have to reverse the words, but keep the word itself intact, removing extra spaces.

**Example:**
- **Input:** "  hello   world  "
- **Output:** "world hello"
- **Explanation:** The words are reversed and extra spaces are removed.

```cpp
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

string reverseWords(string s) {
    stringstream ss(s);
    string word;
    string result = "";
    
    while (ss >> word) {
        result = word + " " + result;
    }
    if (!result.empty()) {
        result.pop_back(); // remove trailing space
    }
    return result;
}

int main() {
    cout << reverseWords("  hello   world  ") << endl; // "world hello"
    return 0;
}
```

## 9. Longest Common Subsequence (LCS)
**Concept:** A highly probable question for the **Prime** profile. Standard 2D Dynamic Programming.

**Example:**
- **Input:** text1 = "abcde", text2 = "ace" 
- **Output:** 3
- **Explanation:** The longest common subsequence is "ace" and its length is 3.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length(), n = text2.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    
    for(int i = 1; i <= m; i++) {
        for(int j = 1; j <= n; j++) {
            if(text1[i-1] == text2[j-1]) {
                dp[i][j] = 1 + dp[i-1][j-1];
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    return dp[m][n];
}
```

## 10. Find Missing and Repeating Number
**Concept:** Math and Array combinations. Given an array of size $N$ containing numbers from 1 to $N$, one number is missing and one is repeating.

**Example:**
- **Input:** arr = [3, 1, 3]
- **Output:** Missing: 2, Repeating: 3
- **Explanation:** The array should contain 1, 2, 3. Number 2 is missing and 3 is repeated.

```cpp
#include <iostream>
#include <vector>
using namespace std;

void findMissingAndRepeating(vector<int>& arr) {
    long long n = arr.size();
    long long S = (n * (n + 1)) / 2;
    long long P = (n * (n + 1) * (2 * n + 1)) / 6;
    
    long long actual_S = 0, actual_P = 0;
    for(int i = 0; i < n; i++) {
        actual_S += (long long)arr[i];
        actual_P += (long long)arr[i] * (long long)arr[i];
    }
    
    long long diff_S = S - actual_S; // Missing - Repeating
    long long diff_P = P - actual_P; // Missing^2 - Repeating^2
    
    long long sum_S = diff_P / diff_S; // Missing + Repeating
    
    long long missing = (diff_S + sum_S) / 2;
    long long repeating = sum_S - missing;
    
    cout << "Missing: " << missing << ", Repeating: " << repeating << endl;
}
```
