from kaggle.api.kaggle_api_extended import KaggleApi
import psycopg2

def readFile(fileName):
    with open(fileName, 'r') as file:
        return file.read()

def get_conn():
    c = psycopg2.connect(host="localhost", database="linear_regression", user="postgres", password="Bluejay9!")
    return c

def downloadDataset():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('gregorut/videogamesales', unzip=True)


def readSQLfiles(conn, sqlstring):
    ...