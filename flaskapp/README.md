# Flask app
## Setup
Setup a virtualenv or add module with name flaskapp of type Flask.

setup `.env` variables

activate virtualenv with `.\Scripts\activate`

Run `pip install -r requirements.txt`

`deactivate` to leave Flask env


## Database setup, Name: Pim

Setup a mariadb server.
`mysql -u root -p < .\flaskapp\database\reset-database.sql`

Setup tables: (inside venv)
`python .\database\setupDatabase.py`

Seed database: (inside venv)
`python .\database\seeder.py`
