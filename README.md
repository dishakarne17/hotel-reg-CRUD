# Hotel Registration CRUD App (Flask)

A simple Flask web application demonstrating full CRUD (Create, Read, Update, Delete)
operations for hotel registration, using Flask-SQLAlchemy and SQLite.

## Project Structure
```
project/
├── app.py
├── templates/
│   └── index.html
└── instance/
    └── example.db     # auto-generated on first run
```

## Features
- Create: Register a new hotel with name, location, rooms, and price per night.
- Read: View all registered hotels in a table.
- Update: Edit an existing hotel's details.
- Delete: Remove a hotel from the database.
- Uses Flask's `instance` folder convention for the SQLite database.
- If `instance/example.db` already exists, `db.create_all()` will only create
  missing tables — it will not overwrite existing data.

## Requirements
- Python 3.8+
- Flask
- Flask-SQLAlchemy

## Installation

```bash
pip install flask flask-sqlalchemy
```

## Setup & Run

1. Save `app.py` in the project root.
2. Create a `templates` folder and place `index.html` inside it.
3. Run the application:

```bash
python app.py
```

4. Flask will automatically create the `instance` folder and `example.db`
   SQLite database on first run (with the `hotel` table).
5. Open your browser at:

```
http://127.0.0.1:5000/
```

## Configuration Notes

- **Secret Key**: Set in `app.py` via `app.config['SECRET_KEY']`. Used for
  flashing messages/session security. Replace `'your-secret-key-change-this-in-production'`
  with a strong random value before deploying:

```python
import secrets
print(secrets.token_hex(16))
```

- **Database URI**: `sqlite:///example.db` resolves to `instance/example.db`
  relative to the app root (Flask-SQLAlchemy default behavior).

## Database Schema (`hotel` table)

| Column           | Type    | Description             |
|------------------|---------|--------------------------|
| id               | Integer | Primary key              |
| name             | String  | Hotel name                |
| location         | String  | Hotel location             |
| rooms            | Integer | Total number of rooms     |
| price_per_night  | Float   | Price per night ($)       |

## License
Free to use and modify for learning/demo purposes.
