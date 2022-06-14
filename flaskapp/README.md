# Flask app

## Dependencies

`python v3.10.3`

`pip v22.0.4`

`pip install virtualenv`

## Setup
Setup a virtualenv or add module with name flaskapp of type Flask.

setup `.env` variables

activate virtualenv with `.\Scripts\activate`

Run `pip install -r requirements.txt`

`deactivate` to leave Flask env


## Database setup, db-name: Pim

Setup a mariadb server.
`mysql -u your_mysql_username -p < .\database\reset-database.sql`

Setup tables: (inside venv)
`python .\database\setupDatabase.py`

Seed database: (inside venv)
`python .\database\seeder.py`
