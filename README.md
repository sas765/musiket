# Musiket

## Description

Website for music lovers to share their taste and recommend new music to others based on their tastes.


## Features

* Users can create an account and log in to the service.
* Users can add, edit and remove music in their collection.
* Music can be classified with tags such as release type and format.
* Users can see others' collections and entries to their collections.
* Users can discuss on others' entries and their own.
* Users can search the service for music with keywords.
* The service has user pages where the entries in their collection and stats about said collection are shown.
* Users can add and remove images in entries in their collection.

## Installation

Install `flask` library:

```
$ pip install flask
```

Set up database:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Run application:

```
$ flask run
```
