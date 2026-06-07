# Object-Oriented Programming: Top Interview Questions

Here are the most frequently asked OOP interview questions, focusing heavily on C++ specific behaviors as requested.

---

## Question 1: What is the difference between Struct and Class in C++?
**Answer:**
In C++, `struct` and `class` are almost identical. The only difference is default visibility:
- In a **class**, members and base classes are `private` by default.
- In a **struct**, members and base classes are `public` by default.
Usually, `struct` is used for passive data structures (like a Point with x and y), and `class` is used for objects that have behavior/methods.

## Question 2: Explain Method Overloading vs. Method Overriding.
**Answer:**
- **Method Overloading (Compile-time Polymorphism):** Multiple functions in the *same class* have the *same name* but different parameters (type or count). The compiler determines which function to call based on the arguments.
- **Method Overriding (Run-time Polymorphism):** A function in a *derived class* has the exact *same name, return type, and parameters* as a `virtual` function in the *base class*. The JVM/Runtime decides which method to call based on the actual object type, not the pointer type.

## Question 3: What is a Virtual Function and the V-Table?
**Answer:**
A **virtual function** is a member function in the base class that you redefine in a derived class. It ensures that the correct function is called for an object, regardless of the type of reference/pointer used for the method call.
The **V-Table (Virtual Table)** is a lookup table of function pointers created by the compiler for every class that contains virtual functions. It is used to resolve function calls dynamically at runtime.

## Question 4: What is a Pure Virtual Function? What is an Abstract Class?
**Answer:**
A **pure virtual function** is a virtual function that has no definition in the base class (syntax: `virtual void func() = 0;`).
An **Abstract Class** is any class that contains at least one pure virtual function. You cannot create an object (instantiate) of an abstract class. Its primary purpose is to act as a base class.

## Question 5: What is a Copy Constructor? When is it called?
**Answer:**
A copy constructor is a member function that initializes an object using another object of the same class. Signature: `ClassName(const ClassName &obj)`.
It is called when:
1. An object is initialized from another object during declaration (`Car c1 = c2;`).
2. An object is passed by value as a parameter to a function.
3. An object is returned by value from a function.

## Question 6: What is the Diamond Problem in Multiple Inheritance?
**Answer:**
The Diamond Problem occurs when a class (D) inherits from two classes (B and C), both of which inherit from the same base class (A). 
Because B and C both contain a copy of A, class D ends up with *two* copies of A's members, causing ambiguity when D tries to access a member of A.
**Solution in C++:** Virtual Inheritance. If B and C inherit from A using the `virtual` keyword (`class B : virtual public A`), class D will only get one shared copy of A.

## Question 7: Can a Constructor be Virtual in C++?
**Answer:**
No, a constructor cannot be virtual. The purpose of a virtual function is to allow polymorphic behavior when we don't know the exact type of the object at compile time. However, to construct an object, the exact type must be known so the correct memory can be allocated. Hence, virtual constructors do not make sense.

## Question 8: Can a Destructor be Virtual in C++?
**Answer:**
Yes, and it *should* be virtual if a class has virtual functions and is intended to be used as a base class. If a derived object is deleted through a base class pointer, and the base class destructor is non-virtual, only the base class destructor will be called. This leads to memory leaks because the derived class destructor is bypassed. Making the base destructor `virtual` ensures both are called.

## Question 9: What is Encapsulation and why is it useful?
**Answer:**
Encapsulation is the bundling of data and methods that operate on that data within a single unit (class). It restricts direct access to some of the object's components.
It is useful because it protects an object's internal state from unintended or harmful modifications. It also allows the internal implementation to change without affecting the code that uses the class, promoting maintainability.

## Question 10: What is a Friend Function?
**Answer:**
A friend function is a function that is not a member of a class but is granted access to the class's `private` and `protected` members. It is declared inside the class using the `friend` keyword. It is useful for operator overloading or testing internal state, but breaks the strict concept of encapsulation.
