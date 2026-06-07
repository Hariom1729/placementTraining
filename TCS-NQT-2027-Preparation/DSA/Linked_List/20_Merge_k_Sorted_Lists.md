# Problem 20: Merge k Sorted Lists

## Problem Statement
You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

## Input Format
- A vector of `ListNode*` pointers `lists`.

## Output Format
- The `head` of the merged sorted linked list.

## Constraints
- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`

---

## Approach: Min-Heap (Priority Queue)

Instead of merging lists one by one (which is slow), we can use a Min-Heap. The heap will always contain at most `k` elements—the current smallest element from each of the `k` lists.

1. Create a `priority_queue` (Min-Heap).
2. Insert the `head` node of all `k` linked lists into the Min-Heap.
3. Extract the smallest node from the heap and add it to our resultant merged list.
4. If the extracted node has a `next` node, push that `next` node into the Min-Heap.
5. Repeat steps 3 and 4 until the heap is empty.

---

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// Custom Comparator for the Priority Queue
struct compare {
    bool operator()(const ListNode* l1, const ListNode* l2) {
        return l1->val > l2->val; // Min-Heap logic
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, compare> pq;
        
        // Push the head of all k lists into the Priority Queue
        for (ListNode* listHead : lists) {
            if (listHead != NULL) {
                pq.push(listHead);
            }
        }
        
        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;
        
        // Process the heap
        while (!pq.empty()) {
            // Get the smallest node
            ListNode* minNode = pq.top();
            pq.pop();
            
            // Add it to the merged list
            tail->next = minNode;
            tail = tail->next;
            
            // If there are more nodes in the list of the extracted node, push the next one
            if (minNode->next != NULL) {
                pq.push(minNode->next);
            }
        }
        
        ListNode* result = dummy->next;
        delete dummy;
        return result;
    }
};

// Main function omitted due to array of linked list setup complexity,
// but the algorithm is optimal.
```

---

## Complexity Analysis

- **Time Complexity:** `O(N log k)` where `N` is the total number of nodes across all lists, and `k` is the number of linked lists. Inserting/extracting from a heap of size `k` takes `O(log k)` time, and we do this `N` times.
- **Space Complexity:** `O(k)`. The priority queue holds at most `k` elements at any given time.
