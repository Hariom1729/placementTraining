# Serialize and Deserialize Binary Tree

## Difficulty
Hard

## Probability
★★★★☆

## Asked In
Infosys SP
Similar Companies: Amazon, Google, Facebook, Microsoft

## Topic
Trees

## Pattern
Level Order Traversal (BFS) / String Parsing

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-1000 <= Node.val <= 1000`

## Input
- `serialize`: `root` pointer of the Binary Tree.
- `deserialize`: `string` representing the serialized tree.

## Output
- `serialize`: Return a string.
- `deserialize`: Return a `TreeNode*`.

## Sample Test Cases

**Example 1:**
```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

**Example 2:**
```
Input: root = []
Output: []
```

## Edge Cases
- Empty tree. The string should be `""` or `"#"`.
- Single node tree.
- A highly skewed tree.

## Intuition
**Serialization:**
We can use a Level Order Traversal (BFS) using a queue.
- If a node is not null, we append its value followed by a comma `,`.
- If a node is null, we append a special character like `#` followed by a comma `,`.
- For example, tree `[1, 2, 3, null, null, 4, 5]` becomes `"1,2,3,#,#,4,5,#,#,#,#,"`.

**Deserialization:**
We can reconstruct the tree using another BFS queue.
- First, we parse the string into tokens using a `stringstream` and `getline` with the comma delimiter.
- The very first token is the root. We push it to the queue.
- While the queue is not empty, we pop a node. The *next* token in our stream is its left child. The *token after that* is its right child. We create these children, attach them to the popped node, and if they are not `#`, we push them to the queue!

## Brute Force Approach
N/A - The string processing BFS approach is standard.

## Optimal Approach
**Detailed explanation:**
**Serialize:**
1. If `root == nullptr`, return `""`.
2. Use a `queue<TreeNode*> q`. Push `root`.
3. Use a `string s = ""`.
4. While `q` is not empty:
   - Pop `curr`.
   - If `curr == nullptr`, append `"#,"` to `s`.
   - If `curr != nullptr`, append `to_string(curr->val) + ","` to `s`, and push `curr->left` and `curr->right` into `q` (even if they are null).

**Deserialize:**
1. If `data == ""`, return `nullptr`.
2. Use `stringstream s(data);` to read tokens separated by commas.
3. `string str; getline(s, str, ',');` reads the first value.
4. Create the root `TreeNode* root = new TreeNode(stoi(str));`.
5. Use a `queue<TreeNode*> q`. Push `root`.
6. While `q` is not empty:
   - Pop `curr`.
   - Read the left child: `getline(s, str, ',')`.
     - If `str != "#"`, create a new node, `curr->left = node`, and push `node` to `q`.
   - Read the right child: `getline(s, str, ',')`.
     - If `str != "#"`, create a new node, `curr->right = node`, and push `node` to `q`.

**Time Complexity:** $O(N)$ for both serialization and deserialization since every node is processed once.
**Space Complexity:** $O(N)$ for the queue and the output string.

## C++ Solution

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <string>
#include <queue>
#include <sstream>
using namespace std;

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (root == nullptr) return "";
        
        string s = "";
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* curr = q.front();
            q.pop();
            
            if (curr == nullptr) {
                s += "#,";
            } else {
                s += to_string(curr->val) + ",";
                // Push children EVEN IF NULL, to preserve structure
                q.push(curr->left);
                q.push(curr->right);
            }
        }
        
        return s;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data.length() == 0) return nullptr;
        
        stringstream s(data);
        string str;
        
        // Read the very first token (the root)
        getline(s, str, ',');
        TreeNode* root = new TreeNode(stoi(str));
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* curr = q.front();
            q.pop();
            
            // Read left child
            getline(s, str, ',');
            if (str != "#") {
                curr->left = new TreeNode(stoi(str));
                q.push(curr->left);
            }
            
            // Read right child
            getline(s, str, ',');
            if (str != "#") {
                curr->right = new TreeNode(stoi(str));
                q.push(curr->right);
            }
        }
        
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));
```

## Dry Run
Serialize `[1, 2, 3]`:
- Queue: `[1]`
- Pop 1. String `"1,"`. Push 2, 3. Queue: `[2, 3]`
- Pop 2. String `"1,2,"`. Push null, null. Queue: `[3, null, null]`
- Pop 3. String `"1,2,3,"`. Push null, null. Queue: `[null, null, null, null]`
- Pop nulls... String becomes `"1,2,3,#,#,#,#,"`.

Deserialize `"1,2,3,#,#,#,#,"`:
- `getline` -> `"1"`. `root = 1`. Queue `[1]`.
- Pop 1.
  - `getline` -> `"2"`. `1->left = 2`. Queue `[2]`.
  - `getline` -> `"3"`. `1->right = 3`. Queue `[2, 3]`.
- Pop 2.
  - `getline` -> `"#"`. `2->left = null`.
  - `getline` -> `"#"`. `2->right = null`.
- Pop 3.
  - `getline` -> `"#"`. `3->left = null`.
  - `getline` -> `"#"`. `3->right = null`.
- End. Return tree.

## Common Mistakes
- **Using Preorder without '#' markers:** If you try to serialize using DFS without null markers, you can never reconstruct the tree because you don't know where a branch ends. E.g. `[1, 2]` vs `[1, null, 2]` would both serialize to `"1, 2"`.
- **Not handling negative numbers:** The C++ `stoi()` correctly handles negative numbers like `"-12"`, but if you write a custom manual integer parser, you might forget the minus sign. `stringstream` makes it foolproof.

## Similar Problems
- Serialize and Deserialize BST (Can be done without '#' markers because BST properties define structure).
