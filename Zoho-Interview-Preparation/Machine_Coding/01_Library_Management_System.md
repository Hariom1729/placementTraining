# Machine Coding: Library Management System

## 1. Requirements

Design a Library Management System with the following core functionalities:
1. **Add Books:** The librarian should be able to add books (Title, Author, ISBN, Quantity).
2. **Search Books:** Users should be able to search books by Title or Author.
3. **Register Users:** System should allow registering users with unique IDs.
4. **Issue Books:** A registered user should be able to borrow a book if available.
5. **Return Books:** A user should be able to return a borrowed book.
6. **Track Inventory:** The system should decrement inventory on issue and increment on return.

**Edge Cases to Handle:**
- Prevent borrowing if the book is out of stock.
- Prevent returning a book that was not borrowed by that user.
- Ensure unique user registration and book ISBNs.

## 2. Class Diagram / Entities

1. `Book`: Represents a book entity.
   - Attributes: `isbn` (string), `title` (string), `author` (string), `total_copies` (int), `available_copies` (int).
2. `User`: Represents a library member.
   - Attributes: `user_id` (int), `name` (string), `borrowed_books` (set of ISBNs).
3. `Library`: The core system managing all operations.
   - Attributes: `books` (hash map mapping ISBN to `Book`), `users` (hash map mapping user_id to `User`).
   - Methods: `addBook()`, `registerUser()`, `searchBook()`, `issueBook()`, `returnBook()`.

## 3. Approach

We will use an Object-Oriented approach in C++. 
- `std::unordered_map` will be used for $O(1)$ fast lookups for Books by ISBN and Users by ID.
- We will encapsulate the attributes and expose appropriate getter/setter methods to maintain the state of the library securely.
- Proper error messages will be printed if a validation fails (e.g., "Book not found", "User not registered").

## 4. C++ Implementation

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

// --- Entity: Book ---
class Book {
private:
    string isbn;
    string title;
    string author;
    int total_copies;
    int available_copies;

public:
    Book() {} // Default constructor
    Book(string i, string t, string a, int copies) {
        isbn = i;
        title = t;
        author = a;
        total_copies = copies;
        available_copies = copies;
    }

    string getISBN() const { return isbn; }
    string getTitle() const { return title; }
    string getAuthor() const { return author; }
    int getAvailableCopies() const { return available_copies; }

    void issueCopy() {
        if (available_copies > 0) available_copies--;
    }

    void returnCopy() {
        if (available_copies < total_copies) available_copies++;
    }

    void displayInfo() const {
        cout << "ISBN: " << isbn << " | Title: " << title 
             << " | Author: " << author 
             << " | Available: " << available_copies << "/" << total_copies << "\n";
    }
};

// --- Entity: User ---
class User {
private:
    int user_id;
    string name;
    unordered_set<string> borrowed_books; // stores ISBNs

public:
    User() {}
    User(int id, string n) : user_id(id), name(n) {}

    int getId() const { return user_id; }
    string getName() const { return name; }

    bool hasBorrowed(const string& isbn) {
        return borrowed_books.find(isbn) != borrowed_books.end();
    }

    void borrowBook(const string& isbn) {
        borrowed_books.insert(isbn);
    }

    void returnBook(const string& isbn) {
        borrowed_books.erase(isbn);
    }
};

// --- Core System: Library ---
class Library {
private:
    unordered_map<string, Book> books;
    unordered_map<int, User> users;

public:
    void addBook(string isbn, string title, string author, int copies) {
        if (books.find(isbn) != books.end()) {
            cout << "Book with ISBN " << isbn << " already exists in system.\n";
            return;
        }
        books[isbn] = Book(isbn, title, author, copies);
        cout << "Added book: " << title << "\n";
    }

    void registerUser(int id, string name) {
        if (users.find(id) != users.end()) {
            cout << "User ID " << id << " is already registered.\n";
            return;
        }
        users[id] = User(id, name);
        cout << "Registered user: " << name << "\n";
    }

    void searchByTitle(string keyword) {
        cout << "--- Search Results for '" << keyword << "' ---\n";
        bool found = false;
        for (auto& pair : books) {
            if (pair.second.getTitle().find(keyword) != string::npos) {
                pair.second.displayInfo();
                found = true;
            }
        }
        if (!found) cout << "No books found.\n";
    }

    void issueBook(int userId, string isbn) {
        if (users.find(userId) == users.end()) {
            cout << "[Error] User not found.\n";
            return;
        }
        if (books.find(isbn) == books.end()) {
            cout << "[Error] Book not found in library.\n";
            return;
        }

        User& u = users[userId];
        Book& b = books[isbn];

        if (b.getAvailableCopies() <= 0) {
            cout << "[Error] Sorry, '" << b.getTitle() << "' is currently out of stock.\n";
            return;
        }
        if (u.hasBorrowed(isbn)) {
            cout << "[Error] User has already borrowed this book.\n";
            return;
        }

        // Proceed to issue
        b.issueCopy();
        u.borrowBook(isbn);
        cout << "[Success] Issued '" << b.getTitle() << "' to " << u.getName() << ".\n";
    }

    void returnBook(int userId, string isbn) {
        if (users.find(userId) == users.end()) {
            cout << "[Error] User not found.\n";
            return;
        }
        if (books.find(isbn) == books.end()) {
            cout << "[Error] Book not found in library.\n";
            return;
        }

        User& u = users[userId];
        Book& b = books[isbn];

        if (!u.hasBorrowed(isbn)) {
            cout << "[Error] User did not borrow this book.\n";
            return;
        }

        // Proceed to return
        b.returnCopy();
        u.returnBook(isbn);
        cout << "[Success] User " << u.getName() << " returned '" << b.getTitle() << "'.\n";
    }
};

// --- Main Driver Function ---
int main() {
    Library lib;

    cout << "--- Library Setup ---\n";
    lib.addBook("101", "The C++ Programming Language", "Bjarne Stroustrup", 3);
    lib.addBook("102", "Effective Modern C++", "Scott Meyers", 2);
    lib.addBook("103", "Clean Code", "Robert C. Martin", 5);

    lib.registerUser(1, "Alice");
    lib.registerUser(2, "Bob");

    cout << "\n--- Search Operation ---\n";
    lib.searchByTitle("C++");

    cout << "\n--- Issue Operations ---\n";
    lib.issueBook(1, "101");
    lib.issueBook(1, "101"); // Error: already borrowed
    lib.issueBook(2, "101");
    lib.issueBook(3, "102"); // Error: User not found

    cout << "\n--- Return Operations ---\n";
    lib.returnBook(2, "103"); // Error: never borrowed
    lib.returnBook(1, "101"); // Success

    cout << "\n--- Final Inventory Check ---\n";
    lib.searchByTitle("C++");

    return 0;
}
```

## 5. Interview Discussion Points
1. **Why `std::unordered_map` over `std::map`?**
   - We used `unordered_map` to get $O(1)$ average time complexity for user and book lookups by their primary keys (ID and ISBN). `std::map` provides $O(\log N)$ but stores elements in a sorted tree structure, which we didn't need here.
2. **How to handle concurrency?**
   - If this were a multi-threaded application (e.g., multiple librarians issuing books simultaneously), the `issueBook()` method would suffer from race conditions. We would need to add `std::mutex` locks inside `issueBook()` and `returnBook()`.
3. **Database Integration:**
   - In a real-world scenario, the HashMaps would act as a Cache (like Redis), and the `addBook` and `issueBook` operations would translate to SQL `INSERT` and `UPDATE` statements running inside Transactions.
