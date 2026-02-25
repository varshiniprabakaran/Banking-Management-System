# ================== LIBRARY MANAGEMENT SYSTEM ==================
# Core Python only | No external libraries | Menu Driven

books = {}
users = {}

FINE_PER_DAY = 50   # Rs.2 per late day


# ---------------- ADD BOOK ----------------
def add_book():
    print("\n--- Add Book ---")
    book_id = input("Enter Book ID: ")

    if book_id in books:
        print("Book already exists!")
        return

    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    books[book_id] = {
        "name": name,
        "author": author,
        "status": "Available",
        "issued_to": None,
        "issue_date": None,
        "return_date": None
    }

    print("Book added successfully!")


# ---------------- VIEW ALL BOOKS ----------------
def view_books():
    print("\n--- All Books ---")

    if not books:
        print("No books available!")
        return

    for bid, book in books.items():
        print(f"{bid} | {book['name']} | {book['author']} | {book['status']}")


# ---------------- SEARCH BOOK ----------------
def search_book():
    print("\n--- Search Book ---")
    keyword = input("Enter Book ID or Name: ").lower()

    found = False
    for bid, book in books.items():
        if keyword == bid.lower() or keyword in book["name"].lower():
            print(f"Found → {bid} | {book['name']} | {book['status']}")
            found = True

    if not found:
        print("Book not found!")


# ---------------- ADD USER ----------------
def add_user():
    print("\n--- Add User ---")
    user_id = input("Enter User ID: ")

    if user_id in users:
        print("User already exists!")
        return

    name = input("Enter User Name: ")

    users[user_id] = {
        "name": name,
        "books": []
    }

    print("User added successfully!")


# ---------------- ISSUE BOOK ----------------
def issue_book():
    print("\n--- Issue Book ---")
    book_id = input("Enter Book ID: ")
    user_id = input("Enter User ID: ")

    if book_id not in books:
        print("Book not found!")
        return

    if user_id not in users:
        print("User not found!")
        return

    if books[book_id]["status"] == "Issued":
        print("Book already issued!")
        return

    issue_date = input("Enter Issue Date (DD-MM-YYYY): ")
    return_date = input("Enter Expected Return Date (DD-MM-YYYY): ")

    books[book_id]["status"] = "Issued"
    books[book_id]["issued_to"] = user_id
    books[book_id]["issue_date"] = issue_date
    books[book_id]["return_date"] = return_date

    users[user_id]["books"].append(book_id)

    print("Book issued successfully!")


# ---------------- RETURN BOOK ----------------
def return_book():
    print("\n--- Return Book ---")
    book_id = input("Enter Book ID: ")

    if book_id not in books:
        print("Book not found!")
        return

    if books[book_id]["status"] == "Available":
        print("Book is not issued!")
        return

    actual_return_date = input("Enter Actual Return Date (DD-MM-YYYY): ")

    expected = books[book_id]["return_date"]
    late_days = int(input("Enter number of late days (0 if on time): "))

    fine = late_days * FINE_PER_DAY

    user_id = books[book_id]["issued_to"]
    users[user_id]["books"].remove(book_id)

    books[book_id]["status"] = "Available"
    books[book_id]["issued_to"] = None
    books[book_id]["issue_date"] = None
    books[book_id]["return_date"] = None

    print("Book returned successfully!")
    print(f"Late Days: {late_days}")
    print(f"Fine Amount: Rs.{fine}")


# ---------------- CHECK STATUS ----------------
def check_status():
    print("\n--- Book Status ---")
    book_id = input("Enter Book ID: ")

    if book_id not in books:
        print("Book not found!")
        return

    book = books[book_id]
    print("Book Name :", book["name"])
    print("Status    :", book["status"])

    if book["status"] == "Issued":
        print("Issued To :", book["issued_to"])
        print("Issue Date:", book["issue_date"])
        print("Return By :", book["return_date"])


# ---------------- DELETE BOOK ----------------
def delete_book():
    print("\n--- Delete Book ---")
    book_id = input("Enter Book ID: ")

    if book_id not in books:
        print("Book not found!")
        return

    if books[book_id]["status"] == "Issued":
        print("Cannot delete issued book!")
        return

    del books[book_id]
    print("Book deleted successfully!")


# ---------------- MAIN MENU ----------------
def main_menu():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Add User")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Check Book Status")
        print("8. Delete Book")
        print("9. Exit")

        choice = input("Enter choice (1-9): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            add_user()
        elif choice == "5":
            issue_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            check_status()
        elif choice == "8":
            delete_book()
        elif choice == "9":
            print("Thank you for using Library Management System.")
            break
        else:
            print("Invalid choice!")


# ---------------- START PROGRAM ----------------
main_menu()
