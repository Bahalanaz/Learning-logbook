# 🐍 Django REST Framework Backend API System (JWT, CRUD, Permissions & Ownership)

This repository documents my progress in building a backend API system using Django REST Framework (DRF). The project focuses on developing production-style REST APIs with authentication, authorization, and structured backend architecture.

This phase represents a major transition from basic Django development into secure, scalable backend API development using industry standards like JWT authentication, DRF Generic Views, and ownership-based data protection.

---

# 🚀 Project Overview

The system allows me to:

- Build RESTful APIs using Django REST Framework  
- Implement full CRUD (Create, Read, Update, Delete) functionality  
- Connect Django models to APIs using serializers  
- Implement JWT-based authentication system  
- Protect API endpoints using authentication and authorization  
- Apply ownership-based access control (user-specific data isolation)  
- Use DRF Generic Views for cleaner and scalable backend structure  
- Understand full request → authentication → authorization → ownership → response flow  
- Design APIs following production backend architecture patterns  

This project simulates how real backend systems are structured in modern applications.

---

# 🧠 Concepts Learned

---

## 1. Django REST Framework (DRF)

DRF is a powerful toolkit that converts Django into a fully functional API framework.

Core idea: It simplifies backend API development using structured components like views, serializers, and responses.

---

## 2. API Development Structure

Backend APIs follow a layered structure:

- Views handle request logic  
- Serializers handle data validation and transformation  
- Models handle database structure  
- URLs route incoming requests  

Core idea: Backend systems are modular and layered.

---

## 3. CRUD Operations (Core Backend Logic)

Implemented full CRUD functionality:

- Create new records  
- Retrieve user-specific records  
- Update existing data  
- Delete records safely  

Core idea: CRUD is the foundation of all backend systems.

---

## 4. Django ORM (Database Layer)

Used Django ORM to interact with the database without writing SQL queries.

Core idea: ORM translates Python logic into database operations automatically.

---

## 5. JWT Authentication System

Implemented token-based authentication using JWT:

- Access token for authentication  
- Refresh token for session renewal  
- Stateless authentication (no server sessions)  
- Identity attached per request using `request.user`

Core idea: JWT is the industry standard for modern APIs.

---

## 6. Authentication vs Authorization

- Authentication: verifies user identity  
- Authorization: controls user permissions  

Core idea: Identity and access control must always be separated.

---

## 7. Permission System

Implemented role-based access control:

- `IsAuthenticated` protects endpoints  
- Only logged-in users can access APIs  
- Permissions are evaluated before view execution  

Core idea: Security must always execute before business logic.

---

## 8. Ownership-Based Access Control

Implemented user-specific data protection:

- Each note is linked to a user (owner)  
- Users can only access their own data  
- Backend enforces ownership using `request.user`  

Core idea: Real-world systems isolate data per user.

---

## 9. DRF Generic Views

Replaced manual APIView logic with Generic Views:

- ListCreateAPIView  
- RetrieveUpdateDestroyAPIView (conceptually understood)  

Core idea: Generic Views reduce boilerplate and improve scalability.

---

## 10. API Security Flow

Request lifecycle:

Client → JWT Authentication → Permission Check → Ownership Filtering → Business Logic → Response

Core idea: Security always executes before logic.

---

## 11. REST API Design Principles

- Resource-based endpoints  
- Consistent JSON responses  
- Proper HTTP status codes  
- Clean separation of concerns  
- User-based data isolation  

Core idea: APIs must be predictable and scalable.

---

# 🛠️ Features

---

## Authentication System
- JWT login system implemented  
- Access and refresh token handling  
- Stateless authentication  
- Secure API access using tokens  

---

## CRUD API System
- Notes API implemented  
- Clean RESTful structure  
- Validation and error handling included  

---

## Security System
- Authentication-protected endpoints  
- Ownership-based access control  
- User-specific data filtering  
- Secure request handling flow  

---

## Backend Architecture Upgrade
- Migrated from APIView to DRF Generic Views  
- Reduced boilerplate code  
- Improved scalability and maintainability  
- Cleaner production-style structure  

---

# 🧪 Key Takeaways

- DRF is the standard for modern Django APIs  
- JWT enables stateless authentication  
- CRUD is the foundation of backend systems  
- Permissions are critical for security  
- Ownership is required for real-world applications  
- Generic Views improve production scalability  
- Backend systems must enforce security first  
- Clean architecture is essential for real-world applications  

---

# 🚀 Outcome

By completing this project, I now understand:

- How to build RESTful APIs using Django REST Framework  
- How JWT authentication works in backend systems  
- How to secure APIs using authentication and permissions  
- How ownership-based access control works in real applications  
- How serializers connect models to APIs  
- How production backend architecture is structured  
- How request lifecycle works internally in DRF  

---

# 🎯 Current Level

I am progressing from beginner Django development to junior backend engineer level with strong understanding of:

- API design  
- Authentication systems  
- Authorization and ownership control  
- Database interaction using ORM  
- Backend security concepts  
- Production-style API architecture  