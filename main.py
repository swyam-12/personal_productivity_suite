#Hello I am Swyam and this is my 1 month Task of my internship at The developer arena.

from calculator import Calculator
from notes_manager import NotesManager
from timer import Timer
from file_organizer import FileOrganizer
from utils import BackupManager

def main():
    calc = Calculator()
    notes = NotesManager()
    timer = Timer()
    organizer = FileOrganizer()
    backup = BackupManager()

    while True:
        print("\n==== Personal Productivity Suite ====")
        print("1. Calculator")
        print("2. Notes Manager")
        print("3. Timer")
        print("4. File Organizer")
        print("5. Backup Data")
        print("6. Restore Data")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            expr = input("Enter expression (e.g., 5+3): ")
            print("Result:", calc.calculate(expr))

        elif choice == "2":
            print("1. Add Note")
            print("2. View Notes")
            sub = input("Choose: ")

            if sub == "1":
                title = input("Title: ")
                content = input("Content: ")
                notes.add_note(title, content)
            elif sub == "2":
                all_notes = notes.view_notes()
                for note in all_notes:
                    print(note)

        elif choice == "3":
            seconds = input("Enter seconds: ")
            timer.start_timer(seconds)

        elif choice == "4":
            path = input("Enter folder path: ")
            organizer.organize(path)

        elif choice == "5":
            backup.backup_data()

        elif choice == "6":
            backup.restore_data()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()