# chart_web_app
This is a documented tutorial on how to make a web application with Python and postgreSQL.

## Before you start
Create a repository

Make sure to make a python gitignore file and in the gitignore file

make a directory called chart_web_app

get the SSH key from the code dropdown and run 

```
git clone <SSH Key>
```
This will make a folder which copies over the gitignore and readme files to your computer.

In the 

Download the requirements.txt file and make sure it's in the same folder as the gitignore and readme files.

Create a database in postgreSQL.

In the command-line, run:
```
pip install kaggle
```
Log into [Kaggle](kaggle.com) and go to [settings](kaggle.com/settings) and get an API token, place it in the hidden .kaggle folder.

This will enable usage of the Kaggle API which will allow you to download datasets from the website.









# <img alt="Java" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

in the chart_web_app folder, create a file called utils.py. This will contain all of your utility functions

in the command line, run:

```
pip install psycopg2
```
This might not work if using Mac OS, run instead:
```
pip install psycopg2-binary
```
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

This file will 