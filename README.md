
---

# 📚 Library Management System

[![Django Version](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Bootstrap Version](https://img.shields.io/badge/Bootstrap-5-purple.svg)](https://getbootstrap.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-blue.svg)](https://www.sqlite.org/index.html)

A full-featured digital library platform built with Django. This system allows users to manage their accounts, browse a catalog of books, and handle borrowing and returning transactions through a personal wallet system.


<!-- ## 🌐 Live Demo -->


<!-- **[🔗 Visit the Live Application](https://your-live-demo-url.com/)** -->

<!-- *Explore the live application to test user registration, book browsing, the deposit system, and the borrowing/returning process.* -->

## 📋 Project Overview

This Library Management System is a robust web application designed to digitize and streamline the core functionalities of a physical library. Built on the powerful Django framework, it provides a seamless experience for both library members and administrators.

The project's architecture demonstrates a clear separation of concerns, with dedicated Django apps for handling user accounts, book catalogs, categories, and financial transactions. A key feature is the integrated user wallet system, which requires users to deposit funds before they can borrow books, simulating a real-world library membership or fee-based model.

## ✨ Features

### 🔐 User Account Management
- **Secure Registration & Authentication**: Full user registration, login, and logout capabilities with password management.

### 📚 Core Library Functions
- **Dynamic Book Catalog**: A comprehensive display of available books, filterable by category.
- **Book Returning System**: Users can return borrowed books from their profile, which makes the book available for others.

### 🔧 Administrative Tools
- **Django Admin Panel**: A powerful backend interface for complete control over the library's data.
- **Book & Category Management**: Administrators can easily add, update, and delete books and categories.

## 🛠️ Technologies Used

### Backend
- **Python 3.10**: Core programming language.
- **Django 5.2**: High-level web framework for rapid, secure, and scalable development.
- **Django Crispy Forms**: For creating elegant and DRY forms.

### Frontend
- **HTML5**: Standard markup language for creating web pages.
- **CSS3**: Styling for visual design and layout.
- **Bootstrap 5**: Popular CSS framework for responsive.

## ⚙️ Setup and Installation (Local)

Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

### Prerequisites
- Python 3.10 
- Git

### Installation Steps

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/roniahamed/Library_Management.git
    cd Library_Management
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a Superuser**
    -   This account will have access to the Django Admin panel.
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

7.  **Access the Application**
    -   **Main Site:** Open your web browser and go to `http://127.0.0.1:8000/`
    -   **Admin Panel:** Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

## 🔮 Future Improvements

### Technical Enhancements
-   **REST API**: Develop a RESTful API using Django REST Framework to support a mobile application or other clients.
-   **Caching**: Integrate Redis for caching frequently accessed data to improve performance.
-   **Containerization**: Add Docker and Docker Compose files for easier setup and deployment.
-   **Automated Testing**: Write unit and integration tests to ensure code quality and reliability.
-   **CI/CD Pipeline**: Set up a continuous integration/continuous deployment pipeline using GitHub Actions.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/roniahamed/Library_Management/issues).

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 👨‍💻 Author & Contact

**Roni Ahamed**
-   **GitHub**: [@roniahamed](https://github.com/roniahamed)
-   **LinkedIn**: [Connect with me](https://www.linkedin.com/in/roniahamed/)

---

**⭐ If you find this project useful, please consider giving it a star on GitHub!**

*This project was built with a passion for clean code and robust back-end solutions.*