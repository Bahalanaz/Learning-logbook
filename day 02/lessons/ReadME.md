This repository documents my progress in mastering Python, moving from basic syntax and data structures to building a persistent User Management System using JSON and File I/O.

🚀 Concepts Learned

1. Python Fundamentals
Variables & Data Types: Practical use of strings, integers, floats, and booleans.

Control Flow:
Conditional Logic: Implementing if/elif/else statements and logical operators (and).
Loops: Using for loops to iterate over collections and while loops with control statements like continue.
Functions: Defining modular code blocks with parameters and return values to ensure code reusability.

2. Data Structures
Lists: Managing ordered collections using .append(), .remove(), and indexing.
Dictionaries: Storing data in key-value pairs and using .items() for clean iteration.
Nested Structures: Creating complex datasets by nesting dictionaries inside lists (e.g., a list of user profiles).

3. Object-Oriented Programming (OOP)
Classes & Objects: Understanding the blueprint of a Class.
The __init__ Method: Using constructors to initialize object attributes (name, email).
Methods: Defining functions within a class to handle object-specific behavior.

4. File Handling & Persistence
Plain Text (TXT): Reading (r), writing (w), and appending (a) data to files using context managers (with open).

JSON Manipulation:
Serialization: Converting Python objects to JSON using json.dump.
Deserialization: Loading JSON data back into Python using json.load.

Path Management: Using the os module (os.path.join) to handle file paths dynamically across different operating systems.

5. Error Handling & Robustness
Try/Except Blocks: Implementing defensive programming to handle FileNotFoundError and json.JSONDecodeError, ensuring the program doesn't crash when files are missing or corrupted.

🛠️ Applied Project: User Management System
The culmination of these skills is a CLI-based User Management System. This application allows for:

Adding Users: Saves user data (Name/Role/Email) to a persistent user.json file.
Data Retrieval: Reads and displays all stored users.
Filtering: A search function to filter users based on specific roles (Admin/User).
Persistence: Data remains saved even after the program is closed.