from os import system
import time
from flight_Console_App import Flight

def header():
    for i in range(100):
        print('*', end='')
    for i in range(50):
        print(" ", end='')
    print('Flight Capacitor Checker!')
    for i in range(100):
        print("*", end='')
try:
    system('cls')
    header()
    people = int(input("\nEnter the number of people ready to board the flight: "))
    capacity = int(input("What's the capacity of the flight: "))
except ValueError:
    print("Value needed!")
system('cls')
try:
    header()
    flight = Flight(capacity)
    names = []
    for i in range(people):
        name = str(input("\nName: "))
        names.append(name)
    system('cls')
    header()
    for person in names:
        time.sleep(2)
        if flight.add_passenger(person):
            print(f"\n{person} has been added to the flight successfully")
        else:
            print(f"\nNo available seat for {person}")
except NameError:
    print("Capacity of the fight needed!")
