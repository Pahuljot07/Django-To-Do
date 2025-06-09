"# Django To-Do App"

This is a task management application built using Django and Django REST Framework. It allows users to register, log in, create and manage their personal task list. The application is styled using Bootstrap 5 for a responsive and modern interface.

"# Features"

- User Registration and Login
- Secure Logout
- Create, Read, Update, and Delete (CRUD) tasks
- Mark tasks as completed or keep them pending
- View tasks separated by status: Pending and Completed
- Search tasks by keyword in title or description
- View task details in a modal popup
- REST API for all core functionalities

"# Tech Stack"

- Python 
- Django 
- Django REST Framework
- SQLite (for local development)
- Bootstrap 5
- Bootstrap Icons
- django-widget-tweaks (for better form rendering)

"# Setup Instructions"

" 1. Clone the Repository"

```bash
git clone https://github.com/Pahuljot07/Django-To-Do.git
cd django-todo-app

"# 2. Create Virtual Environment"
python -m venv venv
source venv/bin/activate       

"# 3. Install Dependencies"
pip install -r requirements.txt

"# 4. Apply Migrations"
python manage.py migrate

"# 5. Run The Development Server"
python manage.py runserver


