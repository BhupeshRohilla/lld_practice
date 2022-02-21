# Parking lot

## Requirements
- Parking lot
    - multiple entries and exit
    - Collect parking ticket at entry
    - Pay at exits on autmated panels or to parking attendant or pay on each floor at info portal.
    - Pay with cash or card.
    - Maximum capacity. Show message at entrance panel and parking display board.
- Multiple floors, each floor:
    - Multiple parking spots are there.
    - Info portal exist which display free spots
- Parking spot:
    - Types: Handicapped, Motorcycle, Car, Truck, Van
    - Size: Compact, Medium, Large
    - Status: Avalable, Free
- Per-hour parking fee model:
    - 1st hour: $4
    - 2nd & 3rd hour: $3.5
    - 4th hour onwards: $2.5


## Actors:
- System
- Admin
- Customer
- Parking Attendant

## Classes:
- ParkingLot
    - Add entry and exits gates.
    - Add floor.

- Floor
    - Add parking spot.
    - update parking spot status.
    - update info portal.

- InfoPortal:
    - provides total parking spots available.

- ParkingSpot:
    - Type
    - Size
    - Status
        -> SubClasses for Petrolium car, electric car

- PetroliumCarSpot(ParkingSpot):
- ElectricCarSpot(ParkingSpot):
    - ElectricPanel which lets you charge the car.
    - Pay for the units used.

- ElectricPanel:
    - Pay for per unit of charge.

- EntryGate:
    - Provides parking ticket.
    - Then opens the gate for the car.
    - Entrance panel to display messages.

- ParkingDisplayBoard:
    - Display messages of the parking lot.

- ExitGate:
    - Scans the parking ticket and check if it is paid or not.
    - If not paid, then gives the option for payment.
    - Process payment from 'Payment' class.
    - Fetch total parking fee from 'Fee' class.

- ParkingTicket:
    - will have a unique id.
    - provides the entry time.
    - details of the payment done or not.

- Payment:
    - pay by cash
    - pay by card

- Fee:
    - provides total fee for the given ticket entry and exit time.

- ParkingAttendant
    - collect this much cash
