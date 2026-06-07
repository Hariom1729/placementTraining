# Problem 9: Number of Recent Calls

## Problem Statement
You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.
Implement the `RecentCounter` class:
- `RecentCounter()` Initializes the counter with zero recent requests.
- `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that has happened in the past `3000` milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

It is guaranteed that every call to `ping` uses a strictly larger value of `t` than the previous call.

## Constraints
- `1 <= t <= 10^9`
- Each test case will call `ping` with strictly increasing values of `t`.
- At most `10^4` calls will be made to `ping`.

---

## Approach: Queue

Since the timestamps `t` are strictly increasing, we can use a queue to store the times of the pings.
When a new `ping(t)` arrives:
1. Push `t` into the queue.
2. The valid time range is `[t - 3000, t]`. Any ping that occurred *before* `t - 3000` is expired.
3. While the front of the queue is less than `t - 3000`, `pop` it from the queue.
4. The number of elements remaining in the queue is exactly the number of valid recent pings. Return `queue.size()`.

---

## C++ Solution

```cpp
#include <iostream>
#include <queue>
using namespace std;

class RecentCounter {
private:
    queue<int> q;

public:
    RecentCounter() {
        
    }
    
    int ping(int t) {
        q.push(t);
        
        // Remove pings that are older than t - 3000
        while (!q.empty() && q.front() < t - 3000) {
            q.pop();
        }
        
        return q.size();
    }
};

int main() {
    RecentCounter rc;
    cout << rc.ping(1) << " ";    // Expected: 1
    cout << rc.ping(100) << " ";  // Expected: 2
    cout << rc.ping(3001) << " "; // Expected: 3
    cout << rc.ping(3002) << "\n";// Expected: 3 (ping at 1 is removed)
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** Amortized `O(1)` per `ping` call. Over all calls, each element is pushed and popped at most once.
- **Space Complexity:** `O(W)` where `W` is the maximum number of pings within a 3000ms window (at most 3000).
