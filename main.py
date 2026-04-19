from system import IncidentSystem

def main():
    system = IncidentSystem()

    while True:
        print("\n===== Campus Incident System =====")
        print("1. Create Ticket")
        print("2. Assign Ticket")
        print("3. Start Work")
        print("4. Resolve Ticket")
        print("5. View Tickets")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "0":
            break

        elif choice == "1":
            location = input("Enter Location: ")
            category = input("Enter Category: ")
            description = input("Enter Description: ")
            system.create_ticket(location, category, description)

        elif choice == "2":
            ticket_id = int(input("Enter Ticket ID: "))
            dept = input("Assign to Department: ")
            system.assign_ticket(ticket_id, dept)

        elif choice == "3":
            ticket_id = int(input("Enter Ticket ID: "))
            system.start_work(ticket_id)

        elif choice == "4":
            ticket_id = int(input("Enter Ticket ID: "))
            note = input("Enter Resolution Note: ")
            system.resolve_ticket(ticket_id, note)

        elif choice == "5":
            system.view_tickets()

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()