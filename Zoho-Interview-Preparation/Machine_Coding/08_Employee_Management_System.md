# Machine Coding: Employee Management System

## 1. Requirements

Design an Employee Management System:
1. **Add Employees:** ID, Name, Designation, Base Salary.
2. **Departments:** Assign employees to departments.
3. **Payroll Calculation:** Calculate final salary including bonuses and tax deductions.
4. **Hierarchy:** Manager can have multiple subordinates.

## 2. Entities
- `Employee`: ID, Name, Role, Base Salary, Manager ID.
- `Department`: Name, List of Employee IDs.

## 3. C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Employee {
public:
    string id;
    string name;
    string designation;
    double baseSalary;
    string managerId;

    Employee() {}
    Employee(string i, string n, string d, double s, string m = "") 
        : id(i), name(n), designation(d), baseSalary(s), managerId(m) {}

    double calculateNetSalary() {
        double bonus = 0.0;
        if(designation == "Manager") bonus = 0.20 * baseSalary;
        else if(designation == "Developer") bonus = 0.10 * baseSalary;
        
        double gross = baseSalary + bonus;
        double tax = 0.10 * gross; // flat 10% tax
        return gross - tax;
    }
};

class EmployeeSystem {
private:
    unordered_map<string, Employee> employees;
    unordered_map<string, vector<string>> departments; // Dept Name -> Employee IDs
    unordered_map<string, vector<string>> managerSubordinates; // Manager ID -> Subordinate IDs

public:
    void addEmployee(string id, string name, string desig, double sal, string dept, string mgrId = "") {
        employees[id] = Employee(id, name, desig, sal, mgrId);
        departments[dept].push_back(id);
        
        if(mgrId != "") {
            managerSubordinates[mgrId].push_back(id);
        }
        cout << "Added Employee: " << name << "\n";
    }

    void printPayroll() {
        cout << "--- Payroll Report ---\n";
        for(auto& pair : employees) {
            Employee& e = pair.second;
            cout << e.name << " (" << e.designation << ") - Net Salary: Rs." << e.calculateNetSalary() << "\n";
        }
    }

    void printSubordinates(string mgrId) {
        if(employees.find(mgrId) == employees.end()) return;
        
        cout << "--- Subordinates of " << employees[mgrId].name << " ---\n";
        for(string subId : managerSubordinates[mgrId]) {
            cout << "- " << employees[subId].name << " (" << employees[subId].designation << ")\n";
        }
    }
};

int main() {
    EmployeeSystem hrSys;
    
    hrSys.addEmployee("M1", "Alice", "Manager", 100000, "IT");
    hrSys.addEmployee("D1", "Bob", "Developer", 60000, "IT", "M1");
    hrSys.addEmployee("D2", "Charlie", "Developer", 55000, "IT", "M1");

    cout << "\n";
    hrSys.printSubordinates("M1");
    
    cout << "\n";
    hrSys.printPayroll();

    return 0;
}
```

## 4. Interview Discussion
- **Composite Pattern:** Employee hierarchy (Manager -> Developers) is a classic example of the Composite Design Pattern. A `Component` can be a leaf (Developer) or a node containing children (Manager).
- **Extensibility:** To support different tax brackets globally, we would use the Strategy Pattern to inject a `TaxCalculationStrategy` interface into the Employee object rather than hardcoding the 10% rate.
