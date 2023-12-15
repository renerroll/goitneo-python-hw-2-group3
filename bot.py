def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError):
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
    return inner


@input_error
def hello_command(args, contacts):
    return "How can I help you?"


@input_error
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            return f"Contact {name} exists. For an update, use the 'change' command."
        contacts[name] = phone
        return "Contact added."
    else:
        raise ValueError


@input_error
def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            raise KeyError
    else:
        raise ValueError


@input_error
def remove_contact(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            del contacts[name]
            return f"Contact {name} deleted."
        else:
            raise KeyError
    else:
        raise ValueError


@input_error
def get_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            raise KeyError
    else:
        raise ValueError


@input_error
def show_all(args, contacts):
    contact_strings = []
    if contacts:
        for name, phone in contacts.items():
            contact_strings.append(f"{name}: {phone}")
    else:
        contact_strings.append("No contacts found.")
    return contact_strings


command_functions = {
    "hello": hello_command,
    "add": add_contact,
    "change": change_contact,
    "remove": remove_contact,
    "phone": get_phone,
    "all": show_all,
}


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in command_functions:
            print(command_functions[command](args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()