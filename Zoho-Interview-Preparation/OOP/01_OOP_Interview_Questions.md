# Object-Oriented Programming (OOP) - C++

## 1. Core Concepts
**1. What is Object-Oriented Programming?**
OOP is a programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods). It aims to bind data and functions together to improve modularity and reusability.

**2. What are the four pillars of OOP?**
1. **Encapsulation:** Wrapping data and methods into a single unit (class) and hiding internal state (access modifiers).
2. **Abstraction:** Hiding complex implementation details and showing only the essential features of an object.
3. **Inheritance:** A mechanism where one class acquires the properties and behaviors of another, promoting code reusability.
4. **Polymorphism:** The ability of different objects to respond in their own way to the same method call (Compile-time via overloading, Run-time via overriding).

**3. Class vs Object?**
A Class is a blueprint or template, whereas an Object is a real-world instance of that class that occupies memory.

## 2. Encapsulation & Abstraction
**4. How is Encapsulation achieved in C++?**
Using access specifiers (`private`, `protected`, `public`). Data members are kept private, and public getter/setter methods are provided to access and modify them securely.

**5. What is an Abstract Class in C++?**
A class that has at least one pure virtual function (e.g., `virtual void draw() = 0;`). It cannot be instantiated. It is used as a base class.

## 3. Inheritance
**6. Types of Inheritance in C++?**
Single, Multiple, Multilevel, Hierarchical, and Hybrid.

**7. What is the Diamond Problem? How to solve it?**
Occurs in Multiple Inheritance when a class inherits from two classes that have a common base class, causing ambiguity. Solved using `virtual` inheritance (`class B : virtual public A`).

## 4. Polymorphism
**8. Compile-time vs Run-time Polymorphism?**
- **Compile-time:** Function Overloading and Operator Overloading. Resolved by the compiler based on arguments.
- **Run-time:** Function Overriding using `virtual` functions and base class pointers. Resolved during execution.

**9. What is a Virtual Function?**
A member function in a base class declared with the `virtual` keyword that is meant to be overridden in a derived class.

**10. What is a V-Table (Virtual Table)?**
A lookup table created by the compiler for dynamic dispatch. Every class that uses virtual functions has a V-Table, and objects have a hidden V-Ptr (Virtual Pointer) pointing to it.

## 5. Constructors & Destructors
**11. Types of Constructors?**
Default, Parameterized, and Copy Constructor.

**12. Deep Copy vs Shallow Copy?**
- **Shallow:** Copies pointers, meaning both objects point to the same memory. (Default copy constructor does this).
- **Deep:** Allocates new memory and copies the actual values. Requires a custom copy constructor.

**13. Why should Destructors be virtual?**
If a derived class object is deleted through a base class pointer, a non-virtual destructor will only destroy the base part, causing a memory leak. A virtual destructor ensures the derived class destructor is called first.

## 6. SOLID Principles
1. **S**ingle Responsibility Principle: A class should have one, and only one, reason to change.
2. **O**pen/Closed Principle: Software entities should be open for extension, but closed for modification.
3. **L**iskov Substitution Principle: Objects of a superclass shall be replaceable with objects of its subclasses.
4. **I**nterface Segregation Principle: No client should be forced to depend on methods it does not use.
5. **D**ependency Inversion Principle: Depend on abstractions, not on concretions.

## 7. C++ Implementation Example (Polymorphism & Abstraction)
```cpp
#include <iostream>
using namespace std;

// Abstract Base Class
class Shape {
public:
    virtual void draw() = 0; // Pure virtual function
    virtual ~Shape() { cout << "Shape Destructor\n"; } // Virtual destructor
};

class Circle : public Shape {
public:
    void draw() override { cout << "Drawing Circle\n"; }
    ~Circle() { cout << "Circle Destructor\n"; }
};

class Square : public Shape {
public:
    void draw() override { cout << "Drawing Square\n"; }
    ~Square() { cout << "Square Destructor\n"; }
};

int main() {
    Shape* s1 = new Circle();
    Shape* s2 = new Square();
    
    s1->draw(); // Dynamic Dispatch -> Drawing Circle
    s2->draw(); // Dynamic Dispatch -> Drawing Square
    
    delete s1; // Safe deletion because of virtual destructor
    delete s2;
    return 0;
}
```
*(This document condenses the top 100 variations of OOP questions asked at Zoho into core concepts and principles).*
