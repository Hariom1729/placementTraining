# Design HashMap

## Difficulty
Easy

## Probability
★★★★☆

## Asked In
Infosys SP
Infosys DSE
Similar Companies: Amazon, Microsoft, LinkedIn

## Topic
Hashing / Design

## Pattern
Array / Linked List / Hashing

## Problem Statement
Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:
- `MyHashMap()` initializes the object with an empty map.
- `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the `key` already exists in the map, update the corresponding `value`.
- `int get(int key)` returns the `value` to which the specified `key` is mapped, or `-1` if this map contains no mapping for the `key`.
- `void remove(int key)` removes the `key` and its corresponding `value` if the map contains the mapping for the `key`.

## Constraints
- `0 <= key, value <= 10^6`
- At most `10^4` calls will be made to `put`, `get`, and `remove`.

## Input
- Array of commands and parameters.

## Output
- Return values from the methods.

## Sample Test Cases

**Example 1:**
```
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
```

## Edge Cases
- Updating an existing key.
- Removing a key that doesn't exist.
- Getting a key that was just removed.

## Intuition
The core idea behind a HashMap is to map a massive space of potential keys to a smaller, fixed-size array using a **Hash Function**.
Since the maximum key is `10^6`, we *could* just create a giant array of size `10^6 + 1` (a Direct Address Table). But in real interviews, the key space is usually arbitrary (like Strings or billions of integers).
Therefore, we must demonstrate **Collision Resolution** using **Chaining**.

We create an array of buckets. Let's choose a prime number for the size, say `10007`.
- **Hash Function:** `key % 10007` gives us the bucket index.
- Since multiple keys can map to the exact same index (a collision), each bucket will not hold just one value, but a **Linked List** (or `vector`) of `(key, value)` pairs!
- `put`: Find the bucket. Scan the list. If key exists, update value. Else, append `(key, value)` to the list.
- `get`: Find the bucket. Scan the list for the key. Return value if found, else `-1`.
- `remove`: Find the bucket. Scan the list for the key. If found, delete it from the list.

## Optimal Approach (Chaining with Vectors / Linked Lists)
**Detailed explanation:**
1. Define a `struct` or use `pair<int, int>` to hold `(key, value)`.
2. Create an array (or `vector`) of `list<pair<int, int>>` named `buckets`. Size it to `10007` or `10000`.
3. Create a helper function `int hash(int key)` that returns `key % SIZE`.
4. `put(key, value)`:
   - Call `hash(key)`. Get a reference to `buckets[hash_index]`.
   - Iterate through the list. If `it->first == key`, update `it->second = value` and return.
   - If loop finishes, `push_back({key, value})`.
5. `get(key)`:
   - Call `hash(key)`. Get a reference to the bucket.
   - Iterate through the list. If `it->first == key`, return `it->second`.
   - If not found, return `-1`.
6. `remove(key)`:
   - Call `hash(key)`. Get a reference to the bucket.
   - Iterate through the list. If `it->first == key`, use `list.erase(it)` and return.

**Time Complexity:** 
- Average Case: $O(1)$ for all operations (assuming a good hash function distributes keys evenly).
- Worst Case: $O(N)$ if all keys collide into the exact same bucket.
**Space Complexity:** $O(N + M)$ where $N$ is the number of keys inserted and $M$ is the number of buckets.

## C++ Solution

```cpp
#include <vector>
#include <list>
#include <utility>
using namespace std;

class MyHashMap {
private:
    int SIZE;
    vector<list<pair<int, int>>> buckets;
    
    // Simple hash function
    int hash(int key) {
        return key % SIZE;
    }

public:
    MyHashMap() {
        SIZE = 10007; // Prime number for better distribution
        buckets.resize(SIZE);
    }
    
    void put(int key, int value) {
        int index = hash(key);
        // Traverse the bucket to see if key already exists
        for (auto it = buckets[index].begin(); it != buckets[index].end(); ++it) {
            if (it->first == key) {
                it->second = value; // Update value
                return;
            }
        }
        // If key doesn't exist, append it
        buckets[index].push_back({key, value});
    }
    
    int get(int key) {
        int index = hash(key);
        for (auto it = buckets[index].begin(); it != buckets[index].end(); ++it) {
            if (it->first == key) {
                return it->second;
            }
        }
        return -1; // Key not found
    }
    
    void remove(int key) {
        int index = hash(key);
        for (auto it = buckets[index].begin(); it != buckets[index].end(); ++it) {
            if (it->first == key) {
                buckets[index].erase(it); // Remove the node from the linked list
                return;
            }
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
```

## Dry Run
`put(1, 1)`:
- `hash(1) = 1`. `buckets[1]` is empty.
- Pushes `{1, 1}` to `buckets[1]`.

`put(10008, 9)`:
- `hash(10008) = 10008 % 10007 = 1`.
- `buckets[1]` has `{1, 1}`. Key `10008` != `1`.
- Pushes `{10008, 9}` to `buckets[1]`.
- `buckets[1]` -> `[{1, 1}, {10008, 9}]` (Collision resolved!)

`get(10008)`:
- `hash(10008) = 1`.
- Loops `buckets[1]`. Sees `1 != 10008`. Next.
- Sees `10008 == 10008`. Returns `9`.

## Common Mistakes
- **Using a massive array (`vector<int> map(1000001, -1)`):** While this passes the tests on LeetCode because the constraints are small, if you do this in an Infosys interview, you will immediately fail the question. The interviewer wants to see you manually implement **Collision Handling** via Linked Lists (Chaining).

## Similar Problems
- Design HashSet
