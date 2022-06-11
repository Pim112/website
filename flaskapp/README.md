# Flask app
## Setup
Setup a virtualenv or add module with name flaskapp of type Flask.

activate virtualenv with `.\Scripts\activate`

Run `pip install -U flask-cors`

`deactivate` to leave Flask env


## Database setup

Setup a mariadb server.
`mysql -u root -p < C:\Users\pim_b\IdeaProjects\website\flaskapp\database\reset-database.sql`

Setup tables: (inside venv)
`python .\database\setupDatabase.py`

Seed database: (inside venv)
`python .\database\seeder.py`
