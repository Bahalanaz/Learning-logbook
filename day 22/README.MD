## 🚀 Folder Overview

This Folder focuses on strengthening core React concepts such as state handling, controlled inputs, side effects using `useEffect`, and building interactive components.

It includes multiple mini-project components that simulate real-world UI behavior like task management, timing systems, dynamic document updates, and live style changes.

---

## 🧠 Concepts Learned

### 1. useState Hook
Used to manage dynamic data inside functional components such as:
- Task lists
- Timer values
- Input fields
- Color values

It enables React components to re-render when data changes.

---

### 2. Event Handling
React events like `onClick` and `onChange` are used to capture user interactions and update state accordingly.

Examples:
- Adding and deleting tasks
- Moving tasks up and down
- Starting/stopping stopwatch
- Updating input fields
- Changing colors

---

### 3. useEffect Hook
Used to handle side effects such as:
- Updating the document title dynamically (Counting component)
- Running intervals for the stopwatch timer
- Managing lifecycle-based logic

---

### 4. Controlled Components
Form inputs are fully controlled using React state:
- Text input for tasks
- Color picker input
- Live synchronization between UI and state

---

### 5. Array State Manipulation
Learned how to properly update arrays in React state:
- Add items using spread operator
- Delete items using `filter`
- Reorder items using swap logic (move up/down)

---

## 🛠️ Features

### 📝 ToDo List Application
- Add new tasks
- Delete tasks
- Move tasks up and down
- Prevent empty task submission
- Uses array state manipulation

---

### ⏱️ Stopwatch Component
- Start, stop, and reset functionality
- Time tracked in milliseconds
- Real-time updates using `setInterval` inside `useEffect`
- Proper cleanup using `clearInterval`
- Time formatted into HH:MM:SS.ms

---

### 🔢 Counting Component
- Increment and decrement counter
- Updates document title dynamically using `useEffect`
- Demonstrates side effects tied to state changes

---

### 🎨 Color Picker Component
- Select a color using HTML color input
- Live preview of selected color
- Dynamic background styling using React state

---

## 📊 Key Takeaways

- React state drives UI updates
- `useEffect` is essential for handling side effects like intervals and DOM updates
- Array state must be copied before modification
- Controlled components keep UI and data in sync
- Small components can be combined to build full applications

---

## 🚀 Outcome

By completing this project, I gained practical experience in:

- Managing complex state in React
- Handling real user interactions
- Using `useEffect` with proper cleanup logic
- Building interactive UI components
- Structuring multiple independent React features in one app

---

## 🎯 Current Level

- State management (intermediate)
- Event handling (intermediate)
- Side effects with `useEffect` (beginner → intermediate)
- Component-based UI design
- Mini React application building