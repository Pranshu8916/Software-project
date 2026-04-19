# Import required class from system file
from system import IncidentSystem


def main():
    # Create system object (this manages all tickets)
    system = IncidentSystem()

    # Infinite loop to keep program running
    while True:
        print("\n===== Campus Incident System =====")
        print("1. Create Ticket")
        print("2. Assign Ticket")
        print("3. Start Work")
        print("4. Resolve Ticket")
        print("5. View Tickets")
        print("0. Exit")

        # Take user input
        choice = input("Enter choice: ")

        # Exit condition
        if choice == "0":
            print("Exiting system...")
            break

        # Create new ticket
        elif choice == "1":
            location = input("Enter Location: ")
            category = input("Enter Category: ")
            description = input("Enter Description: ")

            # Call function to create ticket
            system.create_ticket(location, category, description)

        # Assign ticket to department
        elif choice == "2":
            ticket_id = int(input("Enter Ticket ID: "))
            dept = input("Assign to Department: ")

            system.assign_ticket(ticket_id, dept)

        # Start working on ticket
        elif choice == "3":
            ticket_id = int(input("Enter Ticket ID: "))
            system.start_work(ticket_id)

        # Resolve ticket
        elif choice == "4":
            ticket_id = int(input("Enter Ticket ID: "))
            note = input("Enter Resolution Note: ")

            system.resolve_ticket(ticket_id, note)

        # View all tickets
        elif choice == "5":
            system.view_tickets()

        else:
            print("Invalid choice! Please try again.")


# Run program
if __name__ == "__main__":
    main()
