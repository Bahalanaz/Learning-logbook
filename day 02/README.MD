# 👤 User Management System (Python + File Handling + OOP) 

This repository documents my progress in learning Python backend fundamentals by building a **CLI-based User Management System** with persistent data storage using JSON.

The project focuses on combining **OOP, file handling, and real-world system design concepts**.

---

# 🚀 Project Overview

The system allows users to:

- Add new users (name, role, email)
- View all stored users
- Filter users by role (admin/user)
- Persist data using JSON files
- Maintain data even after program restart

This project simulates a **basic backend database system using file storage instead of SQL**.

---

# 🧠 Concepts Learned

## 1. Object-Oriented Programming (OOP)

- Classes & Objects: User class as a data model
- Encapsulation: Structuring user data inside a class
- Methods:
  - `display()` → prints user information
  - `to_dict()` → converts object to dictionary for storage

---

## 2. File Handling & Persistence

- Reading JSON files using `json.load()`
- Writing JSON files using `json.dump()`
- Handling missing or corrupted files using `try/except`
- Persistent storage using `user.json`

---

## 3. Data Structures

- Lists: storing multiple users
- Dictionaries: representing user objects in JSON format

---

## 4. Control Flow

- if / elif / else for menu navigation
- while loop for continuous CLI execution
- for loop for iterating user data

---

## 5. System Design Thinking

- Separation of concerns:
  - User class → data model
  - Functions → logic layer
  - File system → storage layer
  - CLI → user interface

---

# 🛠️ Features

## 👤 User Management
- Add new users with name, role, email
- Store users persistently in JSON

## 📄 Data Handling
- Load users from file
- Save users back to file safely
- Handle missing/corrupt files

## 🔍 Filtering System
- Filter users by role (admin/user)
- Display only relevant results

## 🖥️ CLI Interface
- Menu-driven system
- Continuous loop until exit

---
