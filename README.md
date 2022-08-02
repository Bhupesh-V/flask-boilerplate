# flask-boilerplate

A boilerplate to make apps using Flask


## Setup

1. Install dependencies
   ```bash
   pip3 install -r requirements.txt
   ```
2. Export env variables
   ```bash
   export FLASK_APP=app
   export FLASK_ENV=development
   ```
3. Setup `migrations` directory
   ```bash
   flask db init
   ```
4. Create the datbase `db.sqlite3`
   ```bash
   flask db migrate
   ```
5. Create the models
   ```bash
   flask db upgrade
   ```
