# Programming: Simulation and Implementation

These are mini machine-coding problems often asked in Round 3 to test your ability to convert real-world logic into code.

## 1. Text Justification (Word Wrap)
**Problem:** Given an array of words and a maximum width, format the text such that each line has exactly `maxWidth` characters and is fully justified.
**C++ Solution:**
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> fullJustify(vector<string>& words, int maxWidth) {
    vector<string> res;
    int i = 0, n = words.size();

    while (i < n) {
        int j = i + 1;
        int lineLength = words[i].length();
        while (j < n && (lineLength + words[j].length() + (j - i - 1) < maxWidth)) {
            lineLength += words[j].length();
            j++;
        }

        int diff = maxWidth - lineLength;
        int numberOfWords = j - i;
        string line = words[i];
        
        if (numberOfWords == 1 || j >= n) {
            // Left justify for the last line or lines with 1 word
            for (int k = i + 1; k < j; k++) line += " " + words[k];
            while (line.length() < maxWidth) line += " ";
            res.push_back(line);
        } else {
            // Fully justify
            int spaces = diff / (numberOfWords - 1);
            int extraSpaces = diff % (numberOfWords - 1);
            for (int k = i + 1; k < j; k++) {
                int spacesToApply = spaces + (extraSpaces-- > 0 ? 1 : 0);
                for (int s = 0; s < spacesToApply; s++) line += " ";
                line += words[k];
            }
            res.push_back(line);
        }
        i = j;
    }
    return res;
}

int main() {
    vector<string> words = {"This", "is", "an", "example", "of", "text", "justification."};
    for(string line : fullJustify(words, 16)) {
        cout << "'" << line << "'\n";
    }
    return 0;
}
```

## 2. LRU Cache Implementation
**Problem:** Implement the LRU (Least Recently Used) cache logic using a doubly-linked list and a hash map.
**C++ Solution:**
```cpp
#include <iostream>
#include <unordered_map>

using namespace std;

class Node {
public:
    int key, value;
    Node* prev;
    Node* next;
    Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
};

class LRUCache {
private:
    int capacity;
    unordered_map<int, Node*> map;
    Node* head;
    Node* tail;

    void remove(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void insert(Node* node) {
        node->next = head->next;
        node->next->prev = node;
        head->next = node;
        node->prev = head;
    }

public:
    LRUCache(int cap) : capacity(cap) {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;
    }

    int get(int key) {
        if (map.find(key) == map.end()) return -1;
        Node* node = map[key];
        remove(node);
        insert(node);
        return node->value;
    }

    void put(int key, int value) {
        if (map.find(key) != map.end()) {
            remove(map[key]);
        }
        if (map.size() == capacity) {
            remove(tail->prev);
            map.erase(tail->prev->key);
        }
        Node* newNode = new Node(key, value);
        insert(newNode);
        map[key] = newNode;
    }
};

int main() {
    LRUCache cache(2);
    cache.put(1, 1);
    cache.put(2, 2);
    cout << cache.get(1) << "\n";    // returns 1
    cache.put(3, 3);                 // evicts key 2
    cout << cache.get(2) << "\n";    // returns -1 (not found)
    cache.put(4, 4);                 // evicts key 1
    cout << cache.get(1) << "\n";    // returns -1 (not found)
    cout << cache.get(3) << "\n";    // returns 3
    cout << cache.get(4) << "\n";    // returns 4
    return 0;
}
```

*(Other Simulation topics heavily favored by Zoho include basic Snake and Ladder simulators, Tic-Tac-Toe state checkers, and multi-elevator simulators. The key is isolating distinct logic blocks into helper methods.)*
