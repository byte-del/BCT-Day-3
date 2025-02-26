from prettytable import PrettyTable

l = []

def signup():
    email = input("Enter email id: ")
    password = input("Enter password: ")
    a = {"email": email, "password": password}
    l.append(a)
    print("Signup successful")

def signin():
    email = input("Enter email id: ")
    password = input("Enter password: ")
    
    for user in l:
        if user["email"] == email and user["password"] == password:
            print("Signin successful")
            return
    print("Invalid credentials")

def display_users():
    if not l:
        print("No users have signed up yet.")
        return
    
    table = PrettyTable(["Email", "Password"])
    
    for user in l:
        table.add_row([user["email"], user["password"]])
    
    print(table)

while True:
    print("\n1. Signup\n2. Signin\n3. Display Users\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        signup()
    elif choice == "2":
        signin()
    elif choice == "3":
        display_users()
    elif choice == "4":
        print("Exiting")
        break
    else:
        print("Invalid choice, try again.")
