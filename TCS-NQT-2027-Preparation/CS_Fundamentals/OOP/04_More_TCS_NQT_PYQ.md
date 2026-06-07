# OOP - Extended TCS NQT Interview Questions (Part 2)

A continuation of the most frequently asked Object-Oriented Programming questions in technical interviews.

---

## 11. What is an Inline Function in C++?
**Answer:**
An inline function is a function that is expanded in line when it is called. When the inline function is called, the C++ compiler inserts the complete body of the function in every place that the function is called, rather than jumping to a separate block of code. This saves the overhead of a function call. It is a request to the compiler, not a command; the compiler may ignore it if the function is too large.

## 12. Differentiate between `struct` in C and `struct` in C++.
**Answer:**
- **In C:** A `struct` can only hold data members (variables). It cannot hold member functions (methods), cannot have access modifiers (everything is public), and cannot use inheritance.
- **In C++:** A `struct` is almost identical to a `class`. It can hold both data and functions, can use access modifiers, and supports inheritance. The only difference is that members of a `struct` are `public` by default, whereas members of a `class` are `private` by default.

## 13. What is Operator Overloading? Can all operators be overloaded?
**Answer:**
Operator Overloading is a type of compile-time polymorphism where you provide a special meaning to an existing operator for a user-defined data type (like adding two objects using the `+` operator).
**No, not all operators can be overloaded.** The following cannot be overloaded in C++:
- Scope Resolution Operator (`::`)
- Member Access or Dot Operator (`.`)
- Pointer-to-member Operator (`.*`)
- Ternary/Conditional Operator (`?:`)
- `sizeof` Operator

## 14. Explain the concept of Data Hiding.
**Answer:**
Data hiding is an OOP principle where the internal object details (data members) are hidden from the outside world. It is achieved through Encapsulation by declaring data members as `private`. This protects the data from accidental corruption and ensures it can only be modified through controlled public interfaces (getter and setter methods).

## 15. What is a Default Constructor? What happens if you don't define one?
**Answer:**
A default constructor is a constructor that either has no parameters, or if it has parameters, all of them have default values.
If you do not define *any* constructor in your class, the C++ compiler automatically provides a default constructor. However, if you define a parameterized constructor, the compiler *will not* provide a default constructor automatically.

## 16. What is a Destructor? Can it be overloaded?
**Answer:**
A destructor is a special member function that is executed automatically when an object is destroyed or goes out of scope. Its main purpose is to free dynamic memory or release resources acquired by the object.
**No, a destructor cannot be overloaded.** A class can only have one destructor, and it takes no parameters and returns no value.

## 17. What is an Interface in C++?
**Answer:**
C++ does not have a built-in `interface` keyword like Java or C#. Instead, an interface is simulated using an **Abstract Class** where *all* the functions are pure virtual functions (`virtual void func() = 0;`), and there are no member variables. It simply defines a contract that derived classes must fulfill.

## 18. Why use pointers to base class in C++?
**Answer:**
Pointers (or references) to a base class are essential for achieving Run-Time Polymorphism. You can point a base class pointer to an object of a derived class. When a virtual function is called through this base class pointer, the C++ runtime system resolves the call to the derived class's overridden version of the function using the V-Table.

## 19. What is a Virtual Base Class?
**Answer:**
A Virtual Base Class is used to prevent the Diamond Problem in multiple inheritance. When two classes inherit from the same base class, and a fourth class inherits from both of those classes, the fourth class will inherit two copies of the original base class's members. By declaring the inheritance as `virtual` (e.g., `class B : virtual public A`), only one shared copy of the base class is passed down.

## 20. Does C++ support Multiple Inheritance? What about Java?
**Answer:**
- **C++:** Yes, C++ fully supports multiple inheritance (a class can inherit from more than one base class).
- **Java:** No, Java does not support multiple inheritance with classes to avoid the Diamond Problem. However, Java allows multiple inheritance through Interfaces.
