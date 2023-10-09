# chart_web_app
This is a documented tutorial on how to make a web application with Python and postgreSQL.

## Before you start
Create a repository

Make sure to make a python gitignore file and in the gitignore file

make a directory called chart_web_app

get the SSH key from the code dropdown and run
`
git clone <insert SSH Key>
`.
This will make a folder which copies over the gitignore and readme files to your computer.

In the .gitignore file, uncomment the last line.

Download the requirements.txt file and make sure it's in the same folder as the gitignore and readme files.

Create a database in postgreSQL.



## Installing PyPI packages

In the command-line, run:
```
pip install kaggle
```
Log into [Kaggle](kaggle.com) and go to [settings](kaggle.com/settings) and get an API token, 
place it in the hidden .kaggle folder.

This will enable usage of the Kaggle API which will allow you to download datasets from the website.

in the command line, run:

```
pip install psycopg2
```
This might not work if using Mac OS, run instead:
```
pip install psycopg2-binary
```

This will allow you to connect to postgres.

```
pip install Flask
```
This will allow you to create a web application using python.

```
pip install matplotlib
```
This will allow you to create graphs in your web application.

in the chart_web_app folder, create a file called utils.py. This will contain all of your utility functions

create two functions in utils.py

one to turn the contents of a file into a string

```python
def file2string(file_name):
    with open(file_name, 'r') as file:
        return file.read()
```

another to run multiple sql commands at once

```python
def runsqls(conn, sqlstring):
    cur = conn.cursor()
    sqls = sqlstring.split(';')
    for sql in sqls:
        cur.execute(sql)
    conn.commit()
    cur.close()
```

create another file called dataProcessing.py

This file will process and clean the dataset which contains some values which make translating it into an SQL table difficult.

Start the file with:
```python
from kaggle.api.kaggle_api_extended import KaggleApi
import psycopg2
import utils as u
```

create a function called download_dataset() which will use the kaggle API to download the dataset.

```python
def download_dataset():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('gregorut/videogamesales', unzip=True)
```
if you wish to use a different dataset, use `user/dataset_name`

Then create a function that will return a connection object:

```python
def get_conn():
    c = psycopg2.connect(host="localhost", database="linear_regression", user="postgres", password="***")
    return c

```




Then create a folder called db, then create two folders in db called sqls and tables.

in tables, create an sql file and configure it to postgreSQL, in the file:

```postgresql
drop table if exists vgsales;
create table vgsales
(
    rank            int,
    name            varchar(512),
    platform        varchar(128),
    Year            int,
    genre           varchar(128),
    publisher       varchar(128),
    na_Sales        decimal,
    eu_Sales        decimal,
    gp_Sales        decimal,
    other_Sales     decimal,
    global_Sales    decimal
)
```
This is the actual command that will make the table in postgres

then create a function that will call that command.

```python
def create_vgsales_table():
    conn = get_conn()
    create_sql = u.file2string('db/tables/vgsales.sql')
    u.runsqls(conn, create_sql)
    conn.close()
```
This function will create a connection object, run the vgsales.sql, and then close the connection.

Before we can insert the values of the vgsales.csv, you need to clean the values which have some null values.

```python
def clean_table():
    insert_str = ""
    data = u.file2string('vgsales.csv')
    data = data.replace("'", " ")
    data = data.replace("N/A", 'NULL')
    data = data.replace(";", '')
    rows = data.split('\n')
    header = rows[0].split(',')
```
This will replace values that would raise errors when translating the csv files into the postgres table. 
This will also split the csv file into a list of rows and create a list of all the headers of the table. 


