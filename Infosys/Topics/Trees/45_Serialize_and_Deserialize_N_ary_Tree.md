# Serialize and Deserialize N-ary Tree

## Difficulty
Hard

## Probability
★★★☆☆

## Asked In
Infosys SP
Similar Companies: Amazon, Microsoft, ByteDance

## Topic
Trees

## Pattern
DFS / String Parsing

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work.

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `0 <= Node.val <= 10^4`
- The height of the n-ary tree is less than or equal to `1000`
- Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

## Input / Output
- Return `string` for serialization.
- Return `Node*` for deserialization.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
Explanation: Example uses a level order representation.
```

**Example 2:**
```
Input: root = []
Output: []
```

## Edge Cases
- Empty tree. Returns `""`.
- Tree with a single root and 0 children.

## Intuition
Unlike Binary Trees which only have exactly 2 children (left and right), N-ary trees have a dynamically sized list of children: `vector<Node*> children`.
If we serialize a Binary Tree, we know `1, 2, #, #, 3, #, #` means node 1 has child 2, and child 2 has nulls, etc.
But for an N-ary tree, how do we know when the children of a specific node end? We need a **delimiter**.
We can use a Preorder DFS. For each node, we append its value. Then we recursively append all of its children. Finally, after all children are appended, we append a special delimiter (like `#`) to mark "end of children list for this node".

**Example format:**
Tree: Root 1 has children 3, 2, 4. Node 3 has children 5, 6.
Serialization: `1,3,5,#,6,#,#,2,#,4,#,#,`
Wait, a cleaner format includes the *size* of the children array directly instead of `#`!
`[value, num_children, children...]`.
Tree: `1` has 3 children `(3, 2, 4)`. `3` has 2 children `(5, 6)`. `2` has 0. `4` has 0.
String: `1,3, 3,2, 5,0, 6,0, 2,0, 4,0,`
This is MUCH easier to parse! We read a value, we read its child count, and then we run a loop `for(int i=0; i<count; i++)` to parse its children recursively.

## Brute Force Approach
N/A - String parsing logic.

## Optimal Approach (Preorder with Child Count)
**Detailed explanation:**
**Serialize:**
1. If `root == nullptr`, return `""`.
2. Append `to_string(root->val) + ","`.
3. Append `to_string(root->children.size()) + ","`.
4. Iterate through `root->children`. Recursively append their serialized strings.

**Deserialize:**
1. If `data == ""`, return `nullptr`.
2. Use a `stringstream ss(data)` and a helper function `decode(stringstream& ss)`.
3. Read the node value: `string valStr; getline(ss, valStr, ',');`. Convert to integer.
4. Read the child count: `string sizeStr; getline(ss, sizeStr, ',');`. Convert to integer.
5. Create `Node* root = new Node(stoi(valStr));`.
6. Run a loop `for (int i = 0; i < stoi(sizeStr); i++)`:
   - Recursively call `decode(ss)` and push the returned child into `root->children.push_back()`.
7. Return `root`.

**Time Complexity:** $O(N)$ for both serialization and deserialization because every node is visited exactly once.
**Space Complexity:** $O(N)$ for the recursion stack (up to $H$) and the output string storage.

## C++ Solution

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

#include <string>
#include <vector>
#include <sstream>
using namespace std;

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(Node* root) {
        if (root == nullptr) {
            return "";
        }
        
        string s = to_string(root->val) + "," + to_string(root->children.size()) + ",";
        
        // Recursively serialize children
        for (Node* child : root->children) {
            s += serialize(child);
        }
        
        return s;
    }

    // Decodes your encoded data to tree.
    Node* deserialize(string data) {
        if (data.empty()) return nullptr;
        
        stringstream ss(data);
        return decode(ss);
    }
    
private:
    Node* decode(stringstream& ss) {
        string valStr, sizeStr;
        
        // Read the node's value and the number of its children
        getline(ss, valStr, ',');
        getline(ss, sizeStr, ',');
        
        // Construct the node
        Node* root = new Node(stoi(valStr));
        int numChildren = stoi(sizeStr);
        
        // Recursively decode and attach the children
        for (int i = 0; i < numChildren; i++) {
            root->children.push_back(decode(ss));
        }
        
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
```

## Dry Run
Tree: Root 1 -> [3, 2]. 3 -> [5, 6]. 2 -> [].
- `serialize(1)`: `1,2,`
  - Child 1 (3): `serialize(3)` -> `3,2,`
    - Child 1 (5): `serialize(5)` -> `5,0,`
    - Child 2 (6): `serialize(6)` -> `6,0,`
  - Child 2 (2): `serialize(2)` -> `2,0,`
Output String: `1,2,3,2,5,0,6,0,2,0,`

Deserialize:
- `decode()` reads 1, count 2. Loop runs 2 times.
  - Iteration 1: calls `decode()`. Reads 3, count 2. Loop runs 2 times.
    - Iteration 1: calls `decode()`. Reads 5, count 0. Returns `Node(5)`. Attached to 3.
    - Iteration 2: calls `decode()`. Reads 6, count 0. Returns `Node(6)`. Attached to 3.
    - Returns `Node(3)` to 1.
  - Iteration 2: calls `decode()`. Reads 2, count 0. Returns `Node(2)`. Attached to 1.
- Returns `Node(1)`. Perfectly reconstructed!

## Common Mistakes
- **Trying to use `#` like binary trees:** Unlike binary trees where every node has exactly 2 children (so you know 2 `#`s means a leaf), N-ary trees have dynamic sizes. Just using `#` creates ambiguity unless you also use brackets `[ ]` which is annoying to parse. Storing the size directly as an integer is brilliant and guarantees an $O(1)$ parsing loop per node.

## Similar Problems
- Serialize and Deserialize Binary Tree
- Serialize and Deserialize BST
