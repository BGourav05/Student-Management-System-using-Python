# Student Management System Pro — Project Report

## Project Title
Student Management System Pro — Light Themed Flask App with Demo Auth & CSV Import/Export

## Summary
An enhanced student management web application built with Flask and SQLite. This demo includes role-based access (Admin/Teacher/Student) using a simple dropdown login, CSV import/export for bulk data management, and a light academic UI.

## Features
- Demo authentication with roles (Admin / Teacher / Student)
- Add / Edit / Delete students (Admin)
- Teacher view for assigned course (demo)
- Student self-view (via Student ID input at login)
- CSV Import and Export
- SQLite backend with auto initialization

## How it works
Flask routes handle role-based dashboards and CRUD operations. CSV import reads a headered CSV (student_id,name,email,course,marks). Export creates a downloadable CSV.

## Future Work
- Real authentication with hashed passwords
- User accounts and role assignment
- Pagination, filtering, and CSV validation
- Deployment and backups
