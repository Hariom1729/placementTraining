# Problem 13: Online Stock Span

## Problem Statement
Design a class that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

Implement the `StockSpanner` class:
- `StockSpanner()` Initializes the object.
- `int next(int price)` Returns the span of the stock's price given that today's price is `price`.

## Constraints
- `1 <= price <= 10^5`
- At most `10^4` calls will be made to `next`.

---

## Approach: Monotonic Decreasing Stack

We want to find how many previous consecutive days had a price `<= current_price`.
We can use a stack that stores pairs of `(price, span)`.

1. When `next(price)` is called, initialize `span = 1` (for the current day).
2. While the stack is not empty and the top of the stack has a price `<= price`:
   - It means the previous day's price was smaller. Thus, its span also contributes to the current day's span.
   - `span += st.top().span`
   - `st.pop()`
3. Push the new `{price, span}` to the stack.
4. Return `span`.

This keeps the stack strictly monotonically decreasing in terms of prices.

---

## C++ Solution

```cpp
#include <iostream>
#include <stack>
using namespace std;

class StockSpanner {
private:
    // Pair of <price, span>
    stack<pair<int, int>> st;

public:
    StockSpanner() {
        
    }
    
    int next(int price) {
        int span = 1;
        
        while (!st.empty() && st.top().first <= price) {
            span += st.top().second;
            st.pop();
        }
        
        st.push({price, span});
        return span;
    }
};

int main() {
    StockSpanner stockSpanner;
    cout << stockSpanner.next(100) << " "; // Expected: 1
    cout << stockSpanner.next(80) << " ";  // Expected: 1
    cout << stockSpanner.next(60) << " ";  // Expected: 1
    cout << stockSpanner.next(70) << " ";  // Expected: 2 (70, 60)
    cout << stockSpanner.next(60) << " ";  // Expected: 1
    cout << stockSpanner.next(85) << " ";  // Expected: 6
    cout << "\n";
    return 0;
}
```

---

## Complexity Analysis

- **Time Complexity:** Amortized `O(1)` per `next` call. Over all `N` calls, each element is pushed and popped at most once, making total time `O(N)`.
- **Space Complexity:** `O(N)` for the stack.
