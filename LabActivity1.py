def check_borrowing(overdue_books, status):
    if overdue_books not in ["yes",'y'] and status in ["active","a"]:
        return "Borrowing allowed"
    elif status in ["suspended","s"]:
        return "Not allowed: suspended account"
    elif overdue_books in ["yes","y"]:
        return "Not allowed: overdue books"
    else:
        return "Invalid Answer"

successfully_allowed = 0
while True:
    name = input("'exit' to stop/ name:").strip()

    if name == "exit":
        break

    overdue = input("overdue books (yes/no):").lower()
    student_status = input("Status: (active/suspended):").lower()

    is_overdue = overdue

    result = check_borrowing(is_overdue, student_status)

    if result == "Borrowing allowed":
        while True:
            books = int(input("How many books you want to borrow minimum: 3.. :"))
            if books <= 3 and books >= 1:
                successfully_allowed +=1
                print("Borrow status: Successfully!!!")
                break
            elif books >= 3:
                print("Warning: Invalid Amout, Mimimum is 3!!")
            elif books == 0:
                print("Invalid Amout: '0'!! Try again.")
            else:
                print("Invalid Input: Try again")
    else:
        print(result)

    print()

    print("successfully allowed to borrow books:", successfully_allowed)