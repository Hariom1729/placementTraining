# Machine Coding: ATM System

## 1. Requirements

Design an ATM machine:
1. **Authentication:** Authenticate user via Card Number and PIN.
2. **Check Balance:** View account balance.
3. **Withdraw Cash:** Deduct balance and output cash.
4. **Denomination Logic:** The ATM must dispense notes optimally (e.g., preference for larger notes) and ensure it has enough physical cash.

## 2. Entities
- `Card`: Number, PIN, linked Account ID.
- `Account`: Balance.
- `CashDispenser`: Keeps track of physical notes (500s, 100s, etc.).
- `ATM`: Orchestrates the flow.

## 3. C++ Implementation

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Account {
public:
    string accId;
    double balance;
    Account() {}
    Account(string i, double b) : accId(i), balance(b) {}
};

class Card {
public:
    string cardNum;
    int pin;
    string accId;
    Card() {}
    Card(string c, int p, string a) : cardNum(c), pin(p), accId(a) {}
};

class CashDispenser {
private:
    int notes500;
    int notes100;

public:
    CashDispenser(int n500, int n100) : notes500(n500), notes100(n100) {}

    bool canDispense(int amount) {
        int totalCash = (notes500 * 500) + (notes100 * 100);
        if (amount > totalCash || amount % 100 != 0) return false;

        // Greedy approach to check if we can form the amount
        int req500 = min(amount / 500, notes500);
        int remAmount = amount - (req500 * 500);
        int req100 = remAmount / 100;

        return req100 <= notes100;
    }

    void dispense(int amount) {
        int req500 = min(amount / 500, notes500);
        int remAmount = amount - (req500 * 500);
        int req100 = remAmount / 100;

        notes500 -= req500;
        notes100 -= req100;
        cout << "[Dispensed] 500x" << req500 << " | 100x" << req100 << "\n";
    }
};

class ATM {
private:
    unordered_map<string, Account> accounts;
    unordered_map<string, Card> cards;
    CashDispenser dispenser;
    string currentSessionAccId = "";

public:
    ATM(int n500, int n100) : dispenser(n500, n100) {}

    void setupData() {
        accounts["A1"] = Account("A1", 10000);
        cards["C1"] = Card("C1", 1234, "A1");
    }

    bool authenticate(string cardNum, int pin) {
        if(cards.find(cardNum) != cards.end() && cards[cardNum].pin == pin) {
            currentSessionAccId = cards[cardNum].accId;
            cout << "[Success] Authentication successful.\n";
            return true;
        }
        cout << "[Error] Invalid Card or PIN.\n";
        return false;
    }

    void checkBalance() {
        if(currentSessionAccId == "") {
            cout << "[Error] Please authenticate first.\n";
            return;
        }
        cout << "Current Balance: Rs." << accounts[currentSessionAccId].balance << "\n";
    }

    void withdraw(int amount) {
        if(currentSessionAccId == "") {
            cout << "[Error] Please authenticate first.\n";
            return;
        }
        if(amount > accounts[currentSessionAccId].balance) {
            cout << "[Error] Insufficient account balance.\n";
            return;
        }
        if(!dispenser.canDispense(amount)) {
            cout << "[Error] ATM cannot dispense this amount (Hardware limitation/No cash).\n";
            return;
        }

        // Process
        accounts[currentSessionAccId].balance -= amount;
        dispenser.dispense(amount);
        cout << "[Success] Please collect your cash. New Balance: Rs." << accounts[currentSessionAccId].balance << "\n";
    }

    void logout() {
        currentSessionAccId = "";
        cout << "Logged out successfully.\n";
    }
};

int main() {
    ATM atm(10, 20); // 10x500 = 5000, 20x100 = 2000. Total ATM cash = 7000
    atm.setupData();

    atm.authenticate("C1", 1234);
    atm.checkBalance();
    atm.withdraw(1200); // Should dispense 2x500 and 2x100
    atm.withdraw(8000); // Should fail (ATM doesn't have 8000 physical cash)
    atm.logout();

    return 0;
}
```

## 4. Interview Discussion
- **State Machine:** ATMs are perfect examples of State Machines (Idle State -> HasCardState -> AuthenticatedState).
- **Greedy Coin Change:** The denomination logic uses a greedy approach, which works for standard currencies like Indian Rupees or US Dollars, but Dynamic Programming is needed for arbitrary currency denominations.
