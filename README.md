## Backend

### Install all required packages

`pip install -r requirements.txt`

### Add db configuration eg.

```
[my_service]
host=localhost
user=<user>
dbname=fxmag_currency_calc_development
port=5432
```

### firstly create db in psql
`CREATE DATABASE fxmag_currency_calc_development;`

### make migration

`python manage.py migrate`

### seed data
`python3 manage.py loaddata currency_rate`

### run tests

`python3 manage.py test`

### rejest crone
`python3 manage.py crontab add`

### run server
`python3 manage.py runserver`

## Frontend

### install packages
`npm install`

### run server, from frontend folder run
`npm start`



TODO:
- dockeryzacja
- testy menagement command(vcrpy), serializerów, modeli, frontu
- dodanie poetry
- stylizacja na froncie
