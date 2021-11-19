# Carpet Cleaning

## Description

**Finding a good carpet cleaning** and **delivery/receiving of carpets** has always been a challenge.
This online service simplifies these processes for you. You can simply search through the carpet cleanings around you and find the one that most suits you. Then you can order from that carpet cleaning based on your needs (e.g. I have 3 carpets that I want them to be cleaned) and the rest of the process is taken care of automatically (By site admins and carpet cleaning's operator)

---

## Setup

1. Create migrations
```sh
> python manage.py makemigrations
```
2. Migrate
```sh
> python manage.py migrate
```
3. Create Super User
```sh
> python manage.py createsuperuser
```

Then you can run the server
```sh
> python manage.py runserver
```
you can visit the site from `localhost:8000` and also access django admin from `localhost:8000/admin/`