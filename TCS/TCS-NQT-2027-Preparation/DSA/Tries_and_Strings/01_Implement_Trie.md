# Problem 1: Implement Trie (Prefix Tree)

## Problem Statement
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

## Constraints
- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters.
- At most `3 * 10^4` calls in total will be made to insert, search, and startsWith.

---

## Approach: Trie Nodes

We create a struct `TrieNode`. Since the alphabet only consists of 26 lowercase English letters, each node will have an array of 26 `TrieNode` pointers. It will also have a boolean `isEndOfWord` flag.
For insertion and searching, we iterate through the characters of the string. The character `'a'` maps to index `0`, `'b'` to index `1`, etc. (`char - 'a'`).

---

## C++ Solution

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// TrieNode structure
struct TrieNode {
    TrieNode* children[26];
    bool isEndOfWord;
    
    TrieNode() {
        isEndOfWord = false;
        for (int i = 0; i < 26; i++) {
            children[i] = nullptr;
        }
    }
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            int index = c - 'a';
            if (curr->children[index] == nullptr) {
                curr->children[index] = new TrieNode();
            }
            curr = curr->children[index];
        }
        curr->isEndOfWord = true;
    }
    
    bool search(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            int index = c - 'a';
            if (curr->children[index] == nullptr) {
                return false;
            }
            curr = curr->children[index];
        }
        return curr->isEndOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for (char c : prefix) {
            int index = c - 'a';
            if (curr->children[index] == nullptr) {
                return false;
            }
            curr = curr->children[index];
        }
        return true;
    }
};

int main() {
    Trie* obj = new Trie();
    obj->insert("apple");
    
    cout << "Search 'apple': " << (obj->search("apple") ? "True" : "False") << endl; // True
    cout << "Search 'app': " << (obj->search("app") ? "True" : "False") << endl;     // False
    cout << "Starts with 'app': " << (obj->startsWith("app") ? "True" : "False") << endl; // True
    
    obj->insert("app");
    cout << "Search 'app' after insert: " << (obj->search("app") ? "True" : "False") << endl; // True

    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** 
  - `insert`, `search`, `startsWith`: `O(L)` where `L` is the length of the word/prefix.
- **Space Complexity:** `O(T * L)` where `T` is total number of words and `L` is average length of word for building the Trie. Each node takes `26` pointers.
