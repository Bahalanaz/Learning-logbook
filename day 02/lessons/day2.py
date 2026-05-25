import json
import os

BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, "user.json")


class User:
    def __init__(self, name, role, email):
        self.name = name
        self.role = role
        self.email = email

    def display(self):
        print("\nUSER INFO")
        print("Name :", self.name)
        print("Role :", self.role)
        print("Email:", self.email)

    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "email": self.email
        }


def load_users():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)


def add_user():
    name = input("Enter name: ")
    role = input("Enter role (admin/user): ")
    email = input("Enter email: ")

    user = User(name, role, email)

    users = load_users()
    users.append(user.to_dict())

    save_users(users)

    print("User added successfully!")


def display_users():
    users = load_users()

    if not users:
        print("No users found.")
        return

    for u in users:
        print("\nName :", u["name"])
        print("Role :", u["role"])
        print("Email:", u["email"])
 


def filter_users():
    role = input("Enter role to filter (admin/user): ")

    users = load_users()

    found = False
    for u in users:
        if u["role"] == role:
            print("\nName :", u["name"])
            print("Role :", u["role"])
            print("Email:", u["email"])
            found = True

    if not found:
        print("No users found for this role.")


while True:
    print(" USER MANAGEMENT SYSTEM")
    print("1. Add User")
    print("2. View Users")
    print("3. Filter Users")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        display_users()
    elif choice == "3":
        filter_users()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")