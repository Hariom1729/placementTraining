# Problem 20: Accounts Merge

## Problem Statement
Given a list of `accounts` where each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails **in sorted order**. The accounts themselves can be returned in any order.

## Constraints
- `1 <= accounts.length <= 1000`
- `2 <= accounts[i].length <= 10`
- `1 <= accounts[i][j].length <= 30`
- `accounts[i][0]` consists of English letters.

---

## Approach: Disjoint Set Union (DSU / Union-Find)

We need to group emails together. Disjoint Set is the perfect data structure for dynamic connectivity problems.

1. Implement a `DisjointSet` class with `findUPar()` (find ultimate parent with path compression) and `unionBySize()`.
2. Iterate through all accounts. For each email, map it to the index of its account (0 to n-1) using a Hash Map (`unordered_map<string, int>`).
   - If an email is already in the map (meaning another account has this email), perform a **Union** between the current account index and the stored account index.
3. After building the DSU, group the emails. Create an array of strings `mergedMail[n]`. Iterate through the Hash Map, find the ultimate parent of the mapped index, and push the email to that parent's array.
4. Finally, construct the answer. For every index `i` from `0` to `n-1` where `mergedMail[i]` is not empty:
   - Sort the emails.
   - Insert the name `accounts[i][0]` at the beginning.
   - Add to result.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class DisjointSet {
    vector<int> parent, size;
public:
    DisjointSet(int n) {
        parent.resize(n);
        size.resize(n, 1);
        for(int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    int findUPar(int node) {
        if (node == parent[node]) return node;
        return parent[node] = findUPar(parent[node]); // Path compression
    }
    
    void unionBySize(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) return;
        
        if (size[ulp_u] < size[ulp_v]) {
            parent[ulp_u] = ulp_v;
            size[ulp_v] += size[ulp_u];
        } else {
            parent[ulp_v] = ulp_u;
            size[ulp_u] += size[ulp_v];
        }
    }
};

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        int n = accounts.size();
        DisjointSet ds(n);
        
        unordered_map<string, int> mailNode;
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < accounts[i].size(); j++) {
                string mail = accounts[i][j];
                // If mail not seen before, map it to account index i
                if (mailNode.find(mail) == mailNode.end()) {
                    mailNode[mail] = i;
                } else {
                    // If seen, union the current index i with the previously mapped index
                    ds.unionBySize(i, mailNode[mail]);
                }
            }
        }
        
        // Group emails by their ultimate parent
        vector<string> mergedMail[n];
        for (auto it : mailNode) {
            string mail = it.first;
            int node = ds.findUPar(it.second);
            mergedMail[node].push_back(mail);
        }
        
        vector<vector<string>> ans;
        for (int i = 0; i < n; i++) {
            if (mergedMail[i].size() == 0) continue;
            
            sort(mergedMail[i].begin(), mergedMail[i].end());
            
            vector<string> temp;
            temp.push_back(accounts[i][0]); // Name
            for (auto it : mergedMail[i]) {
                temp.push_back(it); // Emails
            }
            ans.push_back(temp);
        }
        
        return ans;
    }
};

int main() {
    Solution sol;
    vector<vector<string>> accounts = {
        {"John","johnsmith@mail.com","john_newyork@mail.com"},
        {"John","johnsmith@mail.com","john00@mail.com"},
        {"Mary","mary@mail.com"},
        {"John","johnnybravo@mail.com"}
    };
    
    vector<vector<string>> res = sol.accountsMerge(accounts);
    for (auto acc : res) {
        for (string s : acc) cout << s << " | ";
        cout << "\n";
    }
    
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** `O(N \cdot M \log(N \cdot M))` where `N` is the number of accounts and `M` is the max emails per account. Sorting the grouped emails dominates the time complexity. DSU operations take near `O(1)` time.
- **Space Complexity:** `O(N \cdot M)` for the Hash Map and the answer array.
