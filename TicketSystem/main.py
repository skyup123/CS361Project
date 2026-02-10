
from os import system


events = {
    1: "Twice Concert",
    2: "The Weekend Concert",
    3: "Wicked Broadway Show"
}

ticket_inventory = {
    1: 50,
    2: 30,
    3: 120
}


def get_events():
    return events


def get_availability(event_id):
    return ticket_inventory.get(event_id)


def display_events():
    print("Event ID : Event Name")
    for event_id, name in get_events().items():
        print(event_id, ":", name)


def display_single_event_availability():
    event_id = int(input("Enter event ID: "))

    if event_id not in get_events():
        print("Invalid Event ID")
        return

    print("Event:", get_events()[event_id])
    print("Tickets Available:", get_availability(event_id))


def display_all_event_availability():
    print("Event ID | Event Name | Tickets Available")
    for event_id, name in get_events().items():
        print(f"{event_id} | {name} | {get_availability(event_id)}")


def purchase():
    event_id = int(input("Enter event ID: "))
    quantity = int(input("Enter number of tickets to hold temporarily: "))
    available = get_availability(event_id)
    if quantity <= 0 or quantity > available:
        print("Invalid quantity. Only", available, "ticket(s) left!")
        return
    else:
        print("Tickets selected successfully!")
        print("""
Do you wish to continue purchasing?
[y] Yes                  [n] No
""")

        decision = input("Choice: ")
        if decision == 'n':
            return


def show_help():
    system("clear||cls")
    print("""
====================================
 Help – Ticketing System
====================================

This system allows you to:
• View events
• Check ticket availability
• Purchasing tickets

If you have any question, please contact help@ticketsystem.com
""")


def main_menu():
    print("""
===================================================
        Welcome to the Ticketing System
 Find events and purchase tickets in a few steps.
 Note: If the event database is large, some actions
 may take a moment to complete.")
===================================================
    """)
    while True:
        system("clear||cls")
        print("""
MAIN MENU
----------------------------------
1. View Events
2. View ALL Ticket Availability
3. View SINGLE Event Availability
4. Purchase Tickets
5. Help
6. Exit
----------------------------------""")
        choice = input("Select an option: ")

        if choice == "1":
            display_events()
            input("\nPress Enter to return to menu...")
        elif choice == "2":
            display_all_event_availability()
            input("\nPress Enter to return to menu...")
        elif choice == "3":
            display_single_event_availability()
            input("\nPress Enter to return to menu...")
        elif choice == "4":
            purchase()
            input("\nPress Enter to return to menu...")
        elif choice == "5":
            show_help()
            input("\nPress Enter to return to menu...")
        elif choice == "6":
            print("Thanks for using the Ticketing System! Goodbye")
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main_menu()
