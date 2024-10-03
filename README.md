# TodoList API

This is a simple Todo List API built with Django and Django REST Framework (DRF). The project allows users to create an account, log in, and manage their personal todo tasks. Each user can create, view, update, and delete their own tasks while using JWT-based authentication to secure the endpoints.

## Features

- **User Registration:** Users can create an account to start using the API.
- **JWT Authentication:** Secure access using JSON Web Tokens (JWT) for login and authorization.
- **Create Tasks:** Authenticated users can create their own todo tasks.
- **List Tasks:** Users can view a list of their own tasks, which are filtered by their user account.
- **Update and Delete Tasks:** Users can update or delete their tasks.
- **API Documentation:** The project includes a Swagger UI and Redoc for interactive API documentation.

## Endpoints

- **/register/**: Register a new user.
- **/login/**: Obtain JWT tokens for authentication.
- **/token/refresh/**: Refresh JWT tokens.
- **/todos/**: List all the authenticated user's tasks or create a new task.
- **/todos/<int:pk>/**: Retrieve, update, or delete a specific task by its ID (only if it belongs to the user).

## Technologies Used

- **Django**: Web framework for rapid development.
- **Django REST Framework**: Toolkit for building Web APIs.
- **SQLite**: Relational database used to store user and task data.
- **drf-yasg**: Swagger and Redoc documentation for the API.
- **JWT (JSON Web Token)**: For authentication and authorization.

## Images:

![image](https://github.com/user-attachments/assets/beed9f8a-b384-4a6a-ba30-b8a08fb55abe)

![image](https://github.com/user-attachments/assets/adfde247-309c-43c3-b463-2b8ee81f173c)



## Future Improvements

- Add support for task deadlines and reminders.
- Implement search functionality to filter tasks by title or description.
- Add a frontend interface for easier interaction with the API (possibly using React or Vue.js).
