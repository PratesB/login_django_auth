# Django Authentication System

This project demonstrates how to implement an authentication system using Django Auth.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Customization](#customization)
- [License](#license)


## Introduction
This project provides a complete user authentication system built with Python and Django. It leverages Django's built-in authentication features, including user management, session handling, and message display. 
This project serves as a starting point for building secure web applications with Django.

## Features
- User registration with email and password
- Secure login and logout functionality
- Utilizes Django Sessions to manage user sessions and maintain login state
- Customizable message types (info, success, warning, error).
- Uses the `@login_required` decorator with the `login_url` parameter
- Uses the `@require_http_methods` decorator
- Error handling for authentication and register issues


## Requirements
- Python 3.x or higher
- Django (latest stable version recommended)
- Python Decouple 3.x or higher
- A database system (SQLite, PostgreSQL, MySQL, etc.)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/PratesB/login_django_auth.git
    ```
2. Navigate to the project directory:
    ```sh
    cd login_django_auth
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```
4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
5. Create a `.env` file with the necessary information:
    ```sh
    touch .env
    ```
    Add your environment-specific variables in the `.env` file:
    ```
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DB_ENGINE=django.db.backends.sqlite3
    DB_NAME=db.sqlite3
    ```
6. Create a superuser (for admin access):
    ```sh
    python manage.py createsuperuser
    ```
7. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

1. Access the application in your browser: http://127.0.0.1:8000/

2. Register a new user:
Navigate to the registration page and create an account.

3. Log in:
Use your credentials to log in

4. Log out:
Use the logout functionality to end your session.

## Configuration

-   **Database:** Configure your database settings in `settings.py`.
-   **Security:** Review and adjust security settings in `settings.py` as needed.
-   **URLs:** Customize URLs in `urls.py`.
-   **Templates:** Modify templates in the `templates` directory to match your application's design.

## Customization

-   **User Model:** Extend the default Django User model to include additional fields.
-   **Forms:** Customize registration and login forms.
-   **Views:** Modify views to add custom logic.
-   **Templates:** Change the look and feel of the application.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

