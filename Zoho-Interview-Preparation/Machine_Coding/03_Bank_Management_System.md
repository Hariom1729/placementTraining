# Machine Coding: Bank Management System

## 1. Requirements

Design a basic Bank Management System:
1. **Create Account:** Open a new bank account.
2. **Deposit:** Add money to an account.
3. **Withdraw:** Withdraw money, ensuring sufficient balance.
4. **Transfer:** Transfer money between two accounts.
5. **Statement:** View the transaction history of an account.

## 2. Entities
- `Account`: Account Number, Customer Name, Balance, Transaction History.
- `Transaction`: ID, Type (Credit/Debit), Amount, Date.
- `Bank`: Collection of all accounts.

## 3. C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Transaction {
public:
    string type;
    double amount;
    string details;

    Transaction(string t, double a, string d) : type(t), amount(a), details(d) {}
};

class Account {
private:
    int accNum;
    string name;
    double balance;
    vector<Transaction> history;

public:
    Account() {}
    Account(int id, string n, double b) : accNum(id), name(n), balance(b) {
        history.push_back(Transaction("CREDIT", b, "Initial Deposit"));
    }

    int getAccNum() { return accNum; }
    double getBalance() { return balance; }

    void deposit(double amt) {
        balance += amt;
        history.push_back(Transaction("CREDIT", amt, "Self Deposit"));
        cout << "[Success] Deposited " << amt << ". New Balance: " << balance << "\n";
    }

    bool withdraw(double amt) {
        if(balance >= amt) {
            balance -= amt;
            history.push_back(Transaction("DEBIT", amt, "Self Withdrawal"));
            cout << "[Success] Withdrew " << amt << ". New Balance: " << balance << "\n";
            return true;
        }
        cout << "[Error] Insufficient funds.\n";
        return false;
    }

    void transferIn(double amt, int fromAcc) {
        balance += amt;
        history.push_back(Transaction("CREDIT", amt, "Transfer from " + to_string(fromAcc)));
    }

    void transferOut(double amt, int toAcc) {
        balance -= amt;
        history.push_back(Transaction("DEBIT", amt, "Transfer to " + to_string(toAcc)));
    }

    void printStatement() {
        cout << "--- Statement for Account " << accNum << " (" << name << ") ---\n";
        for(auto& t : history) {
            cout << "[" << t.type << "] Rs." << t.amount << " | " << t.details << "\n";
        }
        cout << "Current Balance: Rs." << balance << "\n";
    }
};

class Bank {
private:
    unordered_map<int, Account> accounts;
    int nextAccNum = 1001;

public:
    void openAccount(string name, double initialDeposit) {
        int id = nextAccNum++;
        accounts[id] = Account(id, name, initialDeposit);
        cout << "[Success] Account opened for " << name << " with ID: " << id << "\n";
    }

    void deposit(int accNum, double amt) {
        if(accounts.find(accNum) != accounts.end()) {
            accounts[accNum].deposit(amt);
        } else cout << "[Error] Account not found.\n";
    }

    void withdraw(int accNum, double amt) {
        if(accounts.find(accNum) != accounts.end()) {
            accounts[accNum].withdraw(amt);
        } else cout << "[Error] Account not found.\n";
    }

    void transfer(int fromAcc, int toAcc, double amt) {
        if(accounts.find(fromAcc) == accounts.end() || accounts.find(toAcc) == accounts.end()) {
            cout << "[Error] Invalid account(s).\n";
            return;
        }
        if(accounts[fromAcc].getBalance() >= amt) {
            accounts[fromAcc].transferOut(amt, toAcc);
            accounts[toAcc].transferIn(amt, fromAcc);
            cout << "[Success] Transfer of " << amt << " successful.\n";
        } else {
            cout << "[Error] Insufficient funds for transfer.\n";
        }
    }

    void printStatement(int accNum) {
        if(accounts.find(accNum) != accounts.end()) {
            accounts[accNum].printStatement();
        } else cout << "[Error] Account not found.\n";
    }
};

int main() {
    Bank myBank;
    myBank.openAccount("Alice", 5000);
    myBank.openAccount("Bob", 2000);

    myBank.transfer(1001, 1002, 1000);
    myBank.withdraw(1001, 5000); // Should fail
    myBank.deposit(1002, 500);

    myBank.printStatement(1001);
    myBank.printStatement(1002);

    return 0;
}
```

## 4. Interview Discussion
- **ACID Properties:** How do we ensure Atomicity during a transfer? (If the debit succeeds but the credit fails, money is lost). In real systems, transfers are wrapped in DB transactions.
- **Double Entry Accounting:** Every debit must have a corresponding credit.
