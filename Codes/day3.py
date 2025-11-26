# Day 3 — Control Flow, Guard Clauses, match/case, Menu CLI

# Guard clause example
logged_in = True
user_age = 19
has_email_verified = False

def verify(logged_in, user_age, has_email_verified):
    if not logged_in:
        print("Not logged in")
        return

    if user_age <= 18:
        print("Age restriction")
        return

    if not has_email_verified:
        print("Please verify email")
        return

    print("Access Granted")

verify(logged_in, user_age, has_email_verified)

# match-case operator example
operation = input("Enter the operation (+, -, *, /): ")

match operation:
    case "+":
        print("Addition")
    case "-":
        print("Subtraction")
    case "*":
        print("Multiplication")
    case "/":
        print("Division")
    case _:
        print("Invalid")

# Menu-driven contact book
user_data = {}

while True:
    print("\n1. Add Contact")
    print("2. Delete Contact")
    print("3. View Contacts")
    print("4. Exit")

    CRUD = input("Enter choice: ").strip()

    match CRUD:
        case '1':
            user_name = input("Enter new name: ").strip().lower()
            user_number = input("Enter phone number: ").strip()
            user_data[user_name] = user_number
            print("Added")

        case '2':
            name = input("Enter name to delete: ").strip().lower()
            if name in user_data:
                user_data.pop(name)
                print("Deleted")
            else:
                print("User not found")

        case '3':
            print(user_data)

        case '4':
            print("Exiting...")
            break

        case _:
            print("Invalid choice")
