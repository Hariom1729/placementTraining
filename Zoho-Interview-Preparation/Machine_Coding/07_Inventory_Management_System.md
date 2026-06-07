# Machine Coding: Inventory Management System

## 1. Requirements

Design an Inventory system:
1. **Add Products:** Manage product catalog.
2. **Manage Stock:** Increase stock when shipments arrive, decrease when sold.
3. **Threshold Alerts:** Alert if a product falls below its reorder threshold.
4. **Process Orders:** Users can order multiple items. Ensure all items are in stock before fulfilling.

## 2. Entities
- `Product`: ID, Name, Price, Quantity, Reorder Threshold.
- `Order`: Order ID, Map of Product IDs to Quantities.

## 3. C++ Implementation

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Product {
public:
    string id;
    string name;
    double price;
    int quantity;
    int reorderThreshold;

    Product() {}
    Product(string i, string n, double p, int q, int t) 
        : id(i), name(n), price(p), quantity(q), reorderThreshold(t) {}
};

class InventorySystem {
private:
    unordered_map<string, Product> catalog;

    void checkThreshold(string pId) {
        Product& p = catalog[pId];
        if(p.quantity <= p.reorderThreshold) {
            cout << "[ALERT] Product '" << p.name << "' is running low! Current stock: " << p.quantity << "\n";
        }
    }

public:
    void addProduct(string id, string name, double price, int qty, int threshold) {
        catalog[id] = Product(id, name, price, qty, threshold);
        cout << "Added product: " << name << "\n";
    }

    void addStock(string id, int qty) {
        if(catalog.find(id) != catalog.end()) {
            catalog[id].quantity += qty;
            cout << "Added " << qty << " units to " << catalog[id].name << ". Total: " << catalog[id].quantity << "\n";
        }
    }

    void processOrder(string orderId, unordered_map<string, int> items) {
        // Validation phase (All or Nothing)
        double totalCost = 0;
        for(auto& item : items) {
            string pId = item.first;
            int reqQty = item.second;
            if(catalog.find(pId) == catalog.end()) {
                cout << "[Order Failed] Product " << pId << " does not exist.\n";
                return;
            }
            if(catalog[pId].quantity < reqQty) {
                cout << "[Order Failed] Insufficient stock for " << catalog[pId].name << ".\n";
                return;
            }
            totalCost += (catalog[pId].price * reqQty);
        }

        // Fulfillment phase
        for(auto& item : items) {
            string pId = item.first;
            int reqQty = item.second;
            catalog[pId].quantity -= reqQty;
            checkThreshold(pId);
        }

        cout << "[Success] Order " << orderId << " fulfilled. Total Cost: Rs." << totalCost << "\n";
    }
};

int main() {
    InventorySystem inv;
    inv.addProduct("P1", "Laptop", 50000, 10, 2);
    inv.addProduct("P2", "Mouse", 1000, 50, 5);

    unordered_map<string, int> myOrder;
    myOrder["P1"] = 1;
    myOrder["P2"] = 47; // Will trigger alert for mouse

    inv.processOrder("ORD-001", myOrder);

    unordered_map<string, int> order2;
    order2["P1"] = 10; // Fails, only 9 laptops left
    inv.processOrder("ORD-002", order2);

    return 0;
}
```

## 4. Interview Discussion
- **All-or-Nothing Transactions:** Why do we loop twice in `processOrder`? The first loop validates *everything*. If we validated and deducted in the same loop, failing on the 3rd item would mean the first 2 items were incorrectly deducted.
