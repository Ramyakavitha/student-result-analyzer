from database import create_table, insert_student, fetch_all
from logic import rank_students, average_marks

def show_menu():
    print("\n1. Add Student\n2. Show All\n3. Rank Students\n4. Average Marks\n5. Exit")

def main():
    create_table()
    while True:
        show_menu()
        choice = input("Choose: ")
        if choice == '1':
            id = int(input("ID: "))
            name = input("Name: ")
            s1 = int(input("Subject 1: "))
            s2 = int(input("Subject 2: "))
            s3 = int(input("Subject 3: "))
            insert_student(id, name, s1, s2, s3)
        elif choice == '2':
            for s in fetch_all():
                print(s)
        elif choice == '3':
            data = fetch_all()
            ranked = rank_students(data)
            print("\nRanked Students:")
            for s in ranked:
                print(s[0], s[1], "Total:", sum(s[2:]))
        elif choice == '4':
            data = fetch_all()
            avg = average_marks(data)
            print("Average Marks:", avg)
        else:
            break

if __name__ == "__main__":
    main()
