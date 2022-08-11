# Projet 12 : Développez une architecture back-end sécurisée en utilisant Django ORM

---

## Getting Started



1. Clone this repository using:
 ```bash 
 git clone https://github.com/pVerneuil/Epic_event_P12.git

2. Navigate to the project root.
3. Create the virtual environment using the command :

 ```bash
python -m venv <environment_name>
```

2. Activate using the virtual enviroment:

- on Linux :

```bash
source <environment_name>/bin/activate
```

- on Windows:

```bash
<environment_name>/Scripts/activate.bat
```
### Set up Postgresql database
1.Open a interactive Postgres session
```bash
sudo -u postgres psql
```
2. Create database and user 
```bash
CREATE DATABASE epic_events;
CREATE USER admin WITH PASSWORD 'admin';
```
3.Settings
```bash
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE epic_events TO admin;
```
4. Quit the session
```bash
\q
```
### Dependencies

Install packages from requirements.txt using

```bash
 pip install -r requirements.txt
 ```

## Usage

- Start the server with:

 ```bash
 python manage.py runserver
 ```

- Open the app in a web browser:  http://127.0.0.1:8000/

- you can use superuser credentails to access the admin area (/admin):
  - username : admin
  - password : azer1234
- Other users (management, sale_1, sale_2, support_1, support_2) all have 'azer1234' as password.