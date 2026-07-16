# Strings

Welcome to the **Strings** section of the Infosys SP & DSE preparation repository.

This module contains the highest-probability String manipulation, parsing, and pattern matching problems asked in Infosys coding rounds. Strings are fundamental to Infosys Online Assessments, often involving two pointers, sliding window, hashing, or dynamic programming.

## Table of Contents

| # | Problem Name | Difficulty | Pattern |
|---|---|---|---|
| 01 | [Valid Palindrome](./01_Valid_Palindrome.md) | Easy | Two Pointers |
| 02 | [Valid Anagram](./02_Valid_Anagram.md) | Easy | Hashing |
| 03 | [Longest Substring Without Repeating Characters](./03_Longest_Substring_Without_Repeating_Characters.md) | Medium | Sliding Window |
| 04 | [Longest Palindromic Substring](./04_Longest_Palindromic_Substring.md) | Medium | Expand Around Center / DP |
| 05 | [String to Integer (atoi)](./05_String_to_Integer_atoi.md) | Medium | Parsing / Math |

*(More problems will be added in subsequent batches...)*

## Key Concepts to Master
1. **ASCII Values:** Characters in C++ are just integers. `ch - 'a'` gives the alphabetical index `0-25`.
2. **Hash Maps for Strings:** Using `vector<int> count(26, 0)` is vastly faster than `unordered_map<char, int>` when you know the string only contains lowercase English letters.
3. **Sliding Window:** For problems like "Longest Substring with X condition", use two pointers `left` and `right` to maintain a valid window.
4. **Palindrome Checking:** Two pointers starting from ends and moving towards the center is the standard way to check palindromes. Expanding from the center is the standard way to *find* palindromes.
5. **C++ String Methods:** Master `substr()`, `find()`, `push_back()`, `pop_back()`, and `getline(stringstream, string, char)`.
