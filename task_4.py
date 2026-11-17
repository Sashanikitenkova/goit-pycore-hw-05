def input_error(func):
    # Create a wrapper function to handle errors
    def inner(*args, **kwargs):
        try:
            # Execute the original function
            return func(*args, **kwargs)

        except KeyError:
            return "Contact not found."

        except ValueError:
            return "Give me name and phone please."

        except IndexError:
            return "Enter the argument for the command."

    # Return the wrapped function
    return inner


def parse_input(user_input):
    # Remove extra spaces and split the input into parts
    parts = user_input.strip().split()

    # Check if the input is empty
    if not parts:
        return "", []

    # Get the command and its arguments
    command = parts[0].lower()
    args = parts[1:]

    return command, args


@input_error
def add_contact(args, contacts):
    # Check if the correct number of arguments is provided
    if len(args) != 2:
        raise ValueError

    # Get the name and phone number
    name, phone = args

    # Add the contact to the dictionary
    contacts[name] = phone

    return "Contact added."


@input_error
def change_contact(args, contacts):
    # Check if the correct number of arguments is provided
    if len(args) != 2:
        raise ValueError

    # Get the name and phone number
    name, phone = args

    # Update the contact if it exists
    if name not in contacts:
        raise KeyError

    contacts[name] = phone

    return "Contact updated."


@input_error
def show_phone(args, contacts):
    # Check if the correct number of arguments is provided
    if len(args) != 1:
        raise ValueError

    # Get the contact name
    name = args[0]

    # Return the phone number if the contact exists
    if name not in contacts:
        raise KeyError

    return contacts[name]


@input_error
def show_all(contacts):
    # Check if there are any contacts
    if not contacts:
        return "No contacts saved."

    # Create a list with all contacts
    result = []

    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")

    # Join all contacts into one string
    return "\n".join(result)


def main():
    # Create an empty dictionary for contacts
    contacts = {}

    print("Welcome to the assistant bot!")

    # Start the main program loop
    while True:
        user_input = input("Enter a command: ")

        # Parse the user's input
        command, args = parse_input(user_input)

        # Exit the program
        if command in ["close", "exit"]:
            if args:
                print("Invalid command.")
            else:
                print("Good bye!")
                break

        # Respond to the hello command
        elif command == "hello":
            if args:
                print("Invalid command.")
            else:
                print("How can I help you?")

        # Add a new contact
        elif command == "add":
            print(add_contact(args, contacts))

        # Change an existing contact
        elif command == "change":
            print(change_contact(args, contacts))

        # Show a contact's phone number
        elif command == "phone":
            print(show_phone(args, contacts))

        # Show all saved contacts
        elif command == "all":
            if args:
                print("Invalid command.")
            else:
                print(show_all(contacts))

        # Handle unknown commands
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()