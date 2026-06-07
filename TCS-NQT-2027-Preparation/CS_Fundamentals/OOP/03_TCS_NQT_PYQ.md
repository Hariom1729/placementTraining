# Object-Oriented Programming (OOP) - TCS NQT Last 5 Years PYQs

These are the most frequently asked OOP questions in TCS Ninja, Digital, and Prime interviews over the last 5 years.

---

## 1. Differentiate between Compile-time and Run-time Polymorphism. Provide C++ examples.
**Answer:**
- **Compile-time (Early Binding):** The function call is resolved during compilation. Examples: Function Overloading and Operator Overloading.
  ```cpp
  class Math {
  public:
      int add(int a, int b) { return a + b; }
      double add(double a, double b) { return a + b; } // Overloading
  };
  ```
- **Run-time (Late Binding):** The function call is resolved during execution based on the actual object type. Example: Function Overriding using `virtual` keyword.
  ```cpp
  class Base { public: virtual void show() { cout << "Base"; } };
  class Derived : public Base { public: void show() override { cout << "Derived"; } };
  ```

## 2. What is an Abstract Class? Can we instantiate it?
**Answer:**
An Abstract Class is a class containing at least one pure virtual function (e.g., `virtual void draw() = 0;`). 
No, we cannot instantiate an abstract class (cannot create an object of it). It strictly serves as a blueprint for derived classes, forcing them to implement the pure virtual functions.

## 3. Explain the Diamond Problem in Multiple Inheritance. How does C++ resolve it?
**Answer:**
The diamond problem occurs when two classes (B and C) inherit from a common base class (A), and a fourth class (D) inherits from both B and C. D ends up with two copies of A's variables and methods, leading to ambiguity.
**Resolution:** C++ uses **Virtual Inheritance** (`class B : virtual public A`). This ensures that only one instance of the base class A is shared among the derived classes, eliminating the ambiguity.

## 4. What is a Memory Leak in C++? How does a Virtual Destructor prevent it?
**Answer:**
A memory leak occurs when dynamically allocated memory (`new`) is not freed (`delete`).
If a derived class object is deleted through a base class pointer, and the base class does not have a `virtual` destructor, only the base class destructor is called. The derived class's memory remains allocated, causing a leak. Making the base destructor `virtual` ensures the derived destructor is called first, fully cleaning up the memory.

## 5. Differentiate between `new` and `malloc()`.
**Answer:**
- `new` is an operator in C++; `malloc()` is a function inherited from C.
- `new` calls the constructor of the object; `malloc()` does not.
- `new` returns a pointer of the exact type; `malloc()` returns a `void*` which must be casted.
- `new` can be overloaded; `malloc()` cannot be.

## 6. What is the difference between shallow copy and deep copy?
**Answer:**
- **Shallow Copy:** Copies all member values from one object to another. If the object contains pointers, only the memory address is copied. Both objects now point to the same memory location. Changing data in one affects the other. (This is what the default copy constructor does).
- **Deep Copy:** Copies all members, but for pointers, it dynamically allocates new memory for the copy and copies the actual values over. Changes to one object do not affect the other.

## 7. What are Access Specifiers? Can a derived class access private members of a base class?
**Answer:**
Access specifiers (`public`, `protected`, `private`) define the visibility of class members.
No, a derived class cannot directly access `private` members of its base class. It can only access `public` and `protected` members.

## 8. What is a Friend Class?
**Answer:**
A friend class is a class that is granted access to the `private` and `protected` members of another class. It is declared using the `friend` keyword. It is useful when two classes are tightly coupled and need to share internal data without exposing it publicly.

## 9. Is it possible to overload a constructor? Is it possible to override a constructor?
**Answer:**
Yes, constructors can be overloaded. A class can have multiple constructors with different parameter lists (Default, Parameterized, Copy).
No, constructors cannot be overridden. Overriding requires inheritance and virtual functions, but constructors are not inherited in the normal sense and cannot be virtual.

## 10. Explain the `this` pointer.
**Answer:**
`this` is a hidden pointer passed as an argument to all non-static member functions. It holds the memory address of the object that invoked the function. It is used to resolve naming conflicts between member variables and local parameters (e.g., `this->name = name;`) and to return the object itself (`return *this;`).
