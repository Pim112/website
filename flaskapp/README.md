# Flask app (Windows setup)

## Dependencies

`python v3.10.3`

`pip v22.0.4`

`pip install virtualenv`

## Setup
Setup a virtualenv or add module with name flaskapp of type Flask.

setup `.env` variables

activate virtualenv with `.\venv\Scripts\activate`

Run `pip install -r requirements.txt`

`deactivate` to leave Flask env


## Database setup, db-name: Pim

Setup a mariadb server, fill in .env variables.

Delete and create the db in Mariadb
`mysql -u your_mysql_username -p < .\database\reset-database.sql`

Setup tables: (inside venv)
`python .\database\setupDatabase.py`

Seed database: (inside venv)
`python .\database\seeder.py`


## Running

To run open the environment
`.\venv\Scripts\activate`

Start the flask app
`flask run`


## Seeder data:
username `pim`
password `pim`
email `pim@bor.nl`
