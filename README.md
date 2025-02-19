# FastAPI Notes App

## Project Overview
This is a simple notes management application built with FastAPI and MongoDB. The app allows users to create, view, and manage notes with the ability to mark important notes for easier identification.

## Features
- Create new notes with title and description
- Mark notes as important with a checkbox
- View all notes in a simple responsive interface
- Display important notes with special styling

## Technologies Used
- **FastAPI**: A modern, fast web framework for building APIs with Python
- **MongoDB**: NoSQL database for storing note data
- **Jinja2**: Template engine for rendering HTML
- **Bootstrap**: For responsive styling and UI components

## Key Learnings

### FastAPI Fundamentals
- Setting up API routes with FastAPI's router system
- Handling different HTTP methods (GET, POST)
- Working with request forms and response types
- Using Jinja2 templates for server-side rendering

### MongoDB Integration
- Connecting Python applications to MongoDB
- Basic operations with PyMongo
- Handling MongoDB documents in Python
- Converting between MongoDB documents and application models

### Form Handling
- Processing form submissions in FastAPI
- Handling different input types (text, textarea, checkbox)
- Form validation and error handling
- Converting form data to appropriate data types

### Common Challenges Solved
1. **Checkbox Handling**: Learned how HTML form checkbox values work - they only appear in the form data when checked
2. **Data Type Consistency**: Ensuring boolean values are properly stored and retrieved from MongoDB
3. **Template Conditionals**: Using Jinja2's conditional rendering based on data properties
4. **Collection Naming**: Maintaining consistent database collection references across operations

## Project Structure
```
/
├── main.py               # Application entry point
├── config/
│   └── db.py             # MongoDB connection setup
├── models/
│   └── note.py           # Data models
├── routes/
│   └── note.py           # API route handlers
├── schemas/
│   └── note.py           # Pydantic schemas for validation
└── templates/
    └── index.html        # Main page template
```

## Setup and Installation

### Prerequisites
- Python 3.7+
- MongoDB

### Steps
1. Clone the repository
2. Install dependencies:
   ```
   pip install fastapi uvicorn pymongo jinja2
   ```
3. Start MongoDB service
4. Run the application:
   ```
   uvicorn main:app --reload
   ```
5. Access the application at `http://localhost:8000`

## Future Improvements
- Add note editing functionality
- Implement note deletion
- Add user authentication
- Create categorization for notes
- Improve UI/UX with AJAX for seamless interactions

## Conclusion
This project served as a great introduction to FastAPI and MongoDB integration. Despite being a simple application, it covered many fundamental concepts including routing, template rendering, form handling, and database operations.
