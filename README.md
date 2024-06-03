# Blog API

This is a blog to learn about DRF

## Installation

### For Development

Clone from Github.

Install a virtual environment if needed.

Install the requirements

```bash
pip install -r requirements.txt
```

Create a .env file add the following...

Create  secret key = ```python -c "import secrets; print(secrets.token_urlsafe())"```

```bash
DEBUG=True
SECRET_KEY=
DATABASE_URL=sqlite:///db.sqlite3
```

Make sure the server is working.

```python
python manage.py runserver
```

### For Production

The current setup can be deployed to Heroku.

If deployed, one must then also install psycopg2 to use PostgreSQL.

## Usage

There is 4 custom commands to help populate the database.

Users are needed first to then make posts.

```python
# Will always create 1 admin, and n amount of other users. username=admin, password=testpass123. Same password for all other accounts.
python manage.py create_users 6

# Deletes all users.
python manage.py del_all_users

# Creates n amount of posts.
python manage.py create_posts 12

# Deletes all posts.
python manage.py del_all_posts
```

Check out the schema for the api endpoints.

```
http://127.0.0.1:8000/api/schema/swagger-ui/
or
http://127.0.0.1:8000/api/schema/redoc/
```