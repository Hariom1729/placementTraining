# Machine Coding: Parking Lot

## 1. Requirements

Design a Parking Lot system:
1. **Multiple Levels:** The lot has multiple floors.
2. **Spot Types:** Spots are specifically for Compact (Cars), Large (Trucks), or Bikes.
3. **Park Vehicle:** Assign the nearest available appropriate spot to a vehicle entering.
4. **Unpark Vehicle:** Free up the spot and calculate the fee based on time parked.

## 2. Entities
- `Vehicle`: Vehicle Number, Type (BIKE, CAR, TRUCK).
- `ParkingSpot`: ID, SpotType, IsFree, Vehicle (if occupied).
- `Level`: Floor number, collection of spots.
- `Ticket`: Entry time, Spot ID, Vehicle details.

## 3. C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

enum VehicleType { BIKE, CAR, TRUCK };

class Vehicle {
public:
    string number;
    VehicleType type;
    Vehicle(string n, VehicleType t) : number(n), type(t) {}
};

class ParkingSpot {
public:
    int id;
    VehicleType spotType;
    bool isFree;
    string parkedVehicleNumber;

    ParkingSpot(int i, VehicleType t) : id(i), spotType(t), isFree(true) {}

    bool canFit(VehicleType vType) {
        return isFree && spotType == vType; // simplified: strict matching
    }

    void park(Vehicle v) {
        isFree = false;
        parkedVehicleNumber = v.number;
    }

    void removeVehicle() {
        isFree = true;
        parkedVehicleNumber = "";
    }
};

class Level {
public:
    int floor;
    vector<ParkingSpot> spots;

    Level(int f, int bikes, int cars, int trucks) {
        floor = f;
        int id = 1;
        for(int i=0; i<bikes; i++) spots.push_back(ParkingSpot(id++, BIKE));
        for(int i=0; i<cars; i++) spots.push_back(ParkingSpot(id++, CAR));
        for(int i=0; i<trucks; i++) spots.push_back(ParkingSpot(id++, TRUCK));
    }

    ParkingSpot* findAvailableSpot(VehicleType type) {
        for(auto& spot : spots) {
            if(spot.canFit(type)) return &spot;
        }
        return nullptr;
    }
};

class ParkingLot {
private:
    vector<Level> levels;

public:
    ParkingLot() {
        // 2 levels. Each has 2 bikes, 2 cars, 1 truck.
        levels.push_back(Level(1, 2, 2, 1));
        levels.push_back(Level(2, 2, 2, 1));
    }

    bool parkVehicle(Vehicle v) {
        for(auto& level : levels) {
            ParkingSpot* spot = level.findAvailableSpot(v.type);
            if(spot != nullptr) {
                spot->park(v);
                cout << "[Parked] " << v.number << " at Floor " << level.floor << ", Spot " << spot->id << "\n";
                return true;
            }
        }
        cout << "[Full] No spot available for " << v.number << "\n";
        return false;
    }

    void unparkVehicle(string number) {
        for(auto& level : levels) {
            for(auto& spot : level.spots) {
                if(!spot.isFree && spot.parkedVehicleNumber == number) {
                    spot.removeVehicle();
                    cout << "[Unparked] " << number << " removed from Floor " << level.floor << "\n";
                    // In a real system, calculate fee based on timestamps here
                    return;
                }
            }
        }
        cout << "[Error] Vehicle " << number << " not found.\n";
    }
};

int main() {
    ParkingLot lot;
    Vehicle v1("CAR-123", CAR);
    Vehicle v2("CAR-456", CAR);
    Vehicle v3("CAR-789", CAR); // Will go to floor 2

    lot.parkVehicle(v1);
    lot.parkVehicle(v2);
    lot.parkVehicle(v3);

    lot.unparkVehicle("CAR-123");
    Vehicle v4("CAR-999", CAR);
    lot.parkVehicle(v4); // Should take the newly freed spot on Floor 1

    return 0;
}
```

## 4. Interview Discussion
- **Strategy Pattern:** If a vehicle can fit in multiple spots (e.g., a Bike in a Car spot), you would implement an allocation strategy interface.
- **Scalability:** Finding an empty spot currently takes $O(N)$ where $N$ is total spots. In large systems, we maintain a min-heap or separate queues of available spots per type to achieve $O(1)$ allocation.
