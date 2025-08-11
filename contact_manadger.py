def show_all_contacts():

    try:
        with open('contacts.txt', 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No contacts file found.")


def search_contacts(query):

    try:
        with open('contacts.txt', 'r') as file:
            found_contacts = []
            for line in file:
                line = line.strip()
                if query.lower() in line.lower():
                    found_contacts.append(line)

            if found_contacts:
                print(f"Found {len(found_contacts)} contact(s) matching '{query}':")
                for contact in found_contacts:
                    print(contact)
            else:
                print(f"No contacts found matching '{query}'")

    except FileNotFoundError:
        print("No contacts file found.")


def add_contact(text):
    try:
        with open('contacts.txt', 'a', encoding='utf8') as file:
            file.write(text + '\n')
    except  FileNotFoundError:
        print("No contacts file found.")



# Example usage:
# add_contact("Wuill Doe, 123-456-7890, email@example.com")
# search_contacts("Doe")
# search_contacts("123-456-7890")
# search_contacts("email@example.com")