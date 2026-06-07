# Object-Oriented Programming (OOP) in C++: Crash Course

Object-Oriented Programming is a paradigm based on the concept of "objects", which can contain data (attributes) and code (methods).

---

## 1. The Four Pillars of OOP

### 1.1 Encapsulation
Encapsulation is the wrapping up of data (variables) and functions (methods) into a single unit called a Class. It prevents direct modification of data from outside the class to maintain integrity.
- **Implementation:** Achieved using access modifiers (`private`, `protected`, `public`). Data is usually kept `private` and accessed via `public` getter/setter methods.

### 1.2 Abstraction
Abstraction means displaying only the essential information and hiding the complex background details.
- **Implementation:** Achieved using abstract classes (classes with at least one pure virtual function) or interfaces.

### 1.3 Inheritance
Inheritance is the mechanism by which one class acquires the properties and behavior of another class. It promotes code reusability.
- **Base Class:** The class whose properties are inherited.
- **Derived Class:** The class that inherits.
- **Types in C++:** Single, Multiple, Multilevel, Hierarchical, and Hybrid.

### 1.4 Polymorphism
Polymorphism means "many forms". It allows methods to do different things based on the object it is acting upon.
- **Compile-time (Early Binding):** Method Overloading, Operator Overloading.
- **Run-time (Late Binding):** Method Overriding (using `virtual` functions).

---

## 2. Important C++ OOP Concepts

### 2.1 Classes and Objects
- **Class:** A blueprint for creating objects.
- **Object:** An instance of a class. Memory is allocated only when an object is created.

```cpp
class Car {
private:
    string brand;
public:
    void setBrand(string b) { brand = b; }
    string getBrand() { return brand; }
};
```

### 2.2 Constructors and Destructors
- **Constructor:** A special member function called automatically when an object is created. It has the same name as the class and no return type.
  - *Types:* Default, Parameterized, Copy Constructor.
- **Destructor:** Called automatically when an object goes out of scope. Used to free dynamically allocated memory. Starts with a tilde `~`.

### 2.3 Virtual Functions & Abstract Classes
- **Virtual Function:** A function in a base class declared with the `virtual` keyword. It tells the compiler to perform dynamic binding.
- **Pure Virtual Function:** `virtual void draw() = 0;`. A function with no implementation in the base class.
- **Abstract Class:** A class containing at least one pure virtual function. You cannot instantiate an abstract class.

### 2.4 Access Modifiers
- `public`: Accessible from anywhere.
- `private`: Accessible only from within the class itself (and friend functions). Default for classes.
- `protected`: Accessible within the class and by derived classes.

### 2.5 `this` Pointer
Every object in C++ has access to its own address through an important pointer called `this`. The `this` pointer is an implicit parameter to all non-static member functions.

### 2.6 `static` Keyword
- **Static Member Variables:** Shared by all objects of the class. They maintain a single copy for the entire class.
- **Static Member Functions:** Can be called without an object (using `ClassName::functionName()`) and can only access static data members.

### 2.7 Friend Functions
A friend function can access `private` and `protected` members of a class, even though it is not a member of that class. It is declared inside the class with the `friend` keyword.
