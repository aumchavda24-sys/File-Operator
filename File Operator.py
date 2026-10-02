from datetime import datetime
import os


class JournalManager:

    FILE_NAME = "journal.txt"

    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry: ").strip()

            if entry == "":
                print("Entry cannot be empty.")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 'a' mode is used to append a new entry
            with open(self.FILE_NAME, "a") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n\n")

            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied while writing to the journal.")

        except OSError as error:
            print(f"Error while saving the entry: {error}")

    def view_entries(self):
        try:
            # 'r' mode is used to read the file
            with open(self.FILE_NAME, "r") as file:
                content = file.read()

            if content.strip() == "":
                print("\nNo journal entries found.")
                return

            print("\nYour Journal Entries:")
            print("---------------------")
            print(content)

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("\nError: Permission denied while reading the journal.")

        except OSError as error:
            print(f"\nError while reading the journal: {error}")

    def search_entry(self):
        keyword = input("\nEnter a keyword or date to search: ").strip()

        if keyword == "":
            print("Search term cannot be empty.")
            return

        try:
            # 'r' mode is used to search the file
            with open(self.FILE_NAME, "r") as file:
                content = file.read()

            entries = content.split("\n\n")

            found = False

            print("\nMatching Entries:")
            print("-----------------")

            for entry in entries:
                if keyword.lower() in entry.lower():
                    print(entry)
                    print()
                    found = True

            if found == False:
                print(f"No entries were found for the keyword: {keyword}")

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("\nError: Permission denied while searching the journal.")

        except OSError as error:
            print(f"\nError while searching the journal: {error}")

    def delete_all_entries(self):

        if not os.path.exists(self.FILE_NAME):
            print("\nNo journal entries to delete.")
            return

        confirmation = input(
            "\nAre you sure you want to delete all entries? (yes/no): "
        ).strip().lower()

        if confirmation != "yes":
            print("Delete operation cancelled.")
            return

        try:
            os.remove(self.FILE_NAME)

            print("\nAll journal entries have been deleted.")

        except FileNotFoundError:
            print("\nNo journal entries to delete.")

        except PermissionError:
            print("\nError: Permission denied while deleting the journal.")

        except OSError as error:
            print(f"\nError while deleting the journal: {error}")

    def show_menu(self):
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print()
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")


# Create JournalManager object
journal = JournalManager()


# Main Menu
while True:

    journal.show_menu()

    choice = input("\nEnter your choice: ").strip()

    match choice:
        case "1":
            journal.add_entry()

        case "2":
            journal.view_entries()

        case "3":
            journal.search_entry()

        case "4":
            journal.delete_all_entries()

        case "5":
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break

        case _:
            print("\nInvalid option. Please select a valid option from the menu.")