# Design HashSet

## Difficulty
Easy

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft

## Topic
Hashing / Design

## Pattern
Array / Linked List / Hashing

## Problem Statement
Design a HashSet without using any built-in hash table libraries.

Implement `MyHashSet` class:
- `void add(key)` Inserts the value `key` into the HashSet.
- `bool contains(key)` Returns whether the value `key` exists in the HashSet or not.
- `void remove(key)` Removes the value `key` in the HashSet. If `key` does not exist in the HashSet, do nothing.

## Constraints
- `0 <= key <= 10^6`
- At most `10^4` calls will be made to `add`, `remove`, and `contains`.

## Input
- Array of commands and parameters.

## Output
- Return values from the methods.

## Sample Test Cases

**Example 1:**
```
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
```

## Edge Cases
- Adding a key that is already in the set (should do nothing, avoid duplicates).
- Removing a key that doesn't exist (should not crash).

## Intuition
A HashSet is exactly like a HashMap, except it only stores `keys`, not `(key, value)` pairs.
We use the exact same logic as `Design HashMap`: an array of buckets, where each bucket is a Linked List.
When we `add(key)`, we hash the key to find the bucket. We traverse the bucket to see if the key already exists. If it does, we do nothing! If it doesn't, we append it.

## Optimal Approach (Chaining)
**Detailed explanation:**
1. Create a `vector<list<int>> buckets` initialized to size `10007` (a prime number).
2. Create `int hash(int key)` that returns `key % 10007`.
3. `add(key)`: 
   - Get the bucket index via `hash(key)`.
   - Traverse the linked list. If `key` is found, `return`.
   - If not found, `push_back(key)`.
4. `remove(key)`:
   - Get the bucket index via `hash(key)`.
   - Traverse the linked list. If `key` is found, `erase` the iterator and `return`.
5. `contains(key)`:
   - Get the bucket index via `hash(key)`.
   - Traverse the linked list. If `key` is found, `return true`.
   - If loop finishes, `return false`.

**Time Complexity:** Average $O(1)$, Worst Case $O(N)$ for highly clustered collisions.
**Space Complexity:** $O(N + M)$ for keys and buckets.

## C++ Solution

```cpp
#include <vector>
#include <list>
using namespace std;

class MyHashSet {
private:
    int SIZE;
    vector<list<int>> buckets;
    
    int hash(int key) {
        return key % SIZE;
    }

public:
    MyHashSet() {
        SIZE = 10007; // Prime size
        buckets.resize(SIZE);
    }
    
    void add(int key) {
        int index = hash(key);
        // Avoid adding duplicates
        for (auto it = buckets[index].begin(); it != buckets[index].end(); ++it) {
            if (*it == key) {
                return; // Already exists
            }
        }
        buckets[index].push_back(key);
    }
    
    void remove(int key) {
        int index = hash(key);
        for (auto it = buckets[index].begin(); it != buckets[index].end(); ++it) {
            if (*it == key) {
                buckets[index].erase(it);
                return;
            }
        }
    }
    
    bool contains(int key) {
        int index = hash(key);
        for (auto it = buckets[index].begin(); it != buckets[index].end(); ++it) {
            if (*it == key) {
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
```

## Dry Run
`add(5)`:
- `hash(5) = 5`. `buckets[5]` is empty. Pushes `5`.
`add(10012)`:
- `hash(10012) = 10012 % 10007 = 5`.
- `buckets[5]` has `5`. Not equal to `10012`. Pushes `10012`.
- `buckets[5]` contains `[5, 10012]`.
`contains(5)`:
- `hash(5) = 5`. Loops `buckets[5]`. Finds `5`. Returns `true`.

## Common Mistakes
- **Using a massive boolean array:** `bool arr[1000001]`. This is completely missing the point of a hashing interview question. You must manually implement bucketing and chaining.

## Similar Problems
- Design HashMap
