# Musiket

## Description

Website for artists and fans alike to share their music collections and/or works.


## Features

* Users can create an account and log in to the service.
* Users can add, edit and remove music in their collection.
* Users can publish their music along with links to streaming services etc.
* Music can be tagged with various tags such as genres and contributors' names.
* Users can see others' collections.
* Users can search the service for music with keywords and/or tags.
* The service has user pages where various stats about the user's collection and published music is shown.

## Installation

Install `flask` library:

```
$ pip install flask
```

Create database table for login:

```
$ sqlite3 database.db < schema.sql
```

Run application:

```
$ flask run
```
