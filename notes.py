import time

def show_note():
    try:
        with open("notes.txt", "r", encoding='utf8') as file:
            notes = file.readlines()
            if not notes:
                print("No notes found.")
            else:
                for i, note in enumerate(notes, start=1):
                    print(f"\n{i}. {note.strip()}\n")
    except FileNotFoundError:
        print("No notes found.")

def add_note():
    with open("notes.txt", "a", encoding='utf8') as file:
        title = input("Enter a title: ")
        note = input("Enter a note: ")
        date = time.strftime("%d/%m/%Y  %H:%M")
        file.write(f'{title} || {note} >>> {date}\n')


def delete_note():
    try:
        with open("notes.txt", "r", encoding='utf8') as file:
            notes = file.readlines()

        if not notes:
            print("No notes found.")
            return

        show_note()  # Show notes to help user choose
        num = int(input("Enter a number to delete: "))

        if 1 <= num <= len(notes):
            notes.pop(num - 1)

            # Write the updated notes back to the file
            with open("notes.txt", "w", encoding='utf8') as file:
                file.writelines(notes)

            print("Note deleted successfully.")
        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("Invalid number.")
    except FileNotFoundError:
        print("No notes found.")

try:
    while True:
        print('1. Show notes\n'
              '2. Add note\n'
              '3. Delete note\n'
              '4. End programm')

        choice = int(input('\nEnter ur choice >>> '))
        if choice == 1:
            show_note()
        elif choice == 2:
            add_note()
        elif choice  == 3:
            delete_note()
        elif choice == 4:
            break
        else:
            print("Invalid choice.")
except  ValueError:
    print("Invalid choice.")
