<<<<<<< HEAD
Django CMS for local news wesite management React as front end
=======
# Local News SaaS

This project is a multivendor SaaS web application focused on local news. It allows a superuser to manage news owners, while news owners can manage their own websites through a content management system.

## Features

- Superuser management of news owners
- Content management system for news owners
- User authentication and account management
- Customizable news articles and categories

## Project Structure

```
local-news-saas
├── thefinenewsapp
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps
│   ├── accounts
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── cms
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── news
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
├── manage.py
└── requirements.txt
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd local-news-saas
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin` to manage news owners and content.
- News owners can log in to manage their own news articles and categories.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
>>>>>>> 461d915 (Initial Setup)
