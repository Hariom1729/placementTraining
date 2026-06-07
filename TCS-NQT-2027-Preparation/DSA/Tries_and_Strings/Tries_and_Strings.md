# Tries & String Algorithms

## 1. Theory & Core Concepts

### Strings in C++
A string is a sequence of characters. In C++, `std::string` provides many built-in methods like `substr()`, `find()`, `push_back()`, and `length()`. Strings are mutable in C++.

### Common String Algorithms:
1. **Two Pointers:** Used for Palindromes, Reverse Strings, etc.
2. **Sliding Window:** Used for Longest Substring Without Repeating Characters, Permutation in String.
3. **KMP (Knuth-Morris-Pratt):** `O(N + M)` string matching algorithm. Finds occurrences of a "pattern" string within a "text" string using an LPS (Longest Prefix Suffix) array.
4. **Rabin-Karp:** String matching using rolling hashing.

---

### Tries (Prefix Trees)
A **Trie** is a specialized tree data structure used for efficient retrieval of a key in a dataset of strings. It is widely used in autocomplete systems, spell checkers, and IP routing.

### Key Characteristics of a Trie:
- Every node represents a character.
- The root node is usually empty.
- A path from the root to a node represents a prefix of some string.
- Each node contains an array (or hash map) of pointers to its children (size 26 for lowercase English letters).
- A boolean flag `isEndOfWord` marks the end of a valid string.

### Trie Operations:
- **Insert:** Start from the root. For each character, if a child link exists, follow it. If not, create a new Trie node. Mark the final node as `isEndOfWord = true`. Time: `O(L)` where L is word length.
- **Search:** Traverse the nodes. If any character link is missing, return `false`. If you reach the end of the word, return `isEndOfWord`. Time: `O(L)`.
- **StartsWith:** Similar to Search, but return `true` as soon as you finish traversing the prefix (you don't care about `isEndOfWord`).

---

## 2. Problem List
*(High frequency problems for TCS NQT)*
*   `01_Implement_Trie.md`
*   `02_Longest_Common_Prefix.md`
*   `03_Valid_Anagram.md`
*   `04_Longest_Substring_Without_Repeating_Characters.md`
*   `05_Find_the_Index_of_the_First_Occurrence_in_a_String_KMP.md`
*   *(... and more)*
