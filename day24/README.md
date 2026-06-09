# Full-Stack Authentication System — Django REST Framework & React

---

## 🚀 Project Overview

A production-style full-stack authentication system built with **Django REST Framework** on the backend and **React** on the frontend.

This project covers the complete authentication lifecycle — registration, login, protected routes, token refresh, and logout — using JWT (JSON Web Tokens) as the security mechanism.

Both servers run independently and communicate through a REST API, simulating a real-world decoupled architecture used by companies like Shopify, Lazada, and other modern web platforms.

---

## 🧠 Concepts Learned

### 1. Custom User Model
Extended Django's `AbstractUser` to replace `username` with `email` as the primary login identifier. Implemented a custom `UserManager` with `create_user` and `create_superuser` methods.

---

### 2. JWT Authentication
Used `djangorestframework-simplejwt` to implement stateless authentication with two token types:
- **Access Token** — short-lived (15 minutes), sent with every protected request
- **Refresh Token** — long-lived (7 days), used to obtain a new access token without re-login

---

### 3. Token Blacklisting
Enabled SimpleJWT's token blacklist to invalidate refresh tokens on logout. Once a token is blacklisted, it cannot be reused — even if it has not expired yet.

---

### 4. DRF Serializers
Built `RegisterSerializer` with password confirmation validation and `UserSerializer` for safe read-only user data exposure. Passwords are always `write_only`.

---

### 5. Protected API Endpoints
Applied `IsAuthenticated` permission class to protect endpoints that require a valid JWT access token.

---

### 6. React Routing
Used `react-router-dom` to build a multi-page React application with public routes (login, register) and protected routes (dashboard).

---

### 7. Axios API Integration
Created a centralized axios instance pointing to the Django backend. All API calls flow through a single configured client.

---

### 8. Token Management in React
Stored JWT tokens in `localStorage` after login. Tokens are read on every protected request, cleared on logout, and checked on page load to determine if a user is authenticated.

---

### 9. Controlled Forms in React
Built fully controlled registration and login forms using `useState`, with real-time input binding and proper form submission handling.

---

### 10. PostgreSQL Integration
Configured Django to use PostgreSQL instead of SQLite, matching the database standard used in production environments.

---

## 🛠️ Features

### 🔐 Register
- Email and password registration
- Password confirmation validation on both backend and frontend
- Duplicate email rejection
- Passwords stored as hashed values — never plain text

---

### 🔑 Login
- Email and password authentication
- Returns JWT access and refresh tokens on success
- Redirects to dashboard on successful login

---

### 🏠 Dashboard (Protected)
- Only accessible to authenticated users
- Fetches and displays the logged-in user's data from the backend
- Redirects unauthenticated users to the login page

---

### 🔄 Token Refresh
- Expired access tokens can be silently refreshed using the refresh token
- Keeps users logged in without requiring re-authentication

---

### 🚪 Logout
- Blacklists the refresh token server-side
- Clears tokens from localStorage
- Redirects to login page

---

## 📊 Key Takeaways

- Always create a custom user model before the first migration
- JWTs are stateless — the server does not store sessions
- Short-lived access tokens reduce the attack window if a token is stolen
- Passwords must always be `write_only` in serializers
- Frontend and backend are fully decoupled — they only communicate through the API
- `transaction.atomic()` is not needed for single-write operations but becomes critical in multi-write operations like order checkout

---

## 🚀 Outcome

By completing this project, I gained practical experience in:

- Designing and implementing a secure email-based authentication system
- Connecting a React frontend to a Django REST API
- Managing JWT tokens across the full request lifecycle
- Building protected routes that redirect unauthenticated users
- Applying professional project structure for a full-stack application

---

## 🎯 Current Level
- Custom Django User models
- JWT authentication and token management
- DRF serializers and permission classes
- Full-stack API integration with React
- Protected routing in React
- PostgreSQL in Django projects
