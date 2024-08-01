# Todos Management System

The Todos Management System is a web application built with Django to help manage user tasks efficiently. 
It allows you to handle various aspects of tasks management. 

## Purpose

This simple to-do application is designed to help users manage their tasks efficiently. With an intuitive interface, users can create, update, and delete tasks effortlessly. 
The app also allows users to mark tasks as completed and set deadlines, ensuring better task organization and time management. It aims to provide a straightforward and user-friendly solution for keeping track of daily responsibilities and improving productivity.

## Features

- **User Authentication:** Secure login for users.
- **User Management:** View profile details and change them.
- **Tasks Management:** Manage dishes with detailed information such as name, description, price, and the type of dish.
- **Tags List:** Create tags and add tags to the tasks to have short hints about the task subject.
- **Admin Controls:** Special administrative features for managing users and data efficiently.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- SQLite (or any other preferred database)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/MykhailoIvchenko/todo-list-django.git
   cd todo-list-django
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your environment variables.
   ```env
   SECRET_KEY=your_secret_key
   ```

5. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

8. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.


To login in the application use credentials for test user:
Username: test_user
Password: user12345