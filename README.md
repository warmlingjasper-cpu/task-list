Task List

A simple task management application built with Django.

About

Task List is a web application for managing tasks. It allows users to create, edit, delete, and filter tasks by date.

This project was developed as a Django practice project, focusing on CRUD operations, ModelForms, template rendering, date filtering, form validation, and Bootstrap styling.

Features
Create tasks
Edit tasks
Delete tasks
Task status management
Start and end dates
Filter tasks by date range
Quick "Today" filter
Form validation
Responsive layout
Dark theme

Technologies:
Python
Django
HTML5
CSS3
JavaScript
Bootstrap 5
SQLite

<img width="1223" height="451" alt="image" src="https://github.com/user-attachments/assets/8daf55cb-e696-4dbe-8081-a95a8d6eacd4" />


Installation
1. Clone the repository
git clone https://github.com/warmlingjasper-cpu/task-list.git
cd task-list
2. Create a virtual environment
Windows
python -m venv venv
venv\Scripts\activate
macOS / Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Apply migrations
python manage.py migrate
5. Run the development server
python manage.py runserver

Open your browser and access:

http://127.0.0.1:8000/
Project Structure
task-list/
│
├── tasklist/
│   ├── migrations/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
Database

This project uses SQLite for development.

The db.sqlite3 file is not included in the repository. After cloning the project, run:

python manage.py migrate

Django will create a new local database automatically.

Future Improvements
User authentication
User-specific tasks
Task priority
Search functionality
Pagination
Task categories
Deployment to a production environment
Author

Lucas Warmling Jasper

GitHub: https://github.com/warmlingjasper-cpu
