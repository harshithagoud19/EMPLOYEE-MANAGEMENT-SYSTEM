import sqlite3
from prettytable import PrettyTable

# ---------- Database Setup ----------
conn = sqlite3.connect("employees.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS employee(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age  INTEGER,
    dept TEXT
)
""")
conn.commit()

# ---------- Functions ----------
def add_employee():
    name = input("Name : ")
    age  = input("Age  : ")
    dept = input("Dept : ")
    cur.execute("INSERT INTO employee(name, age, dept) VALUES (?,?,?)",
                (name, age, dept))
    conn.commit()
    print("✔ Employee added\n")

def view_employees():
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    if not rows:
        print("No employees found.\n")
        return
    table = PrettyTable(["ID","Name","Age","Dept"])
    for r in rows:
        table.add_row(r)
    print(table, "\n")

def update_employee():
    emp_id = input("Enter employee ID to update: ")
    name = input("New Name : ")
    age  = input("New Age  : ")
    dept = input("New Dept : ")
    cur.execute("""UPDATE employee SET name=?, age=?, dept=? WHERE id=?""",
                (name, age, dept, emp_id))
    conn.commit()
    print("✔ Employee updated\n")

def delete_employee():
    emp_id = input("Enter employee ID to delete: ")
    cur.execute("DELETE FROM employee WHERE id=?", (emp_id,))
    conn.commit()
    print("✔ Employee deleted\n")

# ---------- Menu Loop ----------
def main():
    while True:
        print("=== Employee Management ===")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Choose option: ")
        if   choice == "1": add_employee()
        elif choice == "2": view_employees()
        elif choice == "3": update_employee()
        elif choice == "4": delete_employee()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
    conn.close()
