# Machine Coding: Movie Booking System

## 1. Requirements

Design a Movie Booking System (like BookMyShow) with the following core functionalities:
1. **Add Theaters & Shows:** Admin can add theaters, screens, and shows.
2. **Search Movies:** Users can search for shows playing a specific movie.
3. **Book Tickets:** Users can select a show, check available seats, and book tickets.
4. **Concurrency Handling:** Prevent double booking of the same seat.

## 2. Entities
- `Movie`: Title, Language, Duration.
- `Show`: Movie, Theater, Start Time, Available Seats.
- `Seat`: Row, Number, Status (Booked/Available).
- `Booking`: User, Show, Seats Booked, Total Price.

## 3. C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Seat {
public:
    string id;
    bool isBooked;
    double price;

    Seat() {}
    Seat(string i, double p) : id(i), isBooked(false), price(p) {}
};

class Show {
public:
    string showId;
    string movieName;
    string time;
    unordered_map<string, Seat> seats;

    Show() {}
    Show(string id, string m, string t) : showId(id), movieName(m), time(t) {
        // Initialize 10 standard seats for simplicity
        for(int i=1; i<=10; i++) {
            string sId = "S" + to_string(i);
            seats[sId] = Seat(sId, 150.0);
        }
    }

    void displayAvailableSeats() {
        cout << "Available seats for " << movieName << " at " << time << ": ";
        for(auto& pair : seats) {
            if(!pair.second.isBooked) cout << pair.first << " ";
        }
        cout << "\n";
    }

    bool bookSeat(string seatId) {
        if(seats.find(seatId) == seats.end()) {
            cout << "Invalid Seat ID.\n";
            return false;
        }
        if(seats[seatId].isBooked) {
            cout << "Seat " << seatId << " is already booked!\n";
            return false;
        }
        // Book it
        seats[seatId].isBooked = true;
        return true;
    }
};

class MovieBookingSystem {
    unordered_map<string, Show> shows;

public:
    void addShow(string id, string movie, string time) {
        shows[id] = Show(id, movie, time);
    }

    void searchShows(string movieName) {
        cout << "--- Shows for " << movieName << " ---\n";
        for(auto& pair : shows) {
            if(pair.second.movieName == movieName) {
                cout << "Show ID: " << pair.first << " | Time: " << pair.second.time << "\n";
            }
        }
    }

    void bookTickets(string showId, vector<string> seatIds) {
        if(shows.find(showId) == shows.end()) {
            cout << "Invalid Show ID.\n";
            return;
        }
        Show& s = shows[showId];
        
        // Validation pass
        for(string seatId : seatIds) {
            if(s.seats.find(seatId) == s.seats.end() || s.seats[seatId].isBooked) {
                cout << "[Booking Failed] One or more seats are unavailable.\n";
                return;
            }
        }

        // Booking pass
        double total = 0;
        for(string seatId : seatIds) {
            s.bookSeat(seatId);
            total += s.seats[seatId].price;
        }
        cout << "[Success] Tickets booked. Total amount: Rs. " << total << "\n";
    }

    void checkAvailability(string showId) {
        if(shows.find(showId) != shows.end()) {
            shows[showId].displayAvailableSeats();
        }
    }
};

int main() {
    MovieBookingSystem system;
    system.addShow("SH1", "Inception", "10:00 AM");
    system.addShow("SH2", "Inception", "02:00 PM");

    system.searchShows("Inception");

    system.checkAvailability("SH1");
    system.bookTickets("SH1", {"S1", "S2"});
    system.bookTickets("SH1", {"S2", "S3"}); // Should fail
    system.checkAvailability("SH1");

    return 0;
}
```

## 4. Interview Discussion
- **Concurrency:** Real systems use Distributed Locks (like Redis Redlock) or DB row-level locking (`SELECT FOR UPDATE`) to prevent two users from booking `S1` simultaneously.
- **Payment Gateway:** In reality, seats are put into a "Locked" state for 10 minutes pending payment. If payment fails, they revert to "Available".
