# Strings in Data Structures & Algorithms

## 1. Theory & Core Concepts

A **String** is essentially a sequence of characters. In C++, strings are typically handled using the standard library class `std::string`.

### Key Characteristics:
- **Mutability (C++):** Unlike Java or Python where strings are immutable, `std::string` in C++ is **mutable**. You can change characters in-place (e.g., `s[i] = 'a'`), making algorithms like reversing a string extremely memory efficient (`O(1)` space).
- **Character Arrays:** You can also use C-style strings (`char[]` terminated by a null character `\0`), but `std::string` is much safer and provides many built-in methods.
- **ASCII and Unicode:** Understanding character encoding is crucial. The ASCII value of `'a'` is 97, and `'A'` is 65. The difference is 32. 

### Best Practices (C++):
- **Pass by Reference:** When passing strings to functions, always pass them by reference (`const string& s` or `string& s`) to avoid expensive `O(N)` copies.
- **In-place Operations:** Because C++ strings are mutable, always look for in-place solutions (like using `std::swap` for two pointers) instead of creating new strings.

---

## 2. Complexity Analysis of Built-in Methods (C++)

| Method | Time Complexity | Note |
| :--- | :---: | :--- |
| `s[i]` | `O(1)` | Direct access via index. |
| `s.substr(pos, len)` | `O(N)` | Creates and returns a new `std::string`. |
| `s.length()` / `s.size()` | `O(1)` | Returns the pre-computed length. |
| `s.find(str)` | `O(N * M)` | Finds the first occurrence of `str`. |
| `s.push_back(c)` | `O(1)` amortized | Appends character to the end. |
| `s1 == s2`| `O(N)` | Compares character by character. |

---

## 3. Common Patterns in String Problems

When solving string problems for TCS NQT, look out for these heavily tested patterns:

1. **Two Pointers:** 
   - Used for Palindrome checking, Reversing a string, or finding symmetric properties.
2. **Sliding Window:** 
   - Used to find the "Longest substring with K unique characters" or "Longest substring without repeating characters".
3. **Hashing (Frequency Arrays):** 
   - Since there are only 26 lowercase English letters, a fixed size array `int[26]` or `std::vector<int>(26, 0)` acts as a perfect $O(1)$ space hash map for Anagrams and frequency counting.
4. **String Matching:**
   - Basic matching `O(N*M)`.
5. **Stack (`std::stack`):**
   - Used for Valid Parentheses, removing adjacent duplicates, or parsing strings.

---

## 4. Problem List

To keep study materials organized and easy to digest, each coding problem has been placed into its own dedicated Markdown file within this directory. Start with `01_Reverse_String.md` and work your way through sequentially.

*   `01_Reverse_String.md`
*   `02_Valid_Palindrome.md`
*   `03_Valid_Anagram.md`
*   `04_Longest_Substring_Without_Repeating.md`
*   `05_Longest_Palindromic_Substring.md`
*(...and so on)*
