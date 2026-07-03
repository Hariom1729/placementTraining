# 🚀 C++ STL & Built-in Functions Cheat Sheet

When solving problems in TCS NQT or Zoho, using C++ Standard Template Library (STL) and built-in functions can save you immense amounts of time and lines of code.

Here is a master list of the most important built-in functions and the header files you need to include to use them.

---

## 1. `<algorithm>`
The absolute most important header for DSA. Contains algorithms that operate on sequences (like arrays or vectors).

```cpp
#include <algorithm>
```
* **`sort(start_iter, end_iter)`**: Sorts the range in ascending order.
  * *Example:* `sort(arr.begin(), arr.end());`
  * *Descending:* `sort(arr.begin(), arr.end(), greater<int>());`
* **`reverse(start_iter, end_iter)`**: Reverses the order of elements.
  * *Example:* `reverse(str.begin(), str.end());`
* **`max(a, b)`** / **`min(a, b)`**: Returns the maximum / minimum of two values.
* **`*max_element(start, end)`** / **`*min_element(start, end)`**: Returns the maximum/minimum element in an array/vector.
* **`__gcd(a, b)`**: Returns the Greatest Common Divisor of `a` and `b`.
* **`count(start, end, val)`**: Counts how many times `val` appears in the range.
* **`find(start, end, val)`**: Returns an iterator to the first occurrence of `val`.
* **`next_permutation(start, end)`**: Rearranges elements into the next lexicographically greater permutation.
* **`binary_search(start, end, val)`**: Returns `true` if `val` exists in a *sorted* array, `false` otherwise.
* **`lower_bound(start, end, val)`**: Returns iterator to the first element that is $\ge$ `val`.
* **`upper_bound(start, end, val)`**: Returns iterator to the first element that is $>$ `val`.

---

## 2. `<string>`
Used for manipulating string objects.

```cpp
#include <string>
```
* **`str.length()`** or **`str.size()`**: Returns the number of characters in the string.
* **`str.substr(pos, len)`**: Returns a substring starting at index `pos` spanning `len` characters.
  * *Example:* `string sub = str.substr(0, 3);`
* **`to_string(val)`**: Converts a numerical value (int, float, double) to a string.
  * *Example:* `string s = to_string(123);`
* **`stoi(str)`** / **`stoll(str)`**: Converts a string to an `int` or `long long`.
  * *Example:* `int num = stoi("123");`
* **`str.find(substr)`**: Returns the starting index of the first occurrence of `substr`. Returns `string::npos` if not found.
* **`str.erase(pos, len)`**: Removes `len` characters starting from index `pos`.
* **`str.append(str2)`** or **`str += str2`**: Appends `str2` to the end of `str`.

---

## 3. `<cctype>`
Very heavily used in TCS Ninja/Digital string parsing questions. Used for character classification and conversion.

```cpp
#include <cctype>
```
* **`isalpha(c)`**: Checks if the character `c` is an alphabet letter (a-z or A-Z).
* **`isdigit(c)`**: Checks if the character `c` is a decimal digit (0-9).
* **`isalnum(c)`**: Checks if `c` is alphanumeric (letter or digit).
* **`islower(c)`** / **`isupper(c)`**: Checks if `c` is lowercase / uppercase.
* **`isspace(c)`**: Checks if `c` is a whitespace character (space, newline, tab).
* **`tolower(c)`**: Converts an uppercase letter to lowercase.
* **`toupper(c)`**: Converts a lowercase letter to uppercase.

---

## 4. `<cmath>`
Contains common mathematical operations.

```cpp
#include <cmath>
```
* **`pow(base, exp)`**: Returns `base` raised to the power `exp`. (Returns double, cast to int if needed).
* **`sqrt(x)`**: Returns the square root of `x`.
* **`abs(x)`**: Returns the absolute (positive) value of `x`.
* **`ceil(x)`**: Rounds `x` *up* to the nearest integer. (e.g., `ceil(2.3) == 3.0`)
* **`floor(x)`**: Rounds `x` *down* to the nearest integer. (e.g., `floor(2.8) == 2.0`)
* **`round(x)`**: Rounds `x` to the nearest integer based on standard rounding rules (e.g., `round(2.5) == 3.0`).

---

## 5. `<numeric>`
Used for numeric operations on sequences.

```cpp
#include <numeric>
```
* **`accumulate(start, end, initial_sum)`**: Sums up all elements in the range, adding them to `initial_sum`.
  * *Example:* `int sum = accumulate(arr.begin(), arr.end(), 0);`
* **`iota(start, end, start_val)`**: Fills the range with sequentially increasing values starting at `start_val`.

---

## 6. Containers (Data Structures)

### Arrays & Vectors (`<vector>`)
```cpp
#include <vector>
```
* `v.push_back(val)`: Adds `val` to the end.
* `v.pop_back()`: Removes the last element.
* `v.empty()`: Returns true if the vector is empty.
* `v.clear()`: Removes all elements.

### Stacks (`<stack>`)
```cpp
#include <stack>
```
* `s.push(val)`: Pushes `val` to the top.
* `s.pop()`: Removes the top element. (Does NOT return it).
* `s.top()`: Returns the top element.

### Queues (`<queue>`)
```cpp
#include <queue>
```
* `q.push(val)`: Adds `val` to the back.
* `q.pop()`: Removes the front element.
* `q.front()`: Returns the front element.

### Hash Maps (`<unordered_map>`)
```cpp
#include <unordered_map>
```
* `map[key] = val`: Inserts or updates the value associated with `key`.
* `map.count(key)`: Returns 1 if the key exists, 0 otherwise.

### Hash Sets (`<unordered_set>`)
```cpp
#include <unordered_set>
```
* `set.insert(val)`: Inserts `val` into the set.
* `set.count(val)`: Returns 1 if `val` is in the set, 0 otherwise.

---

## 🔥 The Magic Header (Competitive Programming)
If you don't want to memorize header files, use this single header which includes *almost every standard library in C++*.
**Warning:** It may slightly increase compilation time, but it's perfect for timed coding tests.

```cpp
#include <bits/stdc++.h>
using namespace std;
```
