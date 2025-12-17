
# POS Inventory Backend

A backend system for managing a Point-of-Sale (POS) inventory. This project provides RESTful APIs to handle products, categories, sales, and customers for seamless inventory management.

## Features

- **Product Management**: Create, update, delete, and view products.
- **Category Management**: Organize products into categories.
- **Sales Management**: Record and manage sales transactions.
- **User Management**: Role only customer(roles-based users will be added as a future feature)
- **Authentication & Authorization**: Secure login and token-based authentication.

## Tech Stack

- **Backend**: Django / Django REST Framework
- **Database**: SQLite
- **Authentication**: JWT
- **API Testing**: Postman

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sumonstr12/Sales-Inventory-Backend.git
cd Sales-Inventory-Backend
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux

python -m venv venv
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Setup database and run migrations:

```bash
python manage.py migrate
```

5. Start the server:

```bash
python manage.py runserver
```

## API Documentation

* Base URL: `http://127.0.0.1:8000/api/`
### postman url : https://www.postman.com/crimson-crescent-733643/public/collection/e2i2qu0/pos-project-backend-copy?action=share&creator=42126728

1. First Fork the collection then test

## Feedback

As a learner, I welcome all feedback! Please feel free to fork the repository, submit a pull request, or open an issue with your suggestions to help me improve.

